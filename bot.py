import discord
import os
from threading import Thread
from flask import Flask
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
agent = create_agent(model=model, tools=[])

# --- Tiny web server to keep Render Free Tier alive ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active!"

def run_web():
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
# -----------------------------------------------------

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    content = message.content
    response = agent.invoke({"messages": [HumanMessage(content=content)]})
    agent_message = response["messages"][-1].content

    if isinstance(agent_message, list):
        text_to_send = agent_message[0].get('text', str(agent_message))
    elif isinstance(agent_message, dict):
        text_to_send = agent_message.get('text', str(agent_message))
    else:
        text_to_send = str(agent_message)

    await message.channel.send(text_to_send)

if __name__ == "__main__":
    # Start web server in background thread
    web_thread = Thread(target=run_web)
    web_thread.start()
    
    # Start Discord bot
    client.run(os.getenv("DISCORD_API_KEY"))