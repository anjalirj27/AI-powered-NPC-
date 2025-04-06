# 🧠 AI NPC Terminal – Project Overview

## 🎮 What's This All About?

**AI NPC Terminal** is a voice-enabled, multilingual roleplaying assistant where you can **talk to AI-powered characters** — just like NPCs in your favorite RPGs!

Whether you're seeking advice from a **Wise Wizard**, decoding tech-talk with a **Cyborg Hacker**, or enjoying tales from a **Village Elder**, this tool brings fictional characters to life using the latest AI + speech technologies.

It supports:

- 🎙️ Real-time **voice input**
- 🔊 Spoken **voice output**
- 🌐 **Multiple languages** (English, Hindi, Bengali)
- 🖥️ Web UI via **Streamlit** or terminal-based CLI mode

---

## 🌟 Key Highlights

- ✅ **Multilingual Conversations**
- ✅ **Voice Input & Output**
- ✅ **Character-Based Roleplay**
- ✅ **Streamlit Web App + CLI Support**
- ✅ **Fast & Fun AI Responses**

---

## 🧠 Tech Stack

| Feature              | Tool / Library |
|----------------------|----------------|
| **LLM Backend**      | Groq's `gemma-2-9b-it` |
| **Speech-to-Text**   | [OpenAI Whisper](https://github.com/openai/whisper) |
| **Text-to-Speech**   | [gTTS (Google TTS)](https://pypi.org/project/gTTS/) |
| **Voice Playback**   | `pygame` |
| **Web UI**           | [Streamlit](https://streamlit.io) |
| **Language Support** | Manual prompt formatting for EN, HI, BN |

---

## 🚀 How It Works (Simplified Flow)

1. 🧙 Choose an NPC and preferred language via UI  
2. 🎤 Speak or type your message  
3. 🧠 Whisper transcribes your voice (if used)  
4. ⚡ Message is sent to Groq’s LLM for a response  
5. 🗣️ Response is converted to speech using gTTS  
6. 🔊 Voice is played back using `pygame` — the NPC talks!

---






