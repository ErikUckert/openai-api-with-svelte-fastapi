from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ['OPENAIAPIKEY']

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Chat(BaseModel):
    question: str
    clearChat: bool

def initMessages():
    return [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
messages = initMessages()

@app.post("/chat/")
async def create_chat(chat: Chat):
    if chat.clearChat:
        print(chat.clearChat)
        global messages 
        messages = initMessages()
    if chat.question: 
        messages.append({"role": "user", "content": chat.question})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
            )
        messages.append({"role": "assistant", "content": res.choices[0].message.content})
    print(messages)
    return messages