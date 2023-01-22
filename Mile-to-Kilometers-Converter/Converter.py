from tkinter import *


def button_clicked():
    integer = float(input.get())
    result = integer * 1.609
    result_label.config(text=str(result))


window = Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Entry
input = Entry(width=7)
input.grid(row=0, column=1)

# Label
miles_label = Label(text='Miles', font=('Arial', 24))
miles_label.grid(row=0, column=2)

# Label
is_equal_label = Label(text='is equal to:', font=('Arial', 24))
is_equal_label.grid(row=1, column=0)

# Label
result_label = Label(text=0, font=('Arial', 24))
result_label.grid(row=1, column=1)

# Label
km_label = Label(text='Km', font=('Arial', 24))
km_label.grid(row=1, column=2)

# Button
button = Button(text='Calculate', command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
def pri(x):
    print(x)
