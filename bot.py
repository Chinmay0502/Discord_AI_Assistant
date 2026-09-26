import discord
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')
agent = create_agent(model=model, tools=[])

@client.event
async def on_ready():
    print(f'Logged in successfully as {client.user} (ID: {client.user.id})')
    print('Bot is ready and connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    content = message.content
    response = agent.invoke({"messages": [HumanMessage(content=content)]})
    agent_message = response["messages"][-1].content

    # Clean payload text extraction parser
    if isinstance(agent_message, list):
        text_to_send = agent_message[0].get('text', str(agent_message))
    elif isinstance(agent_message, dict):
        text_to_send = agent_message.get('text', str(agent_message))
    else:
        text_to_send = str(agent_message)

    await message.channel.send(text_to_send)

client.run(os.getenv("DISCORD_API_KEY"))