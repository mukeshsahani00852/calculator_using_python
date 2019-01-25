# creating the calculator using tkinter gui

# addition function

"""
def donothing():
    pass


"""
from tkinter import *
from tkinter import messagebox

def err():
    messagebox.showerror("Error", "some error occured")

def how():
    root = Tk()
    root.title("how to use")
    root.geometry("1360x768")
    root.wm_iconbitmap('C:/Users/Mukesh/Downloads/Ampeross-Smooth-Uplay.ico')
    f =  Frame(root, height=768, width=1360, bg="pink")
    f.propagate(0)
    f.pack()
    strt = "welcome in the HOW TO USER the calculator"
    str1 = "1. write the value in quantity 1 and quantity 2 click the operation buttons."
    str2 = "2. for factorial write the element in the quantity 1 and press ! button."
    str3 = "3. for finding the sin(x) write the element in the quantity 1 and press sin(x) button."
    str4 = "4. for finding the cos(x) write the element in the quantity 1 and press cos(x) button."
    str5 = "5. for finding the tan(x) write the element in the quantity 1 and press tan(x) button"
    ll_font = ('Times', -50, 'italic underline')
    l = Label(f, text=strt, font=ll_font, bg='pink', fg='blue')
    l1 = Label(f, text=str1, font=l_font, bg='pink', fg='blue')
    l2 = Label(f, text=str2, font=l_font, bg='pink', fg='blue')
    l3 = Label(f, text=str3, font=l_font, bg='pink', fg='blue')
    l4 = Label(f, text=str4, font=l_font, bg='pink', fg='blue')
    l5 = Label(f, text=str5, font=l_font, bg='pink', fg='blue')
    l.pack()
    l1.place(x=150, y=150)
    l2.place(x=150, y=250)
    l3.place(x=150, y=350)
    l4.place(x=150, y=450)
    l5.place(x=150, y=550)

from math import *

def sina():
    try:
        var1 = e1.get()
        num1 = float(var1)

        result = sin(num1)
        if result ==0:
            res = "Zero"
        else:
            res = str(result)
        res+=" "*100
        lblo = Label(text="result is : "+res, bg='pink', font=l_font,fg='blue').place(x=550, y=50)
        result = 0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()

def cosa():
    try:
        var1 = e1.get()
        num1 = float(var1)
        result = cos(num1)
        if result == 0:
            res = "Zero"
        else:
            res = str(result)
        res += " " * 100
        lblo = Label(text="result is : "+res, bg='pink', font=l_font, fg='blue').place(x=550, y=50)
        result = 0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()
def tana():
    try:
        var1 = e1.get()
        num1 = float(var1)
        result = tan(num1)
        if result == 0:
            res = " Zero"
        else:
            res = str(result)
        res += " " * 100
        lblo = Label(text="result is : "+res, bg='pink', font=l_font, fg='blue').place(x=550, y=50)
        result = 0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()
def facta():
    try:
        var1 = e1.get()
        num1 = int(var1)
        result = factorial(num1)
        res = str(result)
        res += " " * 100
        lblo = Label(text="result is : "+res, bg='pink', font=l_font, fg='blue').place(x=550, y=50)
        result = 0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()


def addition():
    x = e1.get()
    y = e2.get()
    str1 = str(x)
    str2 = str(y)
    try:
        num1 = float(x)
        num2 = float(y)
        result = num1 + num2
        res = str(result)
        res+=" "*100
        lbl = Label(f, text="result is : "+res, font=l_font, fg='blue', bg='pink').place(x=550, y=50)
        result=0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()

# addition function


def multiplication():
    x = e1.get()
    y = e2.get()
    str1 = str(x)
    str2 = str(y)

    try:
        num1 = float(x)
        num2 = float(y)
        result = num1 * num2
        res = str(result)
        res += ' ' * 100
        lbl = Label(text="result is : " +res, font=l_font, fg='blue', bg='pink').place(x=550, y=50)
        result=0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()

