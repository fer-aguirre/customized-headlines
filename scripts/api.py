from fastapi import FastAPI

app = FastAPI()

@app.post("/") 
async def lower_case(string: str):
    return {"response": string.lower()}


"""
import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'string': 'HELLO WORLD',
}

response = requests.post('http://127.0.0.1:8000/', headers=headers, json=json_data)
"""