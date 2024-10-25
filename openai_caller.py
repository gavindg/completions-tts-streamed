from dotenv import load_dotenv
from os import getenv
import requests
import json
import time

# top secret
load_dotenv()
# openai
OPENAI_SECRET = getenv('OPENAI_SECRET')
OPENAI_HEADERS = {
        "Authorization": f"Bearer {OPENAI_SECRET}",
        }
OPENAI_URL = 'https://api.openai.com/v1/chat/completions'
# misc
DEFAULT_MAX_TOKENS = 100


def cc_request(context_history: dict, max_tokens=DEFAULT_MAX_TOKENS):
    data = {
            "model": "gpt-4o-mini",
            "messages": context_history,
            "max_tokens": DEFAULT_MAX_TOKENS,
            "temperature": 0.5,
            }

    start = time.process_time()
    print("[CC] request sent ... ", end='', flush=True)
    resp = requests.post(OPENAI_URL, headers=OPENAI_HEADERS, json=data)
    end = time.process_time()
    print(f"done in {(end - start) * 1000} ms ", end='', flush=True)

    if not resp.ok:
        print("woah")
        raise

    resp_json = json.loads(str(resp.content, encoding='utf-8'))
    resp_text = resp_json["choices"][0]["message"]["content"]
    cc_tokens = resp_json['usage']['completion_tokens']
    print(f'and {cc_tokens} tokens.')
    print()
    return resp_text     # print(json.dumps(jsond, indent=4))


def whisper_request(prompt):
    # TODO: implement the whisper version as well
    pass
