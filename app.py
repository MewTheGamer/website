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

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True, default="Anonymous") 
    email = db.Column(db.String(100), nullable=False) 
    password = db.Column(db.String(100), nullable=False) 
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for("profile"))

name = ""
email = ""
password = ""

@app.route('/profile', methods=['GET','POST'])
def profile():
    print("loaded profile", file=sys.stderr)
    
    if request.method == 'POST':
        try:
            print("trying profile", file=sys.stderr)
            new_profile = Profile(
                    name=request.form.get("name"),
                    email=request.form.get("email"),
                    password=request.form.get("password")
                    )
            result = Profile.query.all()
            print(result, file=sys.stderr)
            if result == []:
                db.session.add(new_profile)
                db.session.commit()
                return redirect(url_for("chat"), )
            else:
                for profile in result:
                    print("trying profile", file=sys.stderr)
                    print(f"trying profile in for loop", file=sys.stderr)
                    if profile.name == new_profile.name:
                        print("Duplicate name", file=sys.stderr)
                        return redirect(url_for("profile"))
                    else:
                        print("created profile", file=sys.stderr)
                        print(result, file=sys.stderr)
                        db.session.add(new_profile)
                        db.session.commit()
                        return redirect(url_for("chat"), )
        except Exception as e:
            print(f"ERROR", file=sys.stderr)
            db.session.rollback()
            db.session.commit()
            print(f"ERROR{e}", file=sys.stderr)
            return render_template("profile.html")

    else:
        return render_template("profile.html")

@app.route('/chat', methods=['GET','POST'])
def chat():
    print("loaded chat", file=sys.stderr)
    global current_message

    if request.method == 'POST':
        current_message = request.form.get("chat_text", '') 
        print(current_message, file=sys.stderr)

        messages.append(current_message)
        print(messages, file=sys.stderr)


    return render_template("chatwindow.html", message_list=messages)


if __name__ == '__main__':
    app.run()

