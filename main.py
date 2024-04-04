import os
from tkinter import *
import tkinter as tk
import math



fen = Tk()
fen.title("Calculator")
fen.geometry("607x548")
fen.configure(background="ivory3")
#Prevent maximum window
fen.resizable(False,False)

#Entering Values   
text = tk.Entry(fen, font = ("Comic Sans MS",60),bg = "#66CDAA",width=13)
text.place(x=1,y=1)
text.focus()

#Operations
def Equal():
    expression = text.get()
    expression = expression.replace('x', '*')
    expression = expression.replace('÷', '/')
    if "√" in expression:
        b=expression.replace("√","")
        c = float(b)
        expression = math.sqrt(c)
        text.delete(0,END)
        text.insert(0,expression)
    elif "%" in expression:
        a = expression.replace("%", "/100")
        b = eval(a)
        expression = text.delete(0,END)
        text.insert(0, b)
    elif "!" in expression:
        b = expression.replace("!", "")
        c = int(b)
        expression = math.factorial(c)
        text.delete(0,END)
        text.insert(0,expression)                
    else:
        text.delete(0, END)
        text.insert(0, eval(expression))
    
#Buttons
abs1 = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button1.png"

Button1 = PhotoImage(file= "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button1.png")
but1 = Button(image=Button1, command = lambda: text.insert(END, '1'))
but1.place(x=0,y=123)


Button2 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button2.png")
but2 = Button(image=Button2, command =lambda: text.insert(END, '2') )
but2.place(x=100, y = 123)

Button3 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button3.png")
but3 = Button(image = Button3, command = lambda: text.insert(END, '3'))
but3.place(x=200, y=123)

Button4 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button4.png")
but4 = Button(image = Button4, command = lambda: text.insert(END, '4'))
but4.place(x=0, y = 225)

Button5 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Screenshot 2024-01-15 220220.png")
but5 = Button(image = Button5, command = lambda: text.insert(END, '5'))
but5.place(x=100, y = 225)

Button6 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button6.png")
but6 = Button(image = Button6, command = lambda: text.insert(END, '6'))
but6.place(x=200, y = 225)

Button7 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button7.png")
but7 = Button(image = Button7, command = lambda: text.insert(END, '7'))
but7.place(x=0, y = 332)

Button8 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button8.png")
but6 = Button(image = Button8, command = lambda: text.insert(END, '8'))
but6.place(x=100, y = 332)

Button9 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Screenshot 2024-01-15 225718.png")
but6 = Button(image = Button9, command = lambda: text.insert(END, '9'))
but6.place(x=200, y = 332)

Button0 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button0.png")
but0 = Button(image = Button0, command = lambda: text.insert(END, '0'))
but0.place(x=0,y=440)

Button00 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Button00.png")
but00 = Button(image = Button00, command = lambda: text.insert(END, '00'))
but00.place(x=100,y=440)

Buttondot = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Screenshot 2024-01-15 231130.png")
but6 = Button(image = Buttondot, command = lambda: text.insert(END, '.'))
but6.place(x=200, y = 440)

ButtonAdd = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\ButtonAdd.png")
butadd = Button(image = ButtonAdd, command = lambda: text.insert(END, '+'))
butadd.place(x=300, y = 331)

ButtonSub = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\SubButton.png")
butsub = Button(image = ButtonSub, command =lambda: text.insert(END, '-'))
butsub.place(x=400, y = 225)


ButtonDiv = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\DivisionButton.png")
butdiv = Button(image = ButtonDiv, command = lambda: text.insert(END, '÷'))
butdiv.place(x=504, y = 123)

ButtonMul = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Screenshot 2024-01-16 132600.png")
butmul = Button(image = ButtonMul, command = lambda: text.insert(END, 'x'))
butmul.place(x=300, y = 225)

'''
ButtonPerc = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Screenshot 2024-01-16 144652.png")
butperc = Button(image = ButtonPerc, command = lambda: text.insert(END, '%'))
butperc.place(x=504, y = 123)
'''

ButtonSqRt = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\SqrtRootButton.png")
butsqrt = Button(image = ButtonSqRt, command = lambda: text.insert(END, '√'))
butsqrt.place(x=400, y = 123)

ButtonEqual = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Equal Image.png")
butEq = Button(image = ButtonEqual, command = Equal)
butEq.place(x=400,y=331)

ButtonC = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\CBUtton.png")
butC = Button(image = ButtonC, command = lambda: text.delete(0,END))
butC.place(x=300, y= 123)

ButtonBr1 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\bracketInward.png")
butbr1 = Button(image = ButtonBr1, command = lambda: text.insert(END, "("))
butbr1.place(x=504,y=225)

ButtonBr2 = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Bracket2.png")
butbr2 = Button(image = ButtonBr2, command = lambda: text.insert(END, ")"))
butbr2.place(x=504,y=331)

Factorial = PhotoImage(file = "C:\\Users\\waqar\\Desktop\\python homework 2\\Python Exercises\\Factorial.png")
factorial = Button(image = Factorial, command = lambda: text.insert(END, "!"))
factorial.place(x=504, y=438)

fen.mainloop()



