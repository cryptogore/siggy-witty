from flask import Flask, request, jsonify
from openai import OpenAI
from rag import get_context
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

SYSTEM_PROMPT = open("siggy_prompt.txt").read()

@app.route("/")
def home():
    return "Siggy is ready."

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    context = get_context()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"system","content":context},
            {"role":"user","content":user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run()