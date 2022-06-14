import requests

def ping_website(_url: str) -> str:
    response = requests.get(_url)
    if response.ok:
        return 'Up'
    else:
        return 'Down'