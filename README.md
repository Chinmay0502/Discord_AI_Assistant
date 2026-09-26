# 🤖 DiscordAI — LLM-Powered Discord Assistant

**DiscordAI** is a smart, full-stack Discord bot powered by LangChain and Google's Gemini LLM, designed to bring intelligent conversational capabilities, custom context handling, and real-time AI assistance directly into your Discord servers.

The project integrates a **Discord Bot Client (`discord.py`)**, a **LangChain agent pipeline**, **Google Gemini (`gemini-1.5-flash`)**, and a lightweight **Flask background web server** to ensure 24/7 cloud uptime and reliable chat responses.

---

## 🌟 Overview

Modern communities require automated, context-aware assistance to handle engagement, answer technical questions, and interact smoothly with members.

**DiscordAI** solves this by listening to server messages, piping them through a custom-configured LangChain agent running on Google Gemini, and streaming clean text replies back to your Discord channels.

The application is built using a modern Python and cloud deployment architecture:

* 🤖 **Bot Framework:** Python `discord.py`
* 🧠 **LLM Engine:** Google Gemini via `langchain-google-genai`
* 🛠️ **Orchestration:** LangChain Agents & Message Core
* 🌐 **Keep-Alive Server:** Flask (Python micro web framework)
* ⚙️ **Runtime Environment:** Python 3.x
* ☁️ **Cloud Hosting:** Render (Web Service + UptimeRobot integration)

---

## ✨ Key Features

* 💬 Real-time Discord server message handling
* 🧠 Powered by Google Gemini (`gemini-1.5-flash`)
* 🔗 LangChain agent framework integration
* 🧹 Clean plain-text response extraction (filters raw LLM payload structures)
* ⚡ Robust intent configuration (`message_content` intent enabled)
* 🌐 Built-in Flask web server for zero-downtime cloud hosting
* 🛡️ Secure configuration via environment variables (`python-dotenv`)
* 🚀 Easy local development and cloud deployment configuration
* 🔄 Automated 24/7 uptime support using external ping services

---

# 🏗️ System Architecture

The project manages concurrent processes for real-time Discord WebSocket communication and background health checks.

