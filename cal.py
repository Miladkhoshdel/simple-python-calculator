#Created By: Milad Khoshdel
#Blog: https://regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkhoshdel

import re

print("calculator")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("GoodBye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else: 
            previous = eval(str(previous) + equation)

while run:
    performMath()
