import tkinter as tk
from tkinter.constants import COMMAND
window = tk.Tk()
currentlyOn = False
currentlyOff = True

# schijf hier tussen je code

def changeSwitchState():
    global currentlyOff, currentlyOn, button

    if currentlyOff == True:
        print("light is off")
        btn_text.set("Light switch off")
        currentlyOff = False
        currentlyOn = True
        window.configure(bg='yellow')

    elif currentlyOn == True:
        print("light is on")
        btn_text.set("Light switch on")
        currentlyOff = True
        currentlyOn = False
        window.configure(bg='white')

btn_text = tk.StringVar()
button = tk.Button(textvariable=btn_text, bg="white", fg="black", command = changeSwitchState)
button.pack(pady = 20, padx = 20)
btn_text.set("Light switch on")


# schijf hier tussen je code

window.mainloop()