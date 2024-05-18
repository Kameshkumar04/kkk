from tkinter import *
from tkinter import ttk

def show_result():
    selected_food = dropvar2.get()
    selected_restaurant = restaurant_var.get()
    result_label.config(text=f"Your order:\nFood: {selected_food}\nRestaurant: {selected_restaurant}")
    result_label.place(x=220, y=250)

def values(select):
    dropmenu1['menu'].delete(0, 'end')
    for option in restaurants.get(select, []):
        dropmenu1['menu'].add_command(label=option, command=lambda opt=option: restaurant_var.set(opt))
    result_label.place_forget()

obj = Tk()
obj.geometry('600x400')
obj.title("Food Delivery App")
obj.configure(bg='lightblue')

Label(obj, text='Select food:', font=("calibri", 20), bg="aqua").place(x=20, y=20)
Label(obj, text='Select restaurant:', font=("calibri", 20), bg="aqua").place(x=20, y=100)

foods = ["Pizza", "Burger", "Pasta", "Sushi", "Salad"]
dropvar2 = StringVar()
dropmenu = ttk.OptionMenu(obj, dropvar2, "____Select____", *foods, command=values)
dropmenu.place(x=200, y=20)

restaurants = {
    "Pizza": ["Pizza Place A", "Pizza Place B"],
    "Burger": ["Burger Place A", "Burger Place B"],
    "Pasta": ["Pasta Place A", "Pasta Place B"],
    "Sushi": ["Sushi Place A", "Sushi Place B"],
    "Salad": ["Salad Place A", "Salad Place B"]
}
restaurant_var = StringVar()
dropmenu1 = ttk.OptionMenu(obj, restaurant_var, "____Select____", "")
dropmenu1.place(x=200, y=100)

result_label = Label(obj, text='', font=("calibri", 16), bg="lightblue")

Button(obj, text='Place Order', command=show_result).place(x=250, y=175)

obj.mainloop()