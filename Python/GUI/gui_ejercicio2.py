import tkinter
from tkinter import ttk
def reset(dictionary):
    for key, value in dictionary.items():
        value['variable'].set(0)
        
window = tkinter.Tk()

frame = ttk.Frame(window, width=800, height=600)
frame['relief'] = 'sunken'
frame.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(frame, text="List of  Operative Systems")
label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

list_of_elems = ["Windows", "macOS", "Linux", "MS DOS", "Android", "iOS", "Symbian"]
dictionary = {}
selected = tkinter.StringVar()

for index, elem in enumerate(list_of_elems):
    dictionary[elem] = {}
    dictionary[elem]['variable'] = tkinter.IntVar()
    dictionary[elem]['checkbutton'] = ttk.Checkbutton(frame, text=elem, variable=dictionary[elem]['variable'])
    dictionary[elem]['checkbutton'].grid(column=0, row=index+1, sticky=tkinter.W, columnspan=2)

button_reset = ttk.Button(frame, text='Reset', command= lambda: reset(dictionary))
button_reset.grid(column=0, row=len(list_of_elems)+1)

window.mainloop()
