from flask import Flask
app = Flask(__name__)


#this only works in the terminal

userInput = ""
displayText = ""
user = True

while True:
    print("enter a text to print")
    print("enter '<<' to end")
    userInput = input(">")
    match userInput:
        case "<<":
            break
        case _:
            if user:
                displayText = displayText + "\n" + userInput
                print(displayText)
                user = False
            else:
                displayText = displayText + "\n" + "    " + userInput
                print(displayText)
                user = True