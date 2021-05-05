from tkinter import *
import math
import tkinter.messagebox
root=Tk()
root.geometry("650x400")

#functions

switch=None
root.title("Skarsh scientific calculator")

def click(event):
	b=event.widget
	text=b['text']
	print(text)
	display.insert(END,text)
	
	
	

Font=("Segoe 18")


def pi_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def log_click():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values ")


def fact_click():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error", "Check our values ")


def sqr_click():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error", "Check our value")


def sin_click():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check ur values ")


def cos_click():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check ur valurs")


def tan_click():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check ur value")


	
def btn7_click():
	if disp.get()=='0':
		disp.delete(0,END)
	pos=len(disp.get())
	disp.insert(pos,'7')
	
def btn8_click():
	if disp.get() == '0':
	   disp.delete(0, END)
	pos=len(disp.get())
	disp.insert(pos,'8')
    

def btn9_click():
	if disp.get() == '0':
	   disp.delete(0, END)
	pos = len(disp.get())
	disp.insert(pos, '9')

def btn4_click():
	if disp.get() == '0':		
		disp.delete(0, END)
	pos = len(disp.get())
	disp.insert(pos, '4')

	
def btn5_click():
	if disp.get() == '0':
	   disp.delete(0, END)
	pos = len(disp.get())	
	disp.insert(pos, '5')

def btn6_click():
	if disp.get() == '0':
	   disp.delete(0, END)
	pos = len(disp.get())
	disp.insert(pos, '6')


def btn1_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

def btn0_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def add_click():
    pos = len(disp.get())
    disp.insert(pos, '+')


def sub_click():
    pos = len(disp.get())
    disp.insert(pos, '-')


def mul_click():
    pos = len(disp.get())
    disp.insert(pos, '*')


def div_click():
    pos = len(disp.get())
    disp.insert(pos, '/')
    
def dot_click():
    pos = len(disp.get())
    disp.insert(pos, '.')

def clear_click(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def e_click():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def bl_click():
    pos = len(disp.get())
    disp.insert(pos, '(')


def br_click():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_click():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])
    
def ln_click():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error", "Check ur value")


def mod_click():
    pos = len(disp.get())
    disp.insert(pos, '%')


def equ_click(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Val Error", "Check your values ")
        
        
        
        
def pow_click():
    pos = len(disp.get())
    disp.insert(pos, '**')

        
def in_click():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check ur value")


def keyevent(*args):
    if disp.get() == '0':
        disp.delete(0, END)
        
        
def round_click():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check ur values")

        
Label(text="Skarsh calculator",font="Constantia 20 ",fg="white", bg="#333333",padx=222).pack(side=TOP, fill=X)
input=StringVar()

disp = Entry(root, font="Verdana 25", fg="black", bg="#47a69b", justify=RIGHT, insertbackground="#abbab1")
disp.pack(fill=X,)
f1=Frame(root,bg="#000000")
f1.pack(expand=TRUE,fill=BOTH)
btnpi = Button(f1, text="π", font=Font, relief=SUNKEN, bd=0,  fg="white", bg="#333333",command=pi_click)
btnpi.pack(side=LEFT, expand=TRUE, fill=BOTH)

factbtn = Button(f1, text=" x! ", font="Segoe 18", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=fact_click)
factbtn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logbtn = Button(f1, text="logx", font="Segoe 17", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=log_click)
logbtn.pack(side=LEFT, expand=TRUE, fill=BOTH)
sinbtn = Button(f1, text="sin", font="Segoe 18", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=sin_click)
sinbtn.pack(side=LEFT, expand=TRUE, fill=BOTH)




btn7 = Button(f1, text="7", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=btn7_click)
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(f1, text="8", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=btn8_click)
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(f1, text="9", font="Segoe 23", relief=SUNKEN, bd=0,  fg="white", bg="#333333",command=btn9_click)
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnadd= Button(f1, text="+", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=add_click)
btnadd.pack(side=LEFT, expand=TRUE, fill=BOTH)

#Row 2



f2=Frame(root,bg="#000000")
f2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(f2, text="e", font="Segoe 18", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=e_click)
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(f2, text=" √x", font="Segoe 18", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=sqr_click)
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


pow_btn = Button(f2, text="x^", font="Segoe 17", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=pow_click)
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosbtn = Button(f2, text="cos", font="Segoe 18", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=cos_click)
cosbtn.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn4 = Button(f2, text="4", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=btn4_click)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(f2, text="5", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=btn5_click)
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(f2, text="6", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=btn6_click)
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnsub= Button(f2, text="-", font="Segoe 23", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=sub_click)
btnsub.pack(side=LEFT, expand=TRUE, fill=BOTH)



#Row3

f3=Frame(root)
f3.pack(expand=TRUE,fill=BOTH)


round_btn = Button(f3, text="round", font="Segoe 10 bold", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=round_click)
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(f3, text="ln", font="Segoe 18", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=in_click)
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

mod_btn = Button(f3, text="%", font="Segoe 21", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=mod_click)
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanbtn = Button(f3, text="tan", font="Segoe 18", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=tan_click)
tanbtn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(f3, text="1", font="Segoe 23", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=btn1_click)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(f3, text="2", font="Segoe 23", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=btn3_click)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(f3, text="3", font="Segoe 23", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=btn3_click)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)


btnmul = Button(f3, text="*", font="Segoe 23", relief=SUNKEN, bd=0,fg="white", bg="#333333",command=mul_click)
btnmul.pack(side=LEFT, expand=TRUE, fill=BOTH)


#row4


f4 = Frame(root)
f4.pack(expand=TRUE, fill=BOTH)



bl_btn = Button(f4, text=" ( ", font="Segoe 21", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=bl_click)
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(f4, text=" ) ", font="Segoe 21", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=bl_click)
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(f4, text=" • ", font="Segoe 21", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=dot_click)
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(f4, text="C", font="Segoe 23", relief=SUNKEN, bd=0,  fg="white", bg="#333333",command=clear_click)
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(f4, text="Del", font="Segoe 20", relief=SUNKEN, bd=0, fg="white", bg="#333333",command=del_click)
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(f4, text="0", font="Segoe 23", relief=SUNKEN, bd=0,  fg="white", bg="#333333",command=btn0_click)
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnequ = Button(f4, text="=", font="Segoe 23", relief=SUNKEN, bd=0 , fg="white", bg="#333333",command=equ_click)
btnequ.pack(side=LEFT, expand=TRUE, fill=BOTH)

btndiv = Button(f4, text="/", font="Segoe 23", relief=SUNKEN, bd=0,  fg="white", bg="#333333",command=div_click)
btndiv.pack(side=LEFT, expand=TRUE, fill=BOTH)
disp.bind("<Return>", equ_click)
disp.bind("<Escape>", clear_click)
disp.bind("<Key-1>", keyevent)
disp.bind("<Key-2>", keyevent)
disp.bind("<Key-3>", keyevent)
disp.bind("<Key-4>", keyevent)
disp.bind("<Key-5>", keyevent)
disp.bind("<Key-6>", keyevent)
disp.bind("<Key-7>", keyevent)
disp.bind("<Key-8>", keyevent)
disp.bind("<Key-9>", keyevent)
disp.bind("<Key-0>", keyevent)
disp.bind("<Key-.>", keyevent)
disp.insert(0, '0')
disp.focus_set()


root.mainloop()