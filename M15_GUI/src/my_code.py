from tkinter import *

#Your code here!
root = Tk()
root.title("Button app")

def on_button_click():
    lbl.config(text="Button pressed!")

lbl = Label(root, text="Button not pressed!")
lbl.pack(pady=10)

btn = Button(root, text="Press me", command=on_button_click)
btn.pack(pady=10)


#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
