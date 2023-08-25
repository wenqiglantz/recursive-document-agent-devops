# recursive-document-agents

## Application Setup

```
conda create --name py38_env 
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
