from typing import Optional
from flask import Flask, url_for, render_template, request, redirect
import sys

app = Flask(__name__)

userInput = ""
user = 0

class Message():
    sent = 0
    name = ""
    template = render_template("message.html")
    message_text = ""

message_list: list[Optional['Message']] = [Message()]*1000

# current_message = ""

@app.route('/', methods=['GET','POST'])
# @app.route('/')
def index():
    print("loaded", file=sys.stderr)
    global current_message

    if request.method == 'POST':
       current_message = request.form.get("chat_text", '') 
       print(current_message, file=sys.stderr)
       message_list.append(new Message())

    return render_template("chatwindow.html")


if __name__ == '__main__':
    app.run()



html_template = """
<!DOCTYPE html!>
<html>
    
    <p> text <p>
</html>


"""
def post():
    userInput = input(">")
    if user == 0:
        print("\n" + userInput)
        user = 1
    else: 
        print("\n" + "    " + userInput)
        user = 0

while True:
    post()


#   |   this only works in the terminal
#   v

# userInput = ""
# displayText = ""
# user = True

# while True:
#     print("enter a text to print")
#     print("enter '<<' to end")
#     userInput = input(">")
#     match userInput:
#         case "<<":
#             break
#         case _:
#             if user:
#                 displayText = displayText + "\n" + userInput
#                 print(displayText)
#                 user = False
#             else:
#                 displayText = displayText + "\n" + "    " + userInput
#                 print(displayText)
#                 user = True
