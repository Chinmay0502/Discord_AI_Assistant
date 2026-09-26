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

A user sends a message in a text channel where the bot has permission to read and send messages.

Step 2 — Filtering & Validation

The on_message event listener checks whether the message was sent by the bot itself. This prevents the bot from responding to its own messages and creating an infinite loop.

Step 3 — Agent Invocation

The user's message content is wrapped inside a HumanMessage object and passed to the LangChain agent.

Step 4 — LLM Processing

The LangChain agent sends the request to the Google Gemini model (gemini-1.5-flash) and generates an AI response.

Step 5 — Text Extraction

The application processes the agent response and extracts the plain text from the returned response payload.

Step 6 — Response Delivery

The extracted text is sent back to the Discord channel using:

await message.channel.send(text_to_send)
🛠️ Technology Stack
Core Language & API
Python — Core programming language.
discord.py — Python API wrapper for interacting with Discord.
Flask — Lightweight web framework used to expose a web endpoint.
Artificial Intelligence
Google Gemini — Large language model used to generate responses.
LangChain — Framework used for AI agent orchestration.
LangChain Google GenAI — Integration between LangChain and Google Gemini.
Deployment & Infrastructure
GitHub — Source-code hosting and version control.
Render — Cloud hosting platform for deploying the application.
UptimeRobot — HTTP monitoring service.
📁 Project Structure
DiscordAI/
│
├── bot.py                  # Main Discord bot + Flask server
├── requirements.txt        # Python dependencies
├── .gitignore              # Files ignored by Git
├── .env                    # Local environment variables (NOT uploaded)
├── .env.example            # Example environment variables
└── README.md               # Project documentation

Note: venv/ is also created locally but is excluded from Git using .gitignore.

🚀 Getting Started

Follow these instructions to run DiscordAI locally or deploy it to the cloud.

Prerequisites

Make sure you have the following installed:

Python 3.x
pip
Git
A Discord Developer account
A Discord Bot
A Discord Bot Token
A Google Generative AI API Key
📥 Clone the Repository

Clone the repository using:

git clone https://github.com/YOUR_USERNAME/DiscordAI.git
cd DiscordAI

Replace YOUR_USERNAME with your GitHub username.

🐍 Create a Virtual Environment

Create a Python virtual environment:

python -m venv venv

The venv/ directory is intentionally not uploaded to GitHub.

Activate the environment:

Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
📦 Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

Your requirements.txt should contain the required dependencies, including:

discord.py
python-dotenv
langchain
langchain-google-genai
flask
⚙️ Configuration

Create a .env file in the root of the project:

DISCORD_API_KEY=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
PORT=10000
Environment Variables
Variable	Description	Required
DISCORD_API_KEY	Discord Bot Token	Yes
GOOGLE_API_KEY	Google Gemini API Key	Yes
PORT	Port used by Flask	No

If PORT is not provided, the application defaults to:

10000
🔐 Environment Security

Never upload your .env file to GitHub.

Your .gitignore should contain:

# Environment variables
.env
.env.*
!.env.example

# Virtual environments
venv/
.venv/
env/

# Python cache
__pycache__/
*.py[cod]

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

This ensures that sensitive credentials and your local virtual environment are not committed to Git.

📄 .env.example

You can create a safe example file that can be committed to GitHub:

DISCORD_API_KEY=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
PORT=10000

The .env.example file contains placeholders only and should never contain your real API keys or Discord token.

💻 Running Locally

After activating your virtual environment and configuring .env, start the bot:

python bot.py

The application will:

Start the Flask web server.
Start the Discord client.
Connect to Discord using the bot token.
Listen for incoming messages.
Send messages to the Gemini-powered LangChain agent.
Return the generated response to the Discord channel.
🤖 Discord Bot Configuration

After creating your Discord application and bot through the Discord Developer Portal, make sure the required intents are enabled.

The bot requires the Message Content Intent because it needs access to the text content of Discord messages.

The code enables it with:

intents = discord.Intents.default()
intents.message_content = True

You should also make sure the bot has the required permissions in your Discord server, such as:

View Channels
Send Messages
Read Message History
☁️ Cloud Deployment with Render

DiscordAI can be deployed as a web service on Render.

1. Push the Project to GitHub

Make sure your repository contains:

