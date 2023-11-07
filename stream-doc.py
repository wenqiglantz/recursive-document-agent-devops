# 2023-11-06 Adding a Streamlit interfacee
# remember to pip install streamlit .
#
import streamlit as st
from llama_index import (
    VectorStoreIndex,
    ListIndex,
    SimpleDirectoryReader,
    ServiceContext
)
from llama_index.retrievers import RecursiveRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import get_response_synthesizer
from llama_index.schema import IndexNode
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.llms import OpenAI
from llama_index.agent import OpenAIAgent
from dotenv import load_dotenv
import openai
import os

#loads dotenv lib to retrieve API keys from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#define LLM service
llm = OpenAI(temperature=0.1, model_name="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

titles = [
    "DevOps Self-Service Pipeline Architecture and Its 3–2–1 Rule", 
    "DevOps Self-Service Centric Terraform Project Structure", 
    "DevOps Self-Service Centric Pipeline Security and Guardrails"
    ]

# Use the st.cache_data decorator to cache the results of this function
@st.cache_data
def load_and_index_documents(titles):
    documents = {}
    agents = {}
    for title in titles:
        # Load documents
        documents[title] = SimpleDirectoryReader(input_files=[f"data/{title}.pdf"]).load_data()
    
        # Build vector and list indexes
        vector_index = VectorStoreIndex.from_documents(documents[title], service_context=service_context)
        list_index = ListIndex.from_documents(documents[title], service_context=service_context)
        
        # Define query engines
        vector_query_engine = vector_index.as_query_engine()
        list_query_engine = list_index.as_query_engine()

        # Define tools
        query_engine_tools = [
            QueryEngineTool(
                query_engine=vector_query_engine,
                metadata=ToolMetadata(
                    name="vector_tool",
                    description=f"Useful for retrieving specific context related to {title}",
                ),
            ),
            QueryEngineTool(
                query_engine=list_query_engine,
                metadata=ToolMetadata(
                    name="summary_tool",
                    description=f"Useful for summarization questions related to {title}",
                ),
            ),
        ]

        # Build agent
        function_llm = OpenAI(model="gpt-3.5-turbo-0613")
        agent = OpenAIAgent.from_tools(
            query_engine_tools,
            llm=function_llm,
            verbose=True,
        )
        agents[title] = agent

    return agents

# Use the st.cache_data decorator to cache the initialization of the query engine
@st.cache_data
def get_query_engine():
    # Define index nodes that link to the document agents
    nodes = [IndexNode(text=f"This content contains details about {title}.", index_id=title) for title in titles]

    # Define retriever
    vector_index = VectorStoreIndex(nodes)
    vector_retriever = vector_index.as_retriever(similarity_top_k=1)

    # Define recursive retriever
    recursive_retriever = RecursiveRetriever(
        "vector",
        retriever_dict={"vector": vector_retriever},
        query_engine_dict=load_and_index_documents(titles),
        verbose=True,
    )

    # Get response synthesizer
    response_synthesizer = get_response_synthesizer(response_mode="compact")

    # Initialize the query engine
    query_engine = RetrieverQueryEngine.from_args(
        recursive_retriever,
        response_synthesizer=response_synthesizer,
        service_context=service_context,
    )

    return query_engine

# Initialize the query engine once and cache it
query_engine = get_query_engine()

# Streamlit app starts here
def main():
    st.title('Document Query Interface')
    query = st.text_input('Enter your query:', '')
    response_placeholder = st.empty()

    if st.button('Search'):
        with st.spinner('Searching...'):
            response = query_engine.query(query)
            response_placeholder.markdown(response)

def stream_response(query, agents):
    # This is a mock-up function to simulate streaming of responses.
    # You would replace this with the actual logic to get chunks of the response.
    # For example, if your response is a generator that yields strings:
    for part in query_engine.query(query):
        yield part
    # If query_engine.query(query) returns a single string, you would need to
    # implement logic to split it into chunks and yield them one by one.

# Run the Streamlit app
if __name__ == '__main__':
    main()