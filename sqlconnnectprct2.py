import mysql.connector as msc
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import *

pswd_dict={'9931':"RLL13",'9983':"HFY54",'1':"1"}

def customer():
	cust_win=tk.Toplevel(win)
	cust_win.geometry('600x400')
	cust_win.resizable(width=False,height=False)
	cust_label=tk.Label(cust_win,text="Do customer operations here")
	cust_exit=tk.Button(cust_win,text="Exit",command=cust_win.destroy)
	cust_label.pack()
	cust_exit.pack()

def c_insert():
	e_cid=StringVar()
	e_cfname=StringVar()
	e_clname=StringVar()
	e_crno=StringVar()
	e_cphno=StringVar()
	e_cstat=StringVar()
	cid=e_cid.get()
	cfname=e_cfname.get()
	clname=e_clname.get()
	crno=e_crno.get()
	cphno=e_cphno.get()
	cstat=e_cstat.get()
	print("1",cid,"2",cfname,"3",clname,"4",crno,"5",cphno,"6",cstat)
	if (cid=="" or cfname=="" or crno=="" or clname=="" or cphno=="" or cstat==""):
		tkmsg.showinfo("Insert Status","All Fields are Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("insert into customer values('"+ cid +"','"+ cfname +"','"+ clname +"','"+ crno +"','"+ cphno +"','"+ cstat +"')")
		curr.execute("commit")   
		e_cid.delete(0,'end')
		e_cfname.delete(0,'end')
		e_crno.delete(0,'end')
		e_clname.delete(0,'end')
		e_cphno.delete(0,'end')
		e_cstat.delete(0,'end')
		tkmsg.showinfo("Insert Status","Insertion Successfull")
		con.close()

def c_delete():
	print("H")

def c_update():
	print("H")

def staff_operations():
	global staff_op
	staff_op=tk.Toplevel(staff_win)
	staff_op.geometry('600x400')
	staff_op.resizable(width=False,height=False)
	staff_oper=tk.Label(staff_op,text="Customer Details",font=('Helvetica 15 underline')).place(x=20,y=20)
	#staff_oper.pack()
	#Customer Details
	global e_cid
	global e_cfname
	global e_clname
	global e_crno
	global e_cphno
	global e_cstat
	cid=tk.IntVar()
	#e_cid=tk.IntVar()
	cfname=StringVar()
	cid=tk.Label(staff_op,text='Customer ID',font=("bold",10)).place(x=20,y=50)
	e_cid=tk.Entry(staff_op,textvariable=cid).place(x=150,y=50)
	cfname=tk.Label(staff_op,text='First Name',font=("bold",10)).place(x=20,y=80)
	e_cfname=tk.Entry(staff_op).place(x=150,y=80)
	clname=tk.Label(staff_op,text='Last Name',font=("bold",10)).place(x=20,y=110)
	e_clname=tk.Entry(staff_op).place(x=150,y=110)
	crno=tk.Label(staff_op,text='Room No:',font=("bold",10)).place(x=20,y=140)
	e_crno=tk.Entry(staff_op).place(x=150,y=140)
	cphno=tk.Label(staff_op,text='Phone No:',font=("bold",10)).place(x=20,y=170)
	e_cphno=tk.Entry(staff_op).place(x=150,y=170)
	cstat=tk.Label(staff_op,text='Status (In/Out)',font=("bold",10)).place(x=20,y=200)
	e_cstat=tk.Entry(staff_op).place(x=150,y=200)
	insert=tk.Button(staff_op,text="Insert Customer",command=c_insert).place(x=20,y=250)
	delete=tk.Button(staff_op,text="Delete Customer",command=c_delete).place(x=180,y=250)
	update=tk.Button(staff_op,text="Update Customer",command=c_update).place(x=340,y=250)		
	staff_exit=tk.Button(staff_op,text="Exit",command=staff_op.destroy).place(x=520,y=360)

def login_verify():
	user1=user.get()
	pswd1=pswd.get()
	user_entry.delete(0, END)
	pswd_entry.delete(0, END)
	if user1 in pswd_dict and pswd1==pswd_dict[user1]:
		staff_operations()
	else:
		verify=Label(staff_win,text="Incorrect staff id or password")
		try_again=Label(staff_win,text="Try Again")
		verify.pack()
		try_again.pack()

def staff():
	global staff_win
	staff_win=tk.Toplevel(win)
	staff_win.geometry('600x400')
	staff_win.resizable(width=False,height=False)
	#staff_label=tk.Label(staff_win,text="This is the staff page")
	global user
	global pswd
	global user_entry
	global pswd_entry
	user=StringVar()
	pswd=StringVar()
	user_label=tk.Label(staff_win,text='Username ')
	user_label.pack()
	user_entry=tk.Entry(staff_win,textvariable=user)
	user_entry.pack()
	pswd_label=tk.Label(staff_win,text='Password ')
	pswd_label.pack()
	pswd_entry=tk.Entry(staff_win,textvariable=pswd,show='*')
	pswd_entry.pack()
	login_button=tk.Button(staff_win,text='Log in',command=login_verify)
	login_button.pack()
	staff_exit=tk.Button(staff_win,text="Exit",command=staff_win.destroy)
	#staff_label.pack()
	staff_exit.pack()

win=tk.Tk()
win.geometry('600x400')
win.resizable(width=False,height=False)
cust_button=tk.Button(win,text="go to customer page",command=customer)
staff_button=tk.Button(win,text="go to staff page",command=staff)
cust_button.pack()
staff_button.pack()
win.mainloop()
