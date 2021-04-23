from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Converter")
root.geometry("400x400")
root.iconbitmap(r"basketball.ico")
root.configure(bg="#32a852")

count = 0
def test():
    response = messagebox.askyesno("How's it going dude?", "Good function, right?")
    if response == 1:
        messagebox.showinfo("Wow", "Thank you")
    else:
        messagebox.showinfo("Well", "Okay :D")

def test2():
    global count
    root.configure(bg="blue")
    count = count + 1
    label1.configure(text=f"Button clicked{count} times")
    if(count == 2):
        root.configure(bg="pink")
    if(count > 2):
        root.configure(bg="yellow")
    if(count > 3):
        root.configure(bg="#32a852")
    if(count == 0):
        label1.configure(text=f"Button clicked{count} times")
    if(count == 20):
        messagebox.showinfo("Hey there", "You clicked 20 times!")
        root.destroy()


def test3():
    root.configure(bg="#32a852")

Button1 = Button(root, text="Click here", command=test,bg="lightgreen",)
Button1.pack()

Button2 = Button(root, text="Change the background color", command=test2)
Button2.pack()
Button2.place(x=115, y=140)

Button3 = Button(root, text="Set the previous color", command=test3)
Button3.pack()
Button3.place(x=135, y=200)

def selected(event):
    if clicked.get() == "Pound":
        label1.pack()
        Button4.pack()
        label2.pack_forget()
        Button5.pack_forget()
        label3.pack_forget()
        Button6.pack_forget()
    if clicked.get() == "Inches":
        label1.pack_forget()
        Button4.pack_forget()
        label2.pack()
        Button5.pack()
        label3.pack_forget()
        Button6.pack_forget()
    if clicked.get() == "Miles":
        label1.pack_forget()
        label2.pack_forget()
        Button4.pack_forget()
        Button5.pack_forget()
        label3.pack()
        Button6.pack()


def convert():
    kilograms = round(float(textbox1.get()) / 2.205)
    label1.configure(text = "Kilograms" + str(kilograms))

def convert2():
        inches = round(float(textbox1.get()) * 2.54)
        label2.configure(text= "Centimeters" + str(inches))

def convert3():
        miles = round(float(textbox1.get()) * 1.609)
        label3.configure(text="Kilometers" + str(miles))

options = [
    "Inches",
    "Pound",
    "Miles",
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack()

textbox1 = Entry(root, width=12)
textbox1.pack()

label1 = Label(root, text="Kilograms:")
label1.pack()
label1.pack_forget()

label2 = Label(root, text="Centimeters:")
label2.pack()
label2.pack_forget()

label3 = Label(root,text="Kilometers:")
label3.pack()
label3.pack_forget()

label4 = Label(root, text="Information: This program is written in Python,\nyou can convert pounds into kilograms,\ninches into centimetres,\nand miles into kilometers")
label4.place(x=75,y=300)

Button4 = Button(root, text="Convert pounds into killograms", command=convert)
Button4.pack()
Button4.place(x=115,y=100)
Button4.pack_forget()

Button5 = Button(root, text="Convert inches into centimeters", command=convert2)
Button5.pack()
Button5.pack_forget()

Button6 = Button(root, text="Convert miles into kilometers", command=convert3)
Button6.pack()
Button6.pack_forget()

root.mainloop()