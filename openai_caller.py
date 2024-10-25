from dotenv import load_dotenv
from os import getenv
import requests
import json

# top secret
load_dotenv()
# openai
OPENAI_SECRET = getenv('OPENAI_SECRET')
OPENAI_HEADERS = {
        "Authorization": f"Bearer {OPENAI_SECRET}",
        }
OPENAI_URL = 'https://api.openai.com/v1/chat/completions'
# misc
DEFAULT_MAX_TOKENS = 1000


def cc_request(context_history: dict, max_tokens=DEFAULT_MAX_TOKENS):
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
    resp_json = json.loads(str(resp.content, encoding='utf-8'))
    resp_text = resp_json["choices"][0]["message"]["content"]
    print(resp_text)
    return resp_text     # print(json.dumps(jsond, indent=4))
