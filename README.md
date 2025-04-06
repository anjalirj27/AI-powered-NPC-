🧠 Project Overview: AI NPC Terminal
🎮 What's This All About?
AI NPC Terminal is a fun, interactive tool where users can roleplay with AI-powered characters, much like talking to Non-Player Characters (NPCs) in video games. But here’s the twist — it supports real-time voice input, voice output, multiple languages, and works both in the browser and command line.

Whether you want to get advice from a Wise Wizard, chat with a Cyborg Hacker, or hear stories from a Village Elder, this app makes it all possible — powered by cutting-edge AI and speech tools.

🌟 Key Highlights
Multilingual: Chat in English, Hindi, or Bengali.

Voice-enabled: Speak your message instead of typing.

Voice response: NPCs talk back with generated speech!

Character-driven: Each NPC has a unique tone and personality.

Web + CLI: Accessible via a slick Streamlit UI or the command-line.

🧠 Tech Stack
Component	Tool/Library Used
LLM Backend	Groq's blazing-fast gemma-2-9b-it
Speech-to-Text	OpenAI Whisper
Text-to-Speech	gTTS (Google TTS)
UI (Web)	Streamlit
Voice Playback	pygame (for playing back generated speech)
Language Support	Manual prompts + multilingual TTS/STT
🧪 Use Cases
RPG or game development demos

Showcasing voice+AI integration

Language learning through conversation

Personal entertainment or portfolio projects

📦 Project Components
File	Purpose
app.py	Main Streamlit interface for web-based interaction
model.py	Simple CLI tool for keyboard-based conversations
.env	Stores your Groq API key (not committed)
requirements.txt	Lists all dependencies to install the app
README.md	You're reading it — complete project guide
🚀 How It Works (Simplified Flow)
User chooses NPC and language via the UI

User speaks or types a message

The app uses Whisper to transcribe voice (if used)

The message is sent to Groq's LLM, which replies in character

The reply is converted to speech using gTTS

pygame plays the voice — the NPC talks!











