# recursive-document-agents-devops
Refer to my blog [Building Production-Ready LLM Apps With LlamaIndex: Recursive Document Agents for Dynamic Retrieval](https://betterprogramming.pub/building-production-ready-llm-apps-with-llamaindex-recursive-document-agents-for-dynamic-retrieval-1f4b25287918?sk=d1e9646f77030401df946805e96e6dc7) for details.

## Application Setup

```
conda create --name py38_env python=3.11
conda activate py38_env
pip install -r requirements.txt
```

Also add `.env` file at the project root and replace placeholder with your API key:
```
OPENAI_API_KEY=<YOUR-API-KEY>
```

Now run the app by kicking off this command:
```
python doc-agent.py
```
