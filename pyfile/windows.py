from tkinter import *


def add():
    num1 = no1.get()
    num2 = no2.get()
    num3 = no3.get()
    num4 = no4.get()

    # Perform the addition
    sum_result = num1 + num2 + num3 + num4

    # Update the result label
    result.config(text="Result : %d" % sum_result)


obj = Tk()
obj.geometry('600x400')
obj.title("Operation")
obj.configure(bg='purple')

# Create labels for input fields
Label(obj, text='Enter A Value:', font=("calibri", 20), bg="aqua").grid(row=1, column=0)
Label(obj, text='Enter B Value:', font=("calibri", 20), bg="aqua").grid(row=2, column=0)
Label(obj, text='Enter C Value:', font=("calibri", 20), bg="aqua").grid(row=3, column=0)
Label(obj, text='Enter D Value:', font=("calibri", 20), bg="aqua").grid(row=4, column=0)

no1 = IntVar()
no2 = IntVar()
no3 = IntVar()
no4 = IntVar()

# Create entry fields for input values
Entry(obj, textvariable=no1, font=("calibri", 20)).grid(row=1, column=1)
Entry(obj, textvariable=no2, font=("calibri", 20)).grid(row=2, column=1)
Entry(obj, textvariable=no3, font=("calibri", 20)).grid(row=3, column=1)
Entry(obj, textvariable=no4, font=("calibri", 20)).grid(row=4, column=1)

# Create the "Add" button
Button(obj, text="Add", font=("calibri", 13), bg="gray", fg="white", width="10", height="1", command=add).grid(row=5,
                                                                                                               column=1)

# Create a label for displaying the result
result = Label(obj, font=("calibri", 13), bg="aqua")
result.grid(row=6, column=1)

obj.mainloop()