# 🤖 DiscordAI — LLM-Powered Discord Assistant

**DiscordAI** is a smart, full-stack Discord bot powered by LangChain and Google's Gemini LLM, designed to bring intelligent conversational capabilities, custom context handling, and real-time AI assistance directly into your Discord servers.

The project integrates a **Discord Bot Client (`discord.py`)**, a **LangChain agent pipeline**, **Google Gemini (`gemini-1.5-flash`)**, and a lightweight **Flask background web server** for cloud deployment and health monitoring.

---

# 🌟 Overview

Modern communities require automated, context-aware assistance to handle engagement, answer technical questions, and interact smoothly with members.

**DiscordAI** listens to server messages, processes them through a LangChain agent running on Google Gemini, and sends clean AI-generated responses back to Discord channels.

The application is built using:

* 🤖 **Bot Framework:** Python `discord.py`
* 🧠 **LLM Engine:** Google Gemini via `langchain-google-genai`
* 🛠️ **Orchestration:** LangChain Agents & Message Core
* 🌐 **Web Server:** Flask
* ⚙️ **Runtime:** Python 3.x
* ☁️ **Cloud Hosting:** Render

---

# ✨ Key Features

* 💬 Real-time Discord server message handling
* 🧠 Powered by Google Gemini (`gemini-1.5-flash`)
* 🔗 LangChain agent framework integration
* 🧹 Plain-text response extraction from LLM responses
* ⚡ Discord `message_content` intent support
* 🌐 Built-in Flask web server
* 🛡️ Environment-variable based secret management
* 🚀 Local and cloud deployment support
* 🔄 HTTP health monitoring support

---

# 🏗️ System Architecture

```text
                     ┌──────────────────────┐
                     │    Discord Server    │
                     └──────────┬───────────┘
                                │
                                │ WebSocket
                                │ discord.py
                                ▼
                     ┌──────────────────────┐
                     │   Python Bot Script  │
                     │    Discord Client    │
                     └───────┬───────┬──────┘
                             │       │
                    AI Prompt│       │Background Thread
                             │       │
                             ▼       ▼
                  ┌────────────────┐  ┌──────────────────┐
                  │ LangChain +    │  │ Flask Web Server │
                  │ Google Gemini  │  │                  │
                  └────────────────┘  └────────┬─────────┘
                                               │
                                               │ HTTP
                                               ▼
                                      ┌──────────────────┐
                                      │ Uptime Monitoring │
                                      └──────────────────┘
```

---

# 🔄 How It Works

The DiscordAI message-processing workflow operates through these core steps:

### Step 1 — Message Event Trigger

A user sends a message in a text channel where the bot has permission to read and send messages.

### Step 2 — Filtering & Validation

The `on_message` event listener checks whether the message was sent by the bot itself. This prevents the bot from responding to its own messages and creating an infinite loop.

### Step 3 — Agent Invocation

The user's message content is wrapped inside a `HumanMessage` object and passed to the LangChain agent.

### Step 4 — LLM Processing

The LangChain agent sends the request to the Google Gemini model (`gemini-1.5-flash`) and generates an AI response.

### Step 5 — Text Extraction

The application processes the agent response and extracts the plain text from the returned response payload.

### Step 6 — Response Delivery

The extracted text is sent back to the Discord channel using:

```python
await message.channel.send(text_to_send)
```

---

# 🛠️ Technology Stack

## Core Language & API

* **Python** — Core programming language.
* **discord.py** — Python API wrapper for interacting with Discord.
* **Flask** — Lightweight web framework used to expose a web endpoint.

## Artificial Intelligence

* **Google Gemini** — Large language model used to generate responses.
* **LangChain** — Framework used for AI agent orchestration.
* **LangChain Google GenAI** — Integration between LangChain and Google Gemini.

## Deployment & Infrastructure

* **GitHub** — Source-code hosting and version control.
* **Render** — Cloud hosting platform.
* **UptimeRobot** — Optional HTTP monitoring service.

---

# 📁 Project Structure

```text
DiscordAI/
│
├── bot.py                  # Main Discord bot + Flask server
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignored files
├── .env.example            # Example environment variables
├── README.md               # Project documentation
│
├── .env                    # Local secrets - NOT uploaded
└── venv/                   # Local virtual environment - NOT uploaded
```

> `.env` and `venv/` are intentionally excluded from Git using `.gitignore`.

---

# 🚀 Getting Started

Follow these instructions to run DiscordAI locally or deploy it to the cloud.

## Prerequisites

Make sure you have:

* Python 3.x
* pip
* Git
* A Discord Developer account
* A Discord Bot
* A Discord Bot Token
* A Google Generative AI API Key

---

