import os
import textwrap
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

# Load dotenv lib to retrieve API keys from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define LLM service
llm = OpenAI(temperature=0.1, model_name="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

# Define the folders containing markdown files
folders = ['cli-commands', 'pd-concepts', 'pd-user-guide']

def find_markdown_files(directory):
    """
    Recursively finds all markdown files in the given directory and its subdirectories.
    """
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

# Load markdown files from each folder and its subfolders
documents = {}
for folder in folders:
    folder_path = os.path.join("data", folder)
    markdown_files = find_markdown_files(folder_path)
    documents[folder] = SimpleDirectoryReader(input_files=markdown_files).load_data()
# Build agents for each folder
agents = {}
for folder, docs in documents.items():
    # Build indexes and query engines
    vector_index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    list_index = ListIndex.from_documents(docs, service_context=service_context)
    vector_query_engine = vector_index.as_query_engine()
    list_query_engine = list_index.as_query_engine()

    # Define tools
    query_engine_tools = [
        QueryEngineTool(query_engine=vector_query_engine, metadata=ToolMetadata(name="vector_tool", description=f"Useful for retrieving specific context related to {folder}")),
        QueryEngineTool(query_engine=list_query_engine, metadata=ToolMetadata(name="summary_tool", description=f"Useful for summarization questions related to {folder}")),
    ]

    # Build agent
    function_llm = OpenAI(model="gpt-3.5-turbo-0613")
    agent = OpenAIAgent.from_tools(query_engine_tools, llm=function_llm, verbose=True)
    agents[folder] = agent

# Define index nodes and retriever
nodes = [IndexNode(text=f"This content contains details about {folder}.", index_id=folder) for folder in folders]
vector_index = VectorStoreIndex(nodes)
vector_retriever = vector_index.as_retriever(similarity_top_k=1)

# Define recursive retriever
recursive_retriever = RecursiveRetriever("vector", retriever_dict={"vector": vector_retriever}, query_engine_dict=agents, verbose=True)

# Define response synthesizer and query engine
response_synthesizer = get_response_synthesizer(response_mode="compact")
query_engine = RetrieverQueryEngine.from_args(recursive_retriever, response_synthesizer=response_synthesizer, service_context=service_context)

def wrap_text(text, width):
    """
    Wraps the given text to the specified width.
    """
    return textwrap.fill(text, width)

# User-defined line width
line_width = int(input("Enter the desired line width for responses: "))

# User Interface
def user_interface():
    print("Welcome to the Document Query Interface. Type 'TERMINATE' to exit.")
    
    # Request for line width input
    line_width = int(input("Enter the desired line width for responses: "))
    
    while True:
        query = input("Enter your query (or type 'TERMINATE' to exit): ")
        if query.upper() == 'TERMINATE':
            print("Exiting the program.")
            break
        
        response = query_engine.query(query)
        wrapped_response = wrap_text(response, line_width)
        print(wrapped_response)
        
if __name__ == '__main__':
    user_interface()
