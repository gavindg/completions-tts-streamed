"""
idea: stream text out of 11labs, test the speed difference
"""

from openai_caller import cc_request
from xi_caller import tts_request


def main():
    prompt = input('input a prompt:\n')
    context_history = [{"role": "user", "content": prompt}]
    resp_text = cc_request(context_history)  # , max_tokens=100)
    tts_request(resp_text)


if __name__ == '__main__':
    main()
