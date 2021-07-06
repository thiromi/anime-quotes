# API endpoint: https://animechan.vercel.app/api/random
# FIRST GOAL: Get a random quote

import requests

def get_quote(base_url: str, endpoint: str, parameters: str) -> str:
    return requests.get(base_url).json()['quote']
