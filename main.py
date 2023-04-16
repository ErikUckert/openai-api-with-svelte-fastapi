from typing import Union

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

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Chat(BaseModel):
    question: str

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]

@app.post("/items/")
async def create_item(item: Item):
    item.name = item.name + " the greatest",
    item.price = 1000
    return item

@app.post("/chat/")
async def create_chat(chat: Chat):
    messages.append({"role": "user", "content": chat.question})
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": chat.question},
        #         # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #         # {"role": "user", "content": "Where was it played?"}
        #     ]
        messages = messages
        )
    messages.append({"role": "assistant", "content": res.choices[0].message.content})
    print(messages)
    return res.choices[0].message.content