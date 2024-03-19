from tkinter import *

root=Tk()
root.title('My Test')
root.geometry('300x600')
root.resizable(width=False,height=False)

head=Label(root,text='Calculator',font=('normal',20))
head.grid(padx=90,row=0,column=0,columnspan=5)

entry=Text(root,width=30,height=2,bd=2)
entry.grid(pady=20,padx=30,columnspan=5)

class Calco:
    def __init__(self):
        self.num1=None
        self.num2=None
        self.action=None

    def clear(self):
        entry.delete(0.0,END)

    def click(self,num):
        entry.insert('end',num)

    def add(self):
        self.num1=int(entry.get(0.0,END))
        entry.delete(0.0,END)
        self.action='addition'

    def sub(self):
        self.num1=int(entry.get(0.0,END))
        entry.delete(0.0,END)
        self.action='subtraction'

    def mul(self):
        self.num1=int(entry.get(0.0,END))
        entry.delete(0.0,END)
        self.action='multiplication'

    def div(self):
        self.num1=int(entry.get(0.0,END))
        entry.delete(0.0,END)
        self.action='division'

    def equal(self):
        self.num2=int(entry.get(0.0,END))
        entry.delete(0.0,END)
        if self.action=='addition':
            num=self.num1+self.num2
            entry.insert(0.0,num)
        elif self.action=='subtraction':
            num=self.num1-self.num2
            entry.insert(0.0,num)
        elif self.action=='multiplication':
            num=self.num1*self.num2
            entry.insert(0.0,num)
        elif self.action=='division':
            num=self.num1/self.num2
            entry.insert(0.0,num)

oCalco=Calco()

button9=Button(root,text=9,width=8,height=3,bd=3,command=lambda:oCalco.click(9)).grid(row=2,column=0,padx=20,pady=10)
button8=Button(root,text=8,width=8,height=3,bd=3,command=lambda:oCalco.click(8)).grid(row=2,column=1,padx=5)
button7=Button(root,text=7,width=8,height=3,bd=3,command=lambda:oCalco.click(7)).grid(row=2,column=2,padx=5)
button6=Button(root,text=6,width=8,height=3,bd=3,command=lambda:oCalco.click(6)).grid(row=3,column=0,padx=20,pady=10)
button5=Button(root,text=5,width=8,height=3,bd=3,command=lambda:oCalco.click(5)).grid(row=3,column=1,padx=5)
button4=Button(root,text=4,width=8,height=3,bd=3,command=lambda:oCalco.click(4)).grid(row=3,column=2,padx=5)
button3=Button(root,text=3,width=8,height=3,bd=3,command=lambda:oCalco.click(3)).grid(row=4,column=0,padx=20,pady=10)
button2=Button(root,text=2,width=8,height=3,bd=3,command=lambda:oCalco.click(2)).grid(row=4,column=1,padx=5)
button1=Button(root,text=1,width=8,height=3,bd=3,command=lambda:oCalco.click(1)).grid(row=4,column=2,padx=5)
button0=Button(root,text=0,width=8,height=3,bd=3,command=lambda:oCalco.click(0)).grid(row=5,column=0,padx=20,pady=10)
button_add=Button(root,text='+',width=8,height=3,bd=3,command=lambda:oCalco.add()).grid(row=5,column=1,padx=5)
button_sub=Button(root,text='-',width=8,height=3,bd=3,command=lambda:oCalco.sub()).grid(row=5,column=2,padx=5)
button_mul=Button(root,text='*',width=8,height=3,bd=3,command=lambda:oCalco.mul()).grid(row=6,column=0,padx=20,pady=10)
button_div=Button(root,text='/',width=8,height=3,bd=3,command=lambda:oCalco.div()).grid(row=6,column=1,padx=5)
button_eql=Button(root,text='=',width=8,height=3,bd=3,command=lambda:oCalco.equal()).grid(row=6,column=2,padx=5)
button_clr=Button(root,text='clear',width=35,height=3,bd=3,command=lambda:oCalco.clear()).grid(row=7,columnspan=5,pady=10,padx=20)

root.mainloop()