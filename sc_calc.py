from tkinter import *
import math
import tkinter.messagebox

exp=""
l=[]
op=""
#===================================
def factorial(txt,val):
    global exp
    a = txt.get()
    txt.insert(1,val)
    n = int(a)
    f = 1
    c = n
    try:
        while c> 0:
            f = f*c
            c -= 1
        AC(txt)
        txt.insert(0, f)
    except:
        AC(txt)
        display.insert(0, "Error")
        
def get_exp(txt, val):
    global exp
    if exp=="":
        txt.delete(0,END)
        txt.insert(0,val)
    else:
        txt.insert(INSERT, val)
    exp += str(val)

def addop(txt, o):
    global exp,op
    if o=='sin' or o=='cos' or o=='tan' or o=='ln':
        exp=""
        txt.delete(0,END)
        txt.insert(0,o)
    elif exp=="":
        txt.delete(0,END)
        txt.insert(0,o)
    
    else:
        txt.insert(INSERT,o)
    op=o
    exp=str(exp)
    exp+=op

def AC(txt):
    global exp, op
    txt.delete(0, END)
    exp=""
    op = ""
    
def DEL(txt):
    global exp
    if len(str(exp))<=1:
        AC(txt)
    else:
        exp=str(exp)
        exp=exp[:-1]
        txt.delete(0, END)
        txt.insert(INSERT, exp)

def evaluate(txt):
    global l, exp, op
    txt.delete(0, END)
    if op=='+' or op=='-' or op=='*' or op=='/' or op=='%':
        ex=eval(str(exp))
    elif op=='ln':
        ex=eval("math.log(float(exp[3:-1]))")
    elif op == "^":
        l=exp.split('^')
        ex=eval("pow(float(l[0]),float(l[1]))")
    elif op=='sin':
        
        ex=eval("math.sin(math.radians(float(exp[4:-1])))")
    elif op=='cos':
        ex=eval("math.cos(math.radians(float(exp[4:-1])))")
    elif op=='tan':
        ex=eval("math.tan(math.radians(float(exp[4:-1])))")
        
    del l[:]
    exp=""
    exp=ex
    txt.insert(INSERT, exp)

#===================================
root=Tk()
root.title("scientific calc")
root.config(background="powder blue")
root.geometry("638x610")

calc=Frame(root)
calc.grid()

disp=Entry(calc,font=('calibri',20,'bold'),bg='powder blue',bd=20,width=28,justify=RIGHT)
disp.grid(row=0,column=0,columnspan=4)
disp.insert(0,'0')

numberpad='789456123'
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6,height=2,font=('calibri',20,'bold'),bg='black',
                          foreground='teal',bd=4,text=numberpad[i],
                          command=lambda x=str(numberpad[i]):get_exp(disp,x)))
        btn[i].grid(row=j,column=k,pady=1)
        i+=1
#======================================
undo=Button(calc, text="Del",width=6,height=2,font=('calibri',20,'bold'),foreground='red',bd=4,
           bg='powder blue',command=lambda:DEL(disp)).grid(row=1,column=1,pady=1)

clr=Button(calc, text="AC",width=6,height=2,font=('calibri',20,'bold'),foreground='red',bd=4,
           bg='powder blue',command=lambda:AC(disp)).grid(row=1,column=0)

sqroot=Button(calc, text='√',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue').grid(row=1,column=2,pady=5)

add=Button(calc, text='+',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda:addop(disp,'+')).grid(row=1,column=3)

sub=Button(calc, text='-',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda:addop(disp,'-')).grid(row=2,column=3)

mul=Button(calc, text='x',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda:addop(disp,'*')).grid(row=3,column=3)

div=Button(calc, text=chr(247),width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda:addop(disp,'/')).grid(row=4,column=3)

zero=Button(calc, text='0',command=lambda:get_exp(disp,'0'),width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black').grid(row=5,column=1)

dot=Button(calc, text='.',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda: get_exp(disp,'.')).grid(row=5,column=0)

pm=Button(calc, text=chr(177),width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue').grid(row=5,column=2)

res=Button(calc, text='=',width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='powder blue',command=lambda:evaluate(disp)).grid(row=5,column=3)

sine=Button(calc, text="sin",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'sin')).grid(row=1,column=4,pady=5)

cosine=Button(calc, text="cos",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'cos')).grid(row=2,column=4,pady=5)

tangent=Button(calc, text="tan",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'tan')).grid(row=3,column=4,pady=5)

lg=Button(calc, text="ln",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'ln')).grid(row=2,column=5,pady=5)

modulo=Button(calc, text="%",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'%')).grid(row=1,column=5,pady=5)

bo=Button(calc, text="(",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:get_exp(disp,'(')).grid(row=4,column=4,pady=5)

bc=Button(calc, text=")",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:get_exp(disp,')')).grid(row=4,column=5,pady=5)

fact=Button(calc, text="!",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:factorial(disp,'!')).grid(row=3,column=5,pady=5)

power=Button(calc, text="^",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black',command=lambda:addop(disp,'^')).grid(row=5,column=4,pady=5)

E=Button(calc, text="e",width=6,height=2,font=('calibri',20,'bold'),foreground='teal',bd=4,
           bg='black').grid(row=5,column=5,pady=5)


lbldisp=Label(calc,text="Sc Calc",font=('arial',30,'bold'),justify=CENTER)
lbldisp.grid(row=0,column=4,columnspan=2)

#======================================
def ex():
    e=tkinter.messagebox.askyesno("sc calc",'u sure u wnna exit?')
    if e>0:
        root.destroy()
        return

def sc():
    root.geometry("944x568")

def standard():
    root.geometry("500x580")

menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='standard',command=standard)
filemenu.add_command(label='scientific',command=sc)
filemenu.add_separator()
filemenu.add_command(label='exit',command=ex)

root.config(menu=menubar)
root.mainloop()