# 📥 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/DiscordAI.git
cd DiscordAI
```

Replace `YOUR_USERNAME` with your GitHub username.

---

# 🐍 Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

The `venv/` directory is local and should **not** be uploaded to GitHub.

### Windows

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```text
discord.py
python-dotenv
langchain
langchain-google-genai
flask
```

---

# ⚙️ Configuration

Create a `.env` file in the root directory:

```env
DISCORD_API_KEY=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
PORT=10000
```

---

# 🔑 Environment Variables

| Variable          | Description           | Required |
| ----------------- | --------------------- | -------- |
| `DISCORD_API_KEY` | Discord Bot Token     | Yes      |
| `GOOGLE_API_KEY`  | Google Gemini API Key | Yes      |
| `PORT`            | Flask server port     | No       |

If `PORT` is not specified, the application uses:

```text
10000
```

---

# 🔐 Environment Security

**Never upload your `.env` file to GitHub.**

Create a `.gitignore` file in the root of your project with:

```gitignore
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
```

This prevents:

* `.env` from being uploaded
* `venv/` from being uploaded
* Python cache files from being uploaded
* IDE configuration files from being uploaded

---

# 📄 .env.example

Create a `.env.example` file that can safely be committed to GitHub:

```env
DISCORD_API_KEY=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
PORT=10000
```

The `.env.example` file should contain **placeholders only**.

Never put your real Discord token or Google API key inside it.

---

# 💻 Running Locally

After activating your virtual environment and creating `.env`, run:

```bash
python bot.py
```

The application will:

1. Start the Flask web server.
2. Start the Discord client.
3. Connect to Discord using the bot token.
4. Listen for incoming messages.
5. Send messages to the Gemini-powered LangChain agent.
6. Return the generated response to the Discord channel.

---

# 🤖 Discord Bot Configuration

After creating your Discord application and bot through the Discord Developer Portal, make sure the required intents are enabled.

The bot requires the **Message Content Intent** because it needs access to the text content of Discord messages.

The code enables it with:

```python
intents = discord.Intents.default()
intents.message_content = True
```

Make sure the bot has appropriate permissions, including:

* View Channels
* Send Messages
* Read Message History

---

# ☁️ Cloud Deployment with Render

DiscordAI can be deployed as a web service on Render.

## 1. Push the Project to GitHub

Your GitHub repository should contain:

```text
bot.py
requirements.txt
.gitignore
.env.example
README.md
```

Do **not** upload:

```text
.env
venv/
```

---

## 2. Create a Render Web Service

Create a new Web Service in Render and connect your GitHub repository.

Configure:

| Setting       | Value                             |
| ------------- | --------------------------------- |
| Runtime       | Python 3                          |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python bot.py`                   |

---

## 3. Add Environment Variables

In the Render environment-variable settings, add:

```text
DISCORD_API_KEY
GOOGLE_API_KEY
PORT
```

Example:

```text
DISCORD_API_KEY = your_discord_bot_token
GOOGLE_API_KEY = your_google_api_key
PORT = 10000
```

Keep your real credentials inside Render's environment settings rather than putting them in your repository.

---

# 🌐 Flask Web Server

The application includes a small Flask server:

```python
@app.route("/")
def home():
    return "DiscordAI Bot is active!"
```

The Flask server reads the port from the environment:

```python
port = int(os.getenv("PORT", 10000))
```

This provides an HTTP endpoint that can be used for application health monitoring.

---

# ⏱️ Uptime Monitoring

You can use an external HTTP monitoring service such as **UptimeRobot** to monitor your deployed application.

After deployment, use your Render service URL as the monitoring target:

```text
https://your-bot-name.onrender.com
```

The root endpoint returns:

```text
DiscordAI Bot is active!
```

> Hosting providers can change their free-tier policies and sleep behavior. Check the current Render documentation for the latest limitations.

---

# 📝 Code Implementation

The main application is contained in `bot.py`.

```python
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
```

---

# 📦 Requirements

Create a `requirements.txt` file containing:

```text
discord.py
python-dotenv
langchain
langchain-google-genai
flask
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables Summary

| Variable          | Purpose                       | Required |
| ----------------- | ----------------------------- | -------- |
| `DISCORD_API_KEY` | Authenticates the Discord bot | Yes      |
| `GOOGLE_API_KEY`  | Authenticates Google Gemini   | Yes      |
| `PORT`            | Flask server port             | No       |

---

# 🛡️ Security Best Practices

## Never Commit Secrets

Do not commit:

```text
.env
```

Do not place API keys directly inside:

```text
bot.py
README.md
requirements.txt
```

Use environment variables instead.

Load environment variables with:

```python
load_dotenv()
```

Access them using:

```python
os.getenv("DISCORD_API_KEY")
```

and:

```python
os.getenv("GOOGLE_API_KEY")
```

## Protect Your Discord Token

Your Discord bot token should be treated like a password.

If your token is accidentally exposed publicly, regenerate it through the Discord Developer Portal.

---

# 🔄 Git Workflow

Check your changes:

```bash
git status
```

Add your files:

```bash
git add .
```

Commit:

```bash
git commit -m "Update DiscordAI"
```

Push to GitHub:

```bash
git push
```

Because `.env` and `venv/` are included in `.gitignore`, they will not be included in the commit.

You can verify this before committing with:

```bash
git status
```

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

# 📜 License

Distributed under the terms of the project's repository license.

---

# ⭐ Support

If you found **DiscordAI** useful, consider giving the repository a ⭐ on GitHub.

---

# 📌 Important Files

| File / Directory   | Upload to GitHub? |
| ------------------ | ----------------- |
| `bot.py`           | ✅ Yes             |
| `requirements.txt` | ✅ Yes             |
| `README.md`        | ✅ Yes             |
| `.gitignore`       | ✅ Yes             |
| `.env.example`     | ✅ Yes             |
| `.env`             | ❌ No              |
| `venv/`            | ❌ No              |
| `.venv/`           | ❌ No              |
| `__pycache__/`     | ❌ No              |
