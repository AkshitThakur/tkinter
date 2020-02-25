from tkinter import *
import csv

root = Tk()#create window
root.geometry("600x700") #fixing the size of interface.
root.title("Tk learning")

def store():
    n = name.get()#save the text present in box.
    name.delete(0, END)#delete the text present in box.
    g = gmail.get()#save the text present in box.
    gmail.delete(0, END)#delete the text present in box.
    data = [n,g]
    lb.config(text=data)#assign text on label.
    file = "tkpro.csv"
    with open(file, "a") as f:
        #headers=["Names","Gmails"]
        w = csv.writer(f, dialect='excel')
        #w.writerow(headers)
        w.writerow(data)

Label(root, text="Name : ").grid(row=0, column=0)
name = Entry(root)#create a entery box.
name.grid(row=0, column=1)
Label(root, text="Gmail : ").grid(row=1, column=0)
gmail = Entry(root)#create a entery box.
gmail.grid(row=1, column=1)

Button(root, text="Sign Up", command=store).grid(row=2, column=1)

lb = Label(root)
lb.grid(row=3, column=0, columnspan=1)

root.mainloop()
