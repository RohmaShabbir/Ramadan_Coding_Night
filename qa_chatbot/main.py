import google.generativeai as genai # for goggle genai API
from dotenv import load_dotenv # for loading envoironment variable
import os # for envorinment variable
import chainlit as cl # for chatbot interface

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with the API key
genai.configure(api_key=gemini_api_key)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Chainlit decorator for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    # Send welcome message to user 
    await cl.Message(content="Hello! how can I help you today?").send()

# Chainlit decorater for when a new message in recived 
@cl.on_message
async def handle_message(message: cl.Message):
    
    # Get the message content from user
    prompt = message.content

    # Generative response using Gemini model
    response = model.generate_content(prompt)

    # Extract text from response, or empty string if on text attribute
    response_text = response.text if hasattr(response, "text") else ""

    # Send response back to user
    await cl.Message(content=response_text).send()
