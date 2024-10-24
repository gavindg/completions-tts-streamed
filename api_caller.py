from dotenv import load_dotenv
from os import getenv
import requests
import json

# top secret
load_dotenv()
OPENAI_SECRET = getenv('OPENAI_SECRET')
OPENAI_HEADERS = {
        "Authorization": f"Bearer {OPENAI_SECRET}"
        }
OPENAI_URL = 'https://api.openai.com/v1/chat/completions'


def call_openai(context_history: dict):
    # todo: make this not suck
    data = {
            "model": "gpt-4o-mini",
            "messages": context_history,
            "max_tokens": 10,
            "temperature": 0.5,
            }
    resp = requests.post(OPENAI_URL, headers=OPENAI_HEADERS, json=data)
    if not resp.ok:
        print("woah")
        raise
    jsond = json.loads(str(resp.content, encoding='utf-8'))
    print(json.dumps(jsond, indent=4))
