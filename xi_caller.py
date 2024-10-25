"""
based on 11labs api reference examples
"""

import requests
from os import getenv, mkdir, path
import dotenv
from pathlib import Path
import time

dotenv.load_dotenv()

if not path.exists(Path(__file__).parent / 'out'):
    print("ts not there")
    mkdir("./out/")


# 11labs
VOICE_ID = "nPczCjzI2devNBz1zQrb"   # brian the goat
ELEVENLABS_SECRET = getenv('ELEVENLABS_SECRET')
XI_HEADERS = {
        "Accept": "application/json",
        "xi-api-key": f"{ELEVENLABS_SECRET}",
        }
XI_VOICES_ENDPOINT = 'https://api.elevenlabs.io/v1/voices'
XI_TTS_ENDPOINT = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

# file writing
CHUNK_SIZE = 1024
OUTPUT_PATH = "./out/output.mp3"


def get_voices():
    # make request
    resp = requests.get(XI_VOICES_ENDPOINT, headers=XI_HEADERS)
    # print the response
    data = resp.json()
    for voice in data['voices']:
        print(f"{voice['name']}; {voice['voice_id']}")


def tts_request(prompt: str):
    total_time = 0
    data = {
        "text": prompt,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }

    print("[XI] request sent ... ", end='', flush=True)
    start = time.process_time()
    resp = requests.post(
            XI_TTS_ENDPOINT,
            headers=XI_HEADERS,
            json=data,
            stream=True
            )
    end = time.process_time()
    print(f"done in {(end - start) * 1000} ms.")
    total_time += (end - start) * 1000

    # get outta here with that weird stuff
    if not resp.ok:
        print(resp.content)
        raise

    # stream in
    with open(OUTPUT_PATH, "wb") as f:
        start = time.process_time()
        print("[XI] streaming ... ", end='', flush=True)
        for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
        end = time.process_time()
        print(f"done in {(end - start) * 1000} ms.")
        total_time += (end - start) * 1000
    
    return total_time
