from flask import Flask
app = Flask(__name__)
userInput = ""
displayText = ""
user = 0
while True:
    print("enter a text to print")
    print("enter '<<' to end")
    userInput = input(">")
    match userInput:
        case "<<":
            break
        case _:
            
            displayText = displayText + "\n" + userInput
            print(displayText)