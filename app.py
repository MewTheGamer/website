from flask import Flask, url_for, render_template, request, redirect
import sys

app = Flask(__name__)

current_message = ""

@app.route('/', methods=['GET','POST'])
# @app.route('/')
def index():
    print("loaded", file=sys.stderr)
    global current_message

    if request.method == 'POST':
       current_message = request.form.get("chat_text", '') 
       print(current_message, file=sys.stderr)

    return render_template("chatwindow.html")


if __name__ == '__main__':
    app.run()

#this only works in the terminal

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
