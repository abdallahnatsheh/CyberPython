from tkinter import *

top = Tk()
top.title("Calculator")
top.minsize(300,300)
#-----FirstNumber-------------
number1label = Label(text="First Number",fg="white",bg="black")
number1label.pack()
number1Entry= Entry()
number1Entry.pack()
#----------------------------------

#-----SecondNumber-----------------
number2label = Label(text="First Number",fg="white",bg="black")
number2label.pack()
number2Entry= Entry()
number2Entry.pack()
#----------------------------------
def addNumber():
    num1 = int(number1Entry.get())
    num2 = int(number2Entry.get())
    result = num1+num2
    resultlabel= Label(text="the result it : "+str(result))
    resultlabel.pack()

#-----AddButton-----------------
add = Button(text="Add",bg="yellow",command=addNumber)
add.pack()


top.mainloop()
