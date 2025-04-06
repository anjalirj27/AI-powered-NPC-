from pathlib import Path

readme_content = """
# 🧠 AI NPC Terminal

An interactive, multilingual, voice-enabled NPC (Non-Player Character) terminal. Choose a role, speak or type your message, and get immersive, character-based responses — complete with voice output!

Perfect for RPG fans, tech demos, or just a fun way to chat with a wise wizard, a cyborg hacker, or a village elder.

---

## ✨ Features

- 🎙️ Voice input using [Whisper](https://github.com/openai/whisper)
- 🔊 Voice output using [gTTS](https://pypi.org/project/gTTS/) + `pygame`
- 🧙 Roleplay with 3 NPC characters:
  - Wise Wizard
  - Cyborg Hacker
  - Village Elder
- 🌐 Language support for English, Hindi, and Bengali
- 🧠 Powered by Groq's LLMs (`gemma2-9b-it`)
- 🌈 Built with Streamlit for a smooth, browser-based UI

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-npc-terminal.git
cd ai-npc-terminal
2. Set up virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up environment variable
Create a .env file in the root folder and add your Groq API key:

ini
Copy
Edit
GROQ_API_KEY=your-groq-api-key
🚀 Run the App
bash
Copy
Edit
streamlit run app.py
Open the app in your browser, pick a role and language, and start chatting!

🎯 Alternate CLI Mode (Optional)
For a quick terminal-based experience:

bash
Copy
Edit
python model.py
You'll chat directly with the NPC using your keyboard.

📁 Project Structure
bash
Copy
Edit
.
├── app.py         # Main Streamlit app
├── model.py       # CLI version of NPC chat
├── requirements.txt
├── .env           # Your API key lives here (not tracked)
└── README.md
🙌 Acknowledgements
Whisper for speech recognition

gTTS for text-to-speech

Groq API for blazing-fast LLM responses

Streamlit for the interactive UI

🧪 Ideas for the Future
Add more NPC characters and voice styles

Support live microphone input

Store chat history across sessions

Add animations or avatar generation for NPCs

📬 Feedback or Suggestions?
Open an issue or reach out! Always happy to connect. """

Save README to file
readme_path = Path("README.md") readme_path.write_text(readme_content.strip())

print("✅ README.md has been generated successfully.")

markdown
Copy
Edit

Let me know if you want to:
- Add icons, badges, or screenshots
- Auto-create this during `setup.py`
- Include instructions for deployment (e.g., Streamlit Cloud or Render)












