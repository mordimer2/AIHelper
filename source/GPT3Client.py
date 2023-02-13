import requests
import json

class GPT3Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/completions"

    def get_response(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.5,
        }

        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))
        response_json = response.json()
        print(response_json)
        return response_json["choices"][0]["text"]
