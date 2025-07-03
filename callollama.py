import requests
import json


def callOLLAMA(user_message):
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "phi3",           # Change model name as needed (e.g., llama3, mistral, etc.)
            "prompt": user_message,
            "stream": False
        }

        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            bot_response = result.get("response", "Sorry, I am unable to help you.")
            return bot_response.strip()
            
    except Exception as e:
        return f"Exception occurred: {str(e)}"