def division():
    x = e1.get()
    y = e2.get()
    str1 = str(x)
    str2 = str(y)
    try:
        num1 = float(x)
        num2 = float(y)
        result = num1 / num2
        res = str(result)
        res += ' ' * 100
        lbl = Label(text="result is : " +res, font=l_font, fg='blue', bg='pink').place(x=550, y=50)
        res  = ' '
        result=0
    except ZeroDivisionError:
        messagebox.showerror("error"," Divided by Zero")

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()



def subtract():
    x = e1.get()
    y = e2.get()
    str1 = str(x)
    str2 = str(y)
    try:
        num1 = float(x)
        num2 = float(y)
        result = num1 - num2
        res = str(result)
        res += ' ' * 100
        lbl = Label(text="result is : " +res, font=l_font, fg='blue', bg='pink').place(x=550, y=50)
        result = 0
        res = ' '

    except ValueError:
        messagebox.showinfo("error","please give valid input")

    except:
        err()




root = Tk()
root.title("calculator")
root.geometry("1360x768")
root.wm_iconbitmap('C:/Users/Mukesh/Downloads/Dakirby309-Windows-8-Metro-Apps-Calculator-Metro.ico')
f = Frame(root, height=700, width=1360, bg='pink')
f.propagate(-1)
f.pack()

lbll_font = ('Times', -50, 'italic underline')

lbll = Label(f, text="CALCULATOR", font=lbll_font, bg='pink', fg='blue')
lbll.place(x=500, y=600)

# Major label


# font for label

l_font = ('Times', -30, 'bold ')

# font for label

# label

l1 = Label(f, text="  Quantity 1 : ", font=l_font, bg='pink', fg='blue')
l2 = Label(f, text="  Quantity 2 : ", font=l_font, bg='pink', fg='blue')

# label


# font for entry

e_font = ('Times', -30, 'bold')

# font for entry

e1 = Entry(f, font=e_font, bg='pink', fg='purple', width=15)
e2 = Entry(f, font=e_font, bg='pink', fg='purple', width=15)


# font for button

b_font = ('Times', -25, 'italic')

# font for button
ba = Button(f, text=" + ", width=5, height=3, bg='white', fg='blue', font=b_font, command=addition)
bm = Button(f, text=" * ", width=5, height=3, bg='white', fg='blue', font=b_font, command=multiplication)
bs = Button(f, text=" - ", width=5, height=3, bg='white', fg='blue', font=b_font, command=subtract)
bd = Button(f, text=" / ", width=5, height=3, bg='white', fg='blue', font=b_font, command=division)
bf = Button(f, text=" ! ", width=5, height=3, bg='white', fg='blue', font=b_font,command=facta)
bsi = Button(f, text="sin(x)", width=5, height=3, bg='white', fg='blue', font=b_font, command=sina)
bco = Button(f, text="cos(x)", width=5, height=3, bg='white', fg='blue', font=b_font, command=cosa)
bta = Button(f, text="tan(x)", width=5, height=3, bg='white', fg='blue', font=b_font, command=tana)
bh = Button(f, text="How to use", width=10, height=2, bg='white', fg='blue', font=b_font, command=how)
be = Button(f, text="exit", width=10, height=2, bg='white', fg='blue', font=b_font, command=root.destroy)




be.place(x=1100, y=570)
e1.place(x=900, y=300)
e2.place(x=900, y=400)
bh.place(x=50, y=50)
bf.place(x=120, y=300)
bsi.place(x=120, y=400)
bco.place(x=360, y=300)
bta.place(x=360, y=400)
ba.place(x=200, y=300)
bm.place(x=280, y=300)
bs.place(x=200, y=400)
bd.place(x=280, y=400)
l1.place(x=700, y=300)
l2.place(x=700, y=400)

root.mainloop()
