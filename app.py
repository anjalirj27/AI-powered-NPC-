import streamlit as st
import os
import time
import torch
import whisper
from deep_translator import GoogleTranslator
from groq import Groq
from gtts import gTTS
import pygame
import tempfile
import threading

# Initialize Whisper model
whisper_model = whisper.load_model("base")

# Initialize Groq Client
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")
groq_client = Groq(api_key=GROQ_API_KEY)

# Initialize pygame mixer
pygame.mixer.init()

# Session states
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("🧠 AI NPC Terminal - Voice & Role")

# Sidebar: Language and Role
language = st.sidebar.selectbox("Language", ["English", "Hindi", "Bengali"])
role = st.sidebar.selectbox("Select NPC Role", ["🧙 Wise Wizard", "🤖 Cyborg Hacker", "👴 Village Elder"])
enable_voice_input = st.sidebar.checkbox("🎤 Use Voice Input", value=False)
enable_voice_output = st.sidebar.checkbox("🔊 Use Voice Output", value=True)

# Role prompts
role_prompts = {
    "🧙 Wise Wizard": "You are a wise wizard. Speak in a mysterious and poetic manner.",
    "🤖 Cyborg Hacker": "You are a futuristic cyborg hacker. Use technical and robotic expressions.",
    "👴 Village Elder": "You are a village elder. Speak with wisdom, warmth, and simplicity."
}
role_prompt = role_prompts[role]

# Helper for language code
lang_map = {"English": "en", "Hindi": "hi", "Bengali": "bn"}
lang_code = lang_map.get(language, "en")

# Voice output function using gTTS + pygame
def speak_text(text):
    def _speak():
        try:
            tts = gTTS(text=text, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                pygame.mixer.music.load(fp.name)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
        except Exception as e:
            st.error(f"Voice Error: {e}")

    threading.Thread(target=_speak).start()

# Transcribe uploaded audio
def transcribe_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        f.flush()
        result = whisper_model.transcribe(f.name)
    return result["text"]

# User input (text or voice)
if enable_voice_input:
    audio_data = st.file_uploader("Upload your voice input (WAV only):", type=["wav"])
    if audio_data is not None:
        user_input = transcribe_audio(audio_data.read())
        st.success(f"You said: {user_input}")
    else:
        user_input = ""
else:
    user_input = st.text_input("💬 Type your message:")

# Main logic
if user_input:
    # Translate to English if needed
    translated_input = (
        GoogleTranslator(source='auto', target='en').translate(user_input)
        if language != "English" else user_input
    )

    # Query Groq
    with st.spinner("🔮 NPC is thinking..."):
        response = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": translated_input}
            ],
            model="gemma2-9b-it"
        )
        output = response.choices[0].message.content.strip()

    # Translate back if needed
    final_output = (
        GoogleTranslator(source='en', target=lang_code).translate(output)
        if language != "English" else output
    )

    # Display response
    st.markdown(f"**{role} says:** {final_output}")

    # Voice Output
    if enable_voice_output:
        speak_text(final_output)

    # Save to chat history
    st.session_state.chat_history.append((user_input, final_output))

# Show chat history
if st.session_state.chat_history:
    st.markdown("### 🗨️ Chat History")
    for i, (q, a) in enumerate(reversed(st.session_state.chat_history)):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**NPC:** {a}")
        st.markdown("---")