bot.py
requirements.txt
.gitignore
.env.example
README.md

Do not upload:

.env
venv/
2. Create a Render Web Service

Go to the Render dashboard and create a new Web Service.

Connect your GitHub repository.

Configure the service with:

Setting	Value
Runtime	Python 3
Build Command	pip install -r requirements.txt
Start Command	python bot.py
3. Add Environment Variables

In Render, open the Environment Variables section and add:

DISCORD_API_KEY
GOOGLE_API_KEY
PORT

For example:

DISCORD_API_KEY = your_discord_bot_token
GOOGLE_API_KEY = your_google_api_key
PORT = 10000

Do not put your actual keys inside bot.py or README.md.

🌐 Flask Keep-Alive Server

The project includes a small Flask server:

@app.route('/')
def home():
    return "DiscordAI Bot is active!"

The server listens on the port provided by the PORT environment variable:

port = int(os.getenv("PORT", 10000))

This allows the application to expose an HTTP endpoint when deployed as a web service.

⏱️ Uptime Monitoring

You can use an external HTTP monitoring service such as UptimeRobot to monitor the deployed application.

After deploying the application, use your Render service URL as the monitoring target.

For example:

https://your-bot-name.onrender.com

The Flask / endpoint returns:

DiscordAI Bot is active!

Availability and sleep behavior depend on the hosting provider's current free-tier policies. Check the provider's documentation for the latest limitations.

📝 Code Implementation

The main application is contained in bot.py.

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

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

agent = create_agent(
    model=model,
    tools=[]
)

# -----------------------------
# Flask Web Server
# -----------------------------

app = Flask(__name__)


@app.route("/")
def home():
    return "DiscordAI Bot is active!"


def run_web():
    port = int(os.getenv("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port
    )


# -----------------------------
# Discord Message Handler
# -----------------------------

@client.event
async def on_message(message):

    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    content = message.content

    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content=content)
            ]
        }
    )

    agent_message = response["messages"][-1].content

    # Extract plain text from the response
    if isinstance(agent_message, list):

        text_to_send = agent_message[0].get(
            "text",
            str(agent_message)
        )

    elif isinstance(agent_message, dict):

        text_to_send = agent_message.get(
            "text",
            str(agent_message)
        )

    else:

        text_to_send = str(agent_message)

    await message.channel.send(text_to_send)


# -----------------------------
# Application Entry Point
# -----------------------------

if __name__ == "__main__":

    web_thread = Thread(
        target=run_web
    )

    web_thread.start()

    client.run(
        os.getenv("DISCORD_API_KEY")
    )
📦 Requirements

A basic requirements.txt can contain:

discord.py
python-dotenv
langchain
langchain-google-genai
flask

Install them with:

pip install -r requirements.txt
🔑 Environment Variables Summary
Variable	Purpose	Required
DISCORD_API_KEY	Authenticates the Discord bot	Yes
GOOGLE_API_KEY	Authenticates Google Gemini	Yes
PORT	Flask server port	No
🛡️ Security Best Practices
Never commit secrets

Do not commit:

.env

Do not place API keys directly inside:

bot.py
README.md
requirements.txt
Use environment variables

Load credentials using:

load_dotenv()

Then access them using:

os.getenv("DISCORD_API_KEY")

and:

os.getenv("GOOGLE_API_KEY")
Protect your Discord token

Your Discord bot token should be treated like a password.

If a token is accidentally exposed publicly, regenerate it through the Discord Developer Portal.

🔄 Git Workflow

After making changes to your project:

git status

Add your changes:

git add .

Commit them:

git commit -m "Update DiscordAI"

Push them to GitHub:

git push

Because .env and venv/ are included in .gitignore, they will not be included in the commit.

🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

To contribute:

Fork the repository.
Create a new branch.
Make your changes.
Commit your changes.
Push the branch.
Open a Pull Request.

Example:

git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
📜 License

Distributed under the terms of the project's repository license.

⭐ Support

If you found DiscordAI useful, consider giving the repository a ⭐ on GitHub.

📌 Important Files
File	Upload to GitHub?
bot.py	✅ Yes
requirements.txt	✅ Yes
README.md	✅ Yes
.gitignore	✅ Yes
.env.example	✅ Yes
.env	❌ No
venv/	❌ No
__pycache__/	❌ No
