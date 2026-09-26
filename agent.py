from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain.tools import ToolRuntime
from tavily import TavilyClient
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
import io
import discord
import asyncio

load_dotenv()

tavily_client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))
hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

# Add these global variables at the top of agent.py
_current_message = None
_current_loop = None


def set_discord_context(message, loop):
  global _current_message, _current_loop
  _current_message = message
  _current_loop = loop


@tool
def generateImage(query: str):
  """Use this tool to generate and send image"""
  try:
    print(f"Generating image for query: {query}")
    image = hf_client.text_to_image(
        query, model="stabilityai/stable-diffusion-xl-base-1.0"
    )

    file_path = "temp_image.png"
    image.save(file_path)

    if _current_message and _current_loop:
      print("Discord context found! Sending image...")
      file = discord.File(file_path, filename="image.png")
      asyncio.run_coroutine_threadsafe(
          _current_message.channel.send(file=file), _current_loop
      )
      return "Image generated and sent successfully."
    else:
      print("ERROR: Failed to locate Discord message context.")
      return "Image generated, but failed to locate Discord context."

  except Exception as e:
    print(f"Image generation error: {str(e)}")
    return f"Failed to generate image via Hugging Face: {str(e)}"
  
@tool
def surfInternet(query: str):
    """Use this tool to surf internet and get latest information"""
    result = tavily_client.search(query = query)
    return str(result)

# OpenRouter Free Tier Model Setup
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),

)

agent = create_agent(
    model = model, 
    tools = [surfInternet, generateImage], 
    system_prompt = """You have tools to surf the internet and generate images. When a user asks for an image, you MUST call the generateImage tool."""
)