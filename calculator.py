from tkinter import *
root=Tk()
root.title("Calculator")
ent=Entry(root, width=50, borderwidth=3, bg="skyblue")
ent.grid(row=0, column=0, columnspan=5)

def button_click(number):
	current=ent.get()
	ent.delete(0, END)
	ent.insert(0, str(current)+str(number))


num1=0
op=""

def add():
	global num1
	global op
	op="+"
	num1=ent.get()
	ent.delete(0, END)

def sub():
	global num1
	global op
	op="-"
	num1=ent.get()
	ent.delete(0, END)

def mult():
	global num1
	global op
	op="x"
	num1=ent.get()
	ent.delete(0, END)

def div():
	global num1
	global op
	op="/"
	num1=ent.get()
	ent.delete(0, END)

def equal():
	num2=ent.get()
	ent.delete(0, END)
	if op=="+":
		ent.insert(0, str(int(num1)+int(num2)))
	elif op=="-":
		ent.insert(0, int(num1)-int(num2))
	elif op=="x":
		ent.insert(0, int(num1)*int(num2))
	elif op=="/":
		ent.insert(0, int(num1)//int(num2))

key1=Button(root, text="1",width=10, command= lambda:button_click(1)).grid(row=1, column=0)
key2=Button(root, text="2",width=10, command= lambda:button_click(2)).grid(row=1, column=1)
key3=Button(root, text="3",width=10, command= lambda:button_click(3)).grid(row=1, column=2)
key4=Button(root, text="4",width=10, command= lambda:button_click(4)).grid(row=2, column=0)
key5=Button(root, text="5",width=10, command= lambda:button_click(5)).grid(row=2, column=1)
key6=Button(root, text="6",width=10, command= lambda:button_click(6)).grid(row=2, column=2)
key7=Button(root, text="7",width=10, command= lambda:button_click(7)).grid(row=3, column=0)
key8=Button(root, text="8",width=10, command= lambda:button_click(8)).grid(row=3, column=1)
key9=Button(root, text="9",width=10, command= lambda:button_click(9)).grid(row=3, column=2)
key0=Button(root, text="0",width=5, command= lambda:button_click(0)).grid(row=3, column=3)
addbut=Button(root, text="+", command=add, width=5).grid(row=1, column=3)
subbut=Button(root, text="-", command=sub,width=5).grid(row=1, column=4)
multbut=Button(root, text="x", command=mult,width=5).grid(row=2, column=3)
divbut=Button(root, text="/", command=div,width=5).grid(row=2, column=4)
equalbut=Button(root, text="=",width=5, command=equal).grid(row=3, column=4)

root.mainloop()