from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
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
