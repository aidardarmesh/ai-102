from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    
    # connect to the project
    project_endpoint = os.getenv("FOUNDRY_PROJECT_URL")
    project_client = AIProjectClient(            
            credential=DefaultAzureCredential(),
            endpoint=project_endpoint,
        )
    
    # Get a chat client
    chat_client = project_client.get_openai_client(api_version="2024-10-21")
    
    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")
    
    response = chat_client.chat.completions.create(
        model=os.getenv("FOUNDRY_MODEL_NAME"),
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_prompt}
        ]
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)