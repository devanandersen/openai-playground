import openai
from dotenv import load_dotenv
import os

def set_openai_key():
    # Load the .env file
    load_dotenv()
    # Set your OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
