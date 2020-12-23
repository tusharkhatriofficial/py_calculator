from tkinter import *
window  = Tk()
window.title("Calculator")
window.configure(bg="#ffa931")
window.resizable(0, 0)
text_box = Entry(window, width=35, borderwidth=5)
text_box.pack()

text_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def button_click(number):
    current = text_box.get()
    text_box.delete(0, END)
    text_box.insert(0, str(current) + str(number))
def button_clear():
    text_box.delete(0, END)
def button_add():
    first_number = text_box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    text_box.delete(0, END)

def button_subtract():
    first_number = text_box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    text_box.delete(0, END)
def button_multiply():
    first_number = text_box.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    text_box.delete(0, END)
def button_divide():
    first_number = text_box.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    text_box.delete(0, END)

def button_equal():
    global s_num
    s_num = text_box.get()
    text_box.delete(0, END)
    if math == "addition":
        text_box.insert(0, int(f_num) + int(s_num))
    elif math == "subtraction":
        text_box.insert(0, int(f_num) - int(s_num))
    elif math == "multiplication":
        text_box.insert(0, int(f_num) * int(s_num))
    elif math == "division":
        text_box.insert(0, int(f_num) / int(s_num))





#creating buttons

button_1 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_2 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_3 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_8 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_9 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(window, text="clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(window, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=40, pady=20, command=button_divide)





# putting buttons at a place
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_subtract.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_divide.grid(row=3, column=3)


button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=3)
button_equal.grid(row=6, column=1, columnspan=2)


# :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)


def on_enter(e):
    button_1['background'] = '#faf0af'
def on_leave(e):
    button_1['background'] = 'SystemButtonFace'
button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)

def on_enter(e):
    button_2['background'] = '#faf0af'
def on_leave(e):
    button_2['background'] = 'SystemButtonFace'
button_2.bind("<Enter>", on_enter)
button_2.bind("<Leave>", on_leave)

def on_enter(e):
    button_3['background'] = '#faf0af'
def on_leave(e):
    button_3['background'] = 'SystemButtonFace'
button_3.bind("<Enter>", on_enter)
button_3.bind("<Leave>", on_leave)

def on_enter(e):
    button_4['background'] = '#faf0af'
def on_leave(e):
    button_4['background'] = 'SystemButtonFace'
button_4.bind("<Enter>", on_enter)
button_4.bind("<Leave>", on_leave)

def on_enter(e):
    button_5['background'] = '#faf0af'
def on_leave(e):
    button_5['background'] = 'SystemButtonFace'
button_5.bind("<Enter>", on_enter)
button_5.bind("<Leave>", on_leave)

def on_enter(e):
    button_6['background'] = '#faf0af'
def on_leave(e):
    button_6['background'] = 'SystemButtonFace'
button_6.bind("<Enter>", on_enter)
button_6.bind("<Leave>", on_leave)

def on_enter(e):
    button_7['background'] = '#faf0af'
def on_leave(e):
    button_7['background'] = 'SystemButtonFace'
button_7.bind("<Enter>", on_enter)
button_7.bind("<Leave>", on_leave)

def on_enter(e):
    button_8['background'] = '#faf0af'
def on_leave(e):
    button_8['background'] = 'SystemButtonFace'
button_8.bind("<Enter>", on_enter)
button_8.bind("<Leave>", on_leave)

def on_enter(e):
    button_9['background'] = '#faf0af'
def on_leave(e):
    button_9['background'] = 'SystemButtonFace'
button_9.bind("<Enter>", on_enter)
button_9.bind("<Leave>", on_leave)

def on_enter(e):
    button_0['background'] = '#faf0af'
def on_leave(e):
    button_0['background'] = 'SystemButtonFace'
button_0.bind("<Enter>", on_enter)
button_0.bind("<Leave>", on_leave)

def on_enter(e):
    button_equal['background'] = '#76ead7'
def on_leave(e):
    button_equal['background'] = 'SystemButtonFace'
button_equal.bind("<Enter>", on_enter)
button_equal.bind("<Leave>", on_leave)

def on_enter(e):
    button_clear['background'] = '#fa1616'
def on_leave(e):
    button_clear['background'] = 'SystemButtonFace'
button_clear.bind("<Enter>", on_enter)
button_clear.bind("<Leave>", on_leave)



window.mainloop()
