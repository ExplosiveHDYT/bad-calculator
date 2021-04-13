#imports PySuperSimpleGUI
from PySuperSimpleGUI import *


#put GUI code here
GUI = [
    [Text("This is the worst calculator \n app possilble in python.", font=("sans", 20))],
    [Text("Enter First value -->    ", font=("sans", 10)), InputText(key="a", font=("sans", 20))],
    [Text("Enter Second value -->", font=("sans", 10)),InputText(key="b", font=("sans", 20))],
    [Button("+", font=("sans", 20)), Button("-", font=("sans", 20))],
    [Button("*", font=("sans", 20)), Button("/", font=("sans", 20))]
    ] 

#Customization
window = Window("Calculinator Thingy", GUI, size=(400, 400), resizable=True)
event, values = window.read()
#Variables
a = int(values["a"])
b = int(values["b"])
c = a + b
d = a - b
e = a * b
f = a / b


#Backend Stuff
while True:
    if event == "+":
        popup("----------------\n|     {ans}     |\n----------------".format(ans = c))
        popen("main.py")
        break
    if event == "-":
        popup("----------------\n|     {ans}     |\n----------------".format(ans = d))
        popen("main.py")
        break
    if event == "*":
        popup("----------------\n|     {ans}     |\n----------------".format(ans = e))
        popen("main.py")
        break
    if event == "/":
        popup("----------------\n|     {ans}     |\n----------------".format(ans = f))
        popen("main.py")
        break
#adds an X button to close the tab
X_Button()
