import tkinter
from tkinter import ttk


window = tkinter.Tk()

frame = ttk.Frame(window, width=800, height=600)
frame['relief'] = 'sunken'
frame.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(frame, text="List of  Operative Systems")
label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

list_of_elems = ["Windows", "macOS", "Linux", "MS DOS", "Android", "iOS", "Symbian"]
selected = tkinter.StringVar()
radio_buttons = {}
for index, elem in enumerate(list_of_elems):
    radio_buttons[elem] =  ttk.Radiobutton(frame, text=elem, value=elem, variable=selected)
    radio_buttons[elem].grid(column=0, row=index+1, sticky=tkinter.W, columnspan=2)

button_reset = ttk.Button(frame, text='Reset', command= lambda: selected.set(""))
button_reset.grid(column=0, row=len(list_of_elems)+1)

window.mainloop()
