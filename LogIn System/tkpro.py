from tkinter import *
import csv

root = Tk()#create window
root.geometry("600x700") #fixing the size of interface.
root.title("Tk Project")

def store():
    n = name.get()#save the text present in box.
    name.delete(0, END)#delete the text present in box.
    g = gmail.get()#save the text present in box.
    gmail.delete(0, END)#delete the text present in box.
    if n and g:#if we donot put anyting in entery it will not save in csv.
        data = [n,g]
        Label(root, text=data).grid(row=4, column=0)
        file = "tkpro.csv"
        with open(file, "a") as f:
            #headers=["Names","Gmails"]
            w = csv.writer(f, dialect='excel')
            #w.writerow(headers)
            w.writerow(data)
    else:#else is not working
        Label(root, text="Please fill the above requirment.").grid(row=4, column=0)

Label(root, text="LogIn System :", fg="green").grid(row=0, column=0)
Label(root, text="Name : ").grid(row=1, column=0)
name = Entry(root)#create a entery box.
name.grid(row=1, column=1)
Label(root, text="Gmail : ").grid(row=2, column=0)
gmail = Entry(root)#create a entery box.
gmail.grid(row=2, column=1)

Button(root, text="Sign Up", fg="blue", command=store, padx=30).grid(row=3, column=1)

root.mainloop()
