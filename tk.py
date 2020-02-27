from tkinter import *

root = Tk()#create window
root.geometry("600x700") #fixing the size of interface.
root.title("Tk learning")

"""
label_text = Label(root, text="one", bg="black", fg="yellow")
#bg : backgroung color of label.
#fg : foreground color of label.
#here i have store the text into a variable which is apply on certain window & this text will be shown at that window with help of pack()
label_text.pack(fill=BOTH, side=TOP)#show the text on window.
label_text1 = Label(root, text="two", bg="black", fg="red")
label_text1.pack(fill=BOTH, side=LEFT)
label_text2 = Label(root, text="three", bg="black", fg="blue")
label_text2.pack(fill=BOTH, side=RIGHT)
"""
"""
#grid:
l = Label(root, text="one", bg="blue", fg="red")
l.grid(row=0,column=1)
l1 = Label(root, text="two", bg="black", fg="white")
l1.grid(row=1,column=0)
l2 = Label(root, text="three",fg="red")
l2.grid(row=1,column=1)
l3 = Label(root, text="four",fg="blue")
l3.grid(row=1,column=2)
l4 = Label(root, text="five", bg="blue",)
l4.grid(row=2,column=1)
"""
"""
#frame:
lab1 = Label(root, bg="yellow", text="top")
lab1.pack(fill=BOTH, expand=TRUE)

frame_var = Frame(root)
frame_var.pack(fill=BOTH, expand=TRUE)
fra1 = Label(frame_var, bg="red", text="one")
fra1.pack(fill=BOTH, expand=TRUE, side=LEFT)
fra2 = Label(frame_var, bg="pink", text="two")
fra2.pack(fill=BOTH, expand=TRUE, side=LEFT)
fra3 = Label(frame_var, bg="green", text="three")
fra3.pack(fill=BOTH, expand=TRUE, side=LEFT)

lab2 = Label(root, bg="blue", text="bottom")
lab2.pack(fill=BOTH, expand=TRUE)
"""
"""
#grid widget:
Label(root, bg="yellow", text="top").pack(fill=BOTH, expand=TRUE)

frame_var = Frame(root)
frame_var.pack(fill=BOTH, expand=TRUE)
fra1 = Label(frame_var, bg="red", text="one").pack(fill=BOTH, expand=TRUE, side=LEFT)
fra2 = Label(frame_var, bg="pink", text="two").pack(fill=BOTH, expand=TRUE, side=LEFT)
fra3 = Label(frame_var, bg="green", text="three").pack(fill=BOTH, expand=TRUE, side=LEFT)

Label(root, bg="blue", text="bottom").pack(fill=BOTH, expand=TRUE)

#label frames:
l_f = LabelFrame(root, text="label frame", padx=10, pady=10)
l_f.pack()
Label(l_f, bg="blue", text="one").grid(row=0, column=0, sticky=W)
Label(l_f, bg="blue", text="two").grid(row=1, column=0, sticky=W)

Message(root, text="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", width=1500)\
    .pack()#\ means continue the line.
#Message widget can have multiple lines but Label has only one.

#canvas widget: use to put img/shape on the interface.
shape_convas = Canvas(root, bg='light blue', width=300, height=300)
img_convas = Canvas(root, width=300, height=300)

shape_convas.create_line(0,150,300,150, width=2, fill='black')#create_line create a line.
#0=x1,150=y1 starting pt. of line & x2=300,y2=150 end pt. of line. width = width of line & fill means which color fill on line
shape_convas.create_line(150,0,150,300, width=2, fill='black')
shape_convas.create_rectangle(5,160,140,290, fill='red')
shape_convas.create_arc(5,5,140,140, start=30, extent=300, fill='blue')
shape_convas.create_oval(160,5,290,140, fill='pink')
shape_convas.create_polygon(225,160,160,290,290,290, fill='green')
photo = PhotoImage(file="im.png")
img_convas.create_image(0,0, anchor=NW, image=photo)
img_convas.create_text(150,5, text="heollooo", fill="red")
shape_convas.grid(row=0, column=0)
img_convas.grid(row=0, column=1)

img = PhotoImage(file="img.png")
Label(root, image=img).pack(fill=BOTH, side=LEFT)
im = PhotoImage(file="im.png")
Label(root, image=im).pack(fill=BOTH, side=RIGHT)

def exe():
    disp.config(text="you clicked")#config uesd to add value on Label.
#this fxn. call when button is clicked & text is added to disp variable.
Button(root, text="click me", command=exe).pack()#if button never click then the disp value never change & it remane empty.

disp = Label(root)
disp.pack()#disp printed with text value

#messagebox widget:
def hello():
    from tkinter import messagebox
    messagebox.showinfo("pop-up", "hello guys")
#messagebox create a pop up & showinfo display message we want to print on pop-up.
#1st argg of showinfo display pop-up name & second display content on pop-up.
Button(root, text="click", command=hello, bg="blue").pack()

from tkinter import messagebox
def disp():
    user_input = entry_box.get()
    messagebox.showinfo("input", user_input)

Label(root, text="entry widget").grid(row=0, column=0, columnspan=4)
Label(root, text="enter input: ").grid(row=1, column=0)

entry_box = Entry(root)#create a entery box.
entry_box.grid(row=1, column=1)

Button(root, text="disp", command=disp).grid(row=1, column=2)

def disp():
    user_input = entry_box.get()#save the text present in box.
    entry_box.delete(0, END)#delete the text present in box.
    lb.config(text=user_input)#assign text on label.

Label(root, text="entry widget").grid(row=0, column=0, columnspan=4)
Label(root, text="enter input: ").grid(row=1, column=0)

entry_box = Entry(root)#create a entery box.
entry_box.grid(row=1, column=1)

Button(root, text="disp", command=disp).grid(row=1, column=2)

lb = Label(root)
lb.grid(row=2, column=0, columnspan=3)

#text widget:contain more line then entry
def show():
    data = disc.get(1.0, END)#neccesary 1.0 shows the index.
    disc.delete(1.0, END)
    mg.config(text=data)

Label(root, text="Add discription", fg="blue").pack()
disc = Text(root, width=50, height=5)#create box.
disc.pack()
Button(root, text="display", command=show).pack()

mg = Message(root, width=30)
mg.pack()

#check button:
def disp():
    check_value = check_control.get()
    lb.config(text=check_value)

check_control = IntVar()#int value default=0
Checkbutton(root, text="check button", variable=check_control, command=disp).pack()
#variable=check_control make value one when we click in checkbox.

lb = Label(root)
lb.pack()

#spin box:
def disp():
    val = box.get()
    lb.config(text=val)

box = Spinbox(root, from_=0, to=10, command=disp)#box with range 0 to 10.
box.pack()

lb = Label(root)
lb.pack()

#list box:
def disp():
    val = option.curselection()#select the option on which cursor has made the click.
    lb.config(text=val)

option = Listbox(root, height=5)
option.insert(1, "cricket")
option.insert(2, "bedminten")
option.insert(3, "hockey")
option.insert(4, "vollyball")
option.insert(5, "chess")
option.pack()

Button(root, text="Submit", command=disp).pack()
lb = Label(root)
lb.pack()

#OptionMenu:
Label(root, text="select options: ").pack()
def disp():
    val = op_default.get()
    lb.config(text=val)

op = ["one","two","three"]
op_default = StringVar()
op_default.set(op[0])
menu = OptionMenu(root, op_default, *op)
menu.pack()

Button(root, text="Submit", command=disp).pack()
lb = Label(root)
lb.pack()

#radio button
def display():
    val = radio.get()
    lb.config(text=val)

radio = StringVar(value="one")
Radiobutton(root, text="two", variable=radio, value="two 2", command=display).pack()
Radiobutton(root, text="one", variable=radio, value="one 1", command=display).pack()
Radiobutton(root, text="three", variable=radio, value="three 3", command=display).pack()
Radiobutton(root, text="four", variable=radio, value="four 4", command=display).pack()

lb = Label(root)
lb.pack()

#menu widget:
def new():
    msg.config(text="create new file")

def edit():
    msg.config(text="edit the file")

def save():
    msg.config(text="save the file")

def red():
    msg.config(bg="red")

def blue():
    msg.config(bg="blue")

def font():
    msg.config(fg="green")

msg = Message(root, bg="red")
msg.pack(fill=BOTH, expand=TRUE)

menu_bar = Menu(root)#create menu bar.
menu_text = Menu(menu_bar, tearoff=0)#option that we have on menu bar.
menu_text.add_command(label="New", command=new)
#add_command are option that display when we click on option from menubar.
menu_text.add_command(label="Edit", command=edit)
menu_text.add_command(label="Save", command=save)
menu_bar.add_cascade(label="Menu", menu=menu_text)
#create assign file,edit,save to a perticular option.

menu_text1 = Menu(menu_bar, tearoff=0)#option that we have on menu bar.
menu_text1.add_command(label="red", command=red)
menu_text1.add_command(label="blue", command=blue)
menu_bar.add_cascade(label="color", menu=menu_text1)

menu_text2 = Menu(menu_bar, tearoff=0)#option that we have on menu bar.
menu_text2.add_command(label="green", command=font)
menu_bar.add_cascade(label="Font", menu=menu_text2)

root.config(menu=menu_bar)

#pop_up menu:
def new():
    msg.config(text="create new file")
def dl():
    msg.config(text="delete the file")
def red():
    msg.config(bg="red")
def font():
    msg.config(fg="green")
def popup(event):#we acn see menu option on write click.
    pop_up.post(event.x_root, event.y_root)

msg = Message(root, bg="red")
msg.pack(fill=BOTH, expand=TRUE)

pop_up = Menu(root, tearoff=0)
pop_up.add_command(label="delete", command=dl)
pop_up.add_command(label="new", command=new)
pop_up.add_command(label="red", command=red)
pop_up.add_command(label="green", command=font)

msg.bind("<Button-3>", popup)#these all option show when we make a right click.

#scrollbar:
scr = Scrollbar(root)
scr.pack(fill=Y, side=RIGHT)
my_list = Listbox(root, yscrollcommand = scr.set)
for i in range(50):
    my_list.insert(END, "here"+str(i))
my_list.pack(side=LEFT, fill=BOTH)
scr.config(command=my_list.yview)
"""

root.mainloop()
