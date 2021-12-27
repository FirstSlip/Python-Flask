from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>{datetime.now()}</p>"

app.run()