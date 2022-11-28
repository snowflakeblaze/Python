## Create a program in Python that fulfills the following:
## Create a window using the Tkinter module we used in class. 
## Your window should contain at least 2 labels. 
## One of the labels should have a greeting (“Hello “, “Welcome “, etc.), 
## and you should then have a function that will add some text to the label 
## right after the greeting, such as after clicking on a button.
## The other label on your window does not need to be changed through an 
## event with a button and can be any text you wish it to be.
## Finally, your window and text should be colors other than the default 
## black text and gray background.

import tkinter as tk

window = tk.Tk()

def clicked():
    added = "Hello " + user_input.get()
    input_lbl.configure(text = added)
    
def clear_text():
    added = ""
    input_lbl.configure(text = added)
   
window.title("Tkinter module")
window.geometry("400x200")
window.configure(background="cyan")

label = tk.Label(window, text = "Welcome", foreground = "pink",
    background = "black")
label.grid(column = 0, row = 1)

input_lbl = tk.Label(window, text = "enter text", foreground = "pink",
    background = "black")
input_lbl.grid(column = 1, row = 0)

user_input = tk.Entry(window, width = 20)
user_input.grid(column = 1, row = 1)

save_btn = tk.Button(window, text = "Enter", command = clicked)
save_btn.grid(column = 3, row = 0)

delete_btn = tk.Button(window, text = "Clear", command = clear_text)
delete_btn.grid(column = 3, row = 2)


window.mainloop()