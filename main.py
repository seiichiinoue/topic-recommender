import os
from dotenv import load_dotenv
import openai
from pydantic import BaseModel
from fastapi import FastAPI
from jinja2 import Template, Environment, FileSystemLoader

load_dotenv()
openai.api_key = os.getenv('API_KEY')

app = FastAPI(docs_url="/docs")

env = Environment(loader=FileSystemLoader('./template'))
template = env.get_template('prompt.tpl')

class Word(BaseModel):
    content: str
    
def generate_prompt(word: str):
    prompt = template.render(word=word)
    return prompt

@app.post("/sense_induction")
def question(word: Word):
    prompt = generate_prompt(word.content)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    res_text = response.choices[0]["message"]["content"].strip()
    senses = {}
    for i, text in enumerate(res_text.split("\n")):
        if text.startswith("- "):
            text = text[2:]
        senses[f"sense-{i}"] = text
    return senses