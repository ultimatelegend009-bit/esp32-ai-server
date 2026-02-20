from flask import Flask, request
import google.generativeai as genai
import os

# API key from Render Environment
genai.configure(api_key=os.environ.get("AIzaSyA9WcHm0uSk-FW0p6fh40ujuwEMZLYyYhg"))

model = genai.GenerativeModel("gemini-pro")
app = Flask(__name__)

@app.route("/ask")
def ask():
    q = request.args.get("q")
    if not q:
        return "No question"

    response = model.generate_content(q)
    return response.text

app.run(host="0.0.0.0", port=10000)
