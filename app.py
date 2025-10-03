from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

userInput = ""
user = 0

# current_message = ""

@app.route('/', methods=['GET','POST'])
def index():
    global current_message

    if request.method == 'POST':
       current_message = request.form.get("chat_text", '') 
       print(current_message)

    return render_template("chatwindow.html")


if __name__ == '__main__':
    app.run()

# def post():
#     userInput = input(">")
#     if user == 0:
#         print("\n" + userInput)
#         user = 1
#     else: 
#         print("\n" + "    " + userInput)
#         user = 0

# while True:
#     post()


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
