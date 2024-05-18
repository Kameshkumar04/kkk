from tkinter import *
from tkinter import ttk
def value(select):
    dropmenu1.set_menu(* option2.get(select))

obj = Tk()
obj.geometry('600x400')
obj.title("Drop Down List")
obj.configure(bg='lightblue')
Label(obj, text='select state:', font=("calibri", 20), bg="aqua").place(x=20, y=20)
Label(obj, text='select District:', font=("calibri", 20), bg="aqua").place(x=20, y=100)
options1=["Andhrapradesh","Goa","Karnataka","Kerala","Tamilnadu"]
dropvar1 = StringVar()
dropmenu=ttk.OptionMenu(obj,dropvar1,"____Select____",*options1,command=value)
dropmenu.place(x=200,y=20)
options2={"Andhrapradesh":["vijayawada","guntur","chitoor"],"Goa":["northgoa","SouthGoa"],"Karnataka":["Bangalore","Mysore"],"Kerala":["alapola","AAlapi"]}
dropvar2=StringVar()
dropmenu1=ttk.OptionMenu(obj,dropvar2,"____Select____",*options1,command=value)
dropmenu1.place(x=200,y=100)


obj.mainloop()
