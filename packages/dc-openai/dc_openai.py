import requests
import json

def chat_completion(api_key, messages, model="gpt-4o", temperature=1.0, base_url="https://api.openai.com/v1"):
    url = "{}/chat/completions".format(base_url)
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json",
    }
    payload = {"model": model, "messages": messages, "temperature": temperature}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise RuntimeError("API error {}: {}".format(response.status_code, response.text))
    return response.json()
