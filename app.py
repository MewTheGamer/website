from typing import Optional
from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template
import sys
from datetime import datetime, timezone

app = Flask(__name__)

userInput = ""
user = 0

# class Message():
#     sent = 0
#     name = ""
#     template = render_template("message.html")
#     message_text = ""


current_message = ""

messages = ["Welcome"]

message_template = Template("""
                            <p>{{ message }}</p>g`
                            """)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/', methods=['GET','POST'])
# @app.route('/')
def index():
    print("loaded", file=sys.stderr)
    global current_message

    if request.method == 'POST':
        current_message = request.form.get("chat_text", '') 
        print(current_message, file=sys.stderr)

        messages.append(current_message)
        print(messages, file=sys.stderr)


    return render_template("chatwindow.html", message_list=messages)


if __name__ == '__main__':
    app.app_context()
    app.run()
