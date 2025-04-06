import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat_with_npc(role_description):
    print("Type 'exit' to leave the conversation.\n")

    if not API_KEY:
        raise ValueError("GROQ_API_KEY is missing in .env file!")

    messages = [
        {"role": "system", "content": role_description}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma2-9b-it",  # ← updated model
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 512
                    }

            )
            response.raise_for_status()
            data = response.json()

            npc_reply = data['choices'][0]['message']['content']
            print(f"NPC: {npc_reply}\n")

            messages.append({"role": "assistant", "content": npc_reply})

        except Exception as e:
            print("❌ Error from API:", e)
            print("📦 Response:", response.text)
            break


if __name__ == "__main__":
    print("🌲 Welcome to the AI NPC Forest!")

    role = """
    You are a mysterious and wise forest guardian NPC. 
    Speak in an old, cryptic, but helpful manner. 
    Give advice to travelers who ask questions about magic, danger, or treasure.
    """

    chat_with_npc(role)