```text
                    ┌──────────────────────┐
                    │    Discord Server    │
                    └──────────┬───────────┘
                               │
                               ▼ WebSocket (discord.py)
                    ┌──────────────────────┐
                    │ Python Bot Script    │
                    │ (Discord Client)     │
                    └───────┬───────┬──────┘
                            │       │
              AI Prompt     │       │ Background Thread
                            │       │
                            ▼       ▼
                ┌───────────────┐   ┌──────────────────┐
                │ LangChain &   │   │ Flask Web Server │
                │ Google Gemini │   │ (Port 10000)     │
                └───────────────┘   └────────┬─────────┘
                                             │ HTTP Ping Request
                                             ▼
                            ┌─────────────────────────────────┐
                            │ UptimeRobot (Keep-Alive Service)│
                            └─────────────────────────────────┘

🔄 How It Works
The DiscordAI message-processing workflow operates through these core steps:

Step 1 — Message Event Trigger
A user sends a message in a text channel where the bot has permissions.

Step 2 — Filtering & Validation
The on_message event listener filters out messages originating from the bot itself to prevent infinite chat loops.

Step 3 — Agent Invocation
The message content is wrapped inside a HumanMessage object and passed directly to the LangChain agent.

Step 4 — LLM Processing
The agent queries the Google Gemini model (gemini-1.5-flash) with the context and generates a response object.

Step 5 — Text Extraction
The system parses the multi-layered response payload to extract strictly the plain text string data.

Step 6 — Response Delivery
The bot pushes the clean text string back through the active Discord message channel using await message.channel.send().

🛠️ Technology Stack
Core Language & API
Python: Core runtime environment for executing script logic.

discord.py: Wrapper API for connecting to Discord's gateway over WebSockets.

Artificial Intelligence & Orchestration
Google Gemini (gemini-1.5-flash): High-speed LLM processing requests.

LangChain: Agent creation framework and workflow orchestration.

LangChain Google GenAI: Official provider package bridging LangChain with Google generative models.

Infrastructure & Uptime
Flask: Lightweight micro web framework to bind a local port for cloud uptime tracking.

Render: Cloud application hosting platform.

UptimeRobot: Automated HTTP monitor preventing free-tier container sleep cycles.

📁 Project Structure
Plaintext
DiscordAI/
│
├── bot.py                  # Main application script (Discord client + Flask web server)
├── requirements.txt        # Python package dependency manifest
├── .env                    # Local environment variables (API keys & tokens)
└── README.md               # Project documentation
🚀 Getting Started
Follow these instructions to run and deploy DiscordAI locally or in the cloud.

Prerequisites
Ensure you have the following installed on your system:

Python 3.x

pip

Git

A Discord Developer Account & Bot Token

A Google Generative AI API Key

📥 Clone the Repository
Bash
git clone [https://github.com/your-username/DiscordAI.git](https://github.com/your-username/DiscordAI.git)
cd DiscordAI
🐍 Local Environment Setup
Create and activate a Python virtual environment:

Bash
python -m venv venv
Activate Virtual Environment
Windows:

Bash
venv\Scripts\activate
macOS / Linux:

Bash
source venv/bin/activate
📦 Install Dependencies
Install the required packages using pip:

Bash
pip install -r requirements.txt
(Ensure your requirements.txt includes discord.py, python-dotenv, langchain, langchain-google-genai, and flask)

⚙️ Configuration
Create a .env file in your root project folder and supply your secret tokens:

Code snippet
DISCORD_API_KEY=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
PORT=10000
⚠️ Security Note: Never commit your .env file to version control repositories.

💻 Running Locally
Start your application locally:

Bash
python bot.py
The script will launch the Flask keep-alive server on port 10000 while initiating the asynchronous Discord WebSocket client connection.

☁️ Cloud Deployment Guide (Render Free Tier)
To keep your bot online 24/7 using Render's free tier:

Push your project files (bot.py, requirements.txt) to a public or private GitHub repository.

Log into the Render Dashboard and click New + -> Web Service.

Connect your GitHub repository.

Configure your deployment parameters:

Name: discord-ai-bot

Runtime: Python 3

Build Command: pip install -r requirements.txt

Start Command: python bot.py

Instance Type: Free

Navigate to the Environment section and add your keys:

DISCORD_API_KEY = your_discord_token

GOOGLE_API_KEY = your_gemini_key

Click Create Web Service.

Copy your public Render URL (https://your-bot-name.onrender.com), create a free account on UptimeRobot, and point an HTTP monitor to ping it every 5 minutes to prevent sleep timeouts.

📝 Code Implementation Reference (bot.py)
Python
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

# --- Flask Keep-Alive Server ---
app = Flask(__name__)

@app.route('/')
def home():
    return "DiscordAI Bot is active!"

def run_web():
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
# -------------------------------

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

if __name__ == "__main__":
    web_thread = Thread(target=run_web)
    web_thread.start()
    
    client.run(os.getenv("DISCORD_API_KEY"))
🔐 Environment Variables Summary
Variable Name	Description	Required
DISCORD_API_KEY	Authentication token generated in the Discord Developer Portal	Yes
GOOGLE_API_KEY	API key provisioned for Google Generative AI models	Yes
PORT	Local network binding port used by the Flask server (Default: 10000)	No
🛡️ Security Best Practices
Token Protection: Never expose your bot token or API credentials inside public files, issues, or commit histories.

Intents Scoping: Only enable necessary gateway intents (message_content) required for core bot tasks.

Ignore Self-Triggers: Always verify if message.author == client.user: to prevent catastrophic recursive messaging loops inside channels.

🤝 Contributing
Contributions, feature requests, and bug reports are welcome! Feel free to fork the repository and submit pull requests.

📜 License
Distributed under the terms of the project's repository license.

⭐ Support
If you found DiscordAI helpful or interesting, please consider giving the repository a ⭐ on GitHub!
