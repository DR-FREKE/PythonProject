from tkinter import Button, Tk;

window = Tk(className="fresh window")
window.minsize(400, 400);

def saySomething():
    minput = input("type something here:");
    print(minput);

button = Button(window, text="click", width=20, height=5, command=saySomething)
button.pack();

window.mainloop();