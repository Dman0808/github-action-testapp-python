from flask import Flask
app = Flask(1.1.2)

from app import app
@app.route("C:User/dus08/OneDrive/Documents/Github/AutoGPT/autogpt_platform/autogpt_libs/pyproject.toml")
def hello():
    return "Hello World!"
