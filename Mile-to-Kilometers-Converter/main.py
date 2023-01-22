from tkinter import *


def button_clicked():
    string = input.get()
    my_label.config(text=string)


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label['text'] = 'New Text'
my_label.config(text='New Text')
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20)
# my_label.pack(side='left')
# my_label.pack(side='bottom')

# Button
button = Button(text='Click Me', command=button_clicked)
button.grid(row=1, column=1)

# Button
button = Button(text='Click Me', command=button_clicked)
button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
input.grid(row=3, column=4)

window.mainloop()
