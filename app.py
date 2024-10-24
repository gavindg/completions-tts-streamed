"""
idea: stream text out of 11labs, test the speed difference
"""

from api_caller import call_openai

call_openai([{"role": "user", "content": "Say 'this is a test'"}])
