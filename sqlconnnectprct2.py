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
	cid=i_cid.get()
	cfname=i_cfname.get()
	clname=i_clname.get()
	crno=i_crno.get()
	cphno=i_cphno.get()
	cstat=i_cstat.get()
	#print("1",cid,"2",cfname,"3",clname,"4",crno,"5",cphno,"6",cstat)
	if (cid=="" or cfname=="" or crno=="" or clname=="" or cphno=="" or cstat==""):
		tkmsg.showinfo("Insert Status","All Fields are Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("insert into customer values('"+ cid +"','"+ cfname +"','"+ clname +"','"+ crno +"','"+ cphno +"','"+ cstat +"')")
		curr.execute("commit")   
		i_cid.delete(0,'end')
		i_cfname.delete(0,'end')
		i_crno.delete(0,'end')
		i_clname.delete(0,'end')
		i_cphno.delete(0,'end')
		i_cstat.delete(0,'end')
		tkmsg.showinfo("Insert Status","Insertion Successfull")
		con.close()
		
def c_delete():
	cid=i_cid.get()
	if(cid==""):
		tkmsg.showinfo("Delete Status","Field is Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("delete from customer where customer_id='"+ cid +"'")
		curr.execute("commit")
		i_cid.delete(0,'end')
		tkmsg.showinfo("Delete Status","Deletion Successfull")
		con.close()

def c_update():
	cid=i_cid.get()
	cstat=i_cstat.get()
	if (cid=="" or cstat==""):
		tkmsg.showinfo("Update Status","Fields are Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("update customer set cust_status='"+ cstat +"' where customer_id='"+ cid +"'")
		curr.execute("commit")
		i_cid.delete(0,'end')
		i_cstat.delete(0,'end')
		tkmsg.showinfo("Update Status","Updation Successfull")
		con.close()

def c_show():
	con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
	curr=con.cursor()
	curr.execute("select * from customer ")
	rows=curr.fetchall()
	List.delete(0,List.size())
	data="Cust_ID     FirstName     LastName     RoomNo     PhoneNo     Status"
	List.insert(List.size()+1, data)
	for i in rows:
		data=str(i[0])+"       "+i[1]+"       "+i[2]+"       "+str(i[3])+"       "+i[4]+"       "+i[5]
		List.insert(List.size()+1, data)
	con.close()

def staff_operations():
	global staff_op
	staff_op=tk.Toplevel(staff_win)
	staff_op.geometry('1200x800')
	staff_op.resizable(width=False,height=False)
	staff_oper=tk.Label(staff_op,text="Customer Details",font=('Helvetica 15 underline')).place(x=20,y=20)
	#staff_oper.pack()
	#Customer Details
	global i_cid
	global i_cfname
	global i_clname
	global i_crno
	global i_cphno
	global i_cstat
	#cid=tk.IntVar()
	#e_cid=tk.IntVar()
	#cfname=StringVar()
	#e_cid=StringVar
	#e_cfname=StringVar
	#e_clname=StringVar
	#e_crno=StringVar
	#e_cphno=StringVar
	#e_cstat=StringVar
	cid=tk.Label(staff_op,text='Customer ID',font=("bold",10))
	cid.place(x=20,y=50)
	i_cid=tk.Entry(staff_op)
	i_cid.place(x=150,y=50)
	cfname=tk.Label(staff_op,text='First Name',font=("bold",10))
	cfname.place(x=20,y=80)
	i_cfname=tk.Entry(staff_op)
	i_cfname.place(x=150,y=80)
	clname=tk.Label(staff_op,text='Last Name',font=("bold",10))
	clname.place(x=20,y=110)
	i_clname=tk.Entry(staff_op)
	i_clname.place(x=150,y=110)
	crno=tk.Label(staff_op,text='Room No:',font=("bold",10))
	crno.place(x=20,y=140)
	i_crno=tk.Entry(staff_op)
	i_crno.place(x=150,y=140)
	cphno=tk.Label(staff_op,text='Phone No:',font=("bold",10))
	cphno.place(x=20,y=170)
	i_cphno=tk.Entry(staff_op)
	i_cphno.place(x=150,y=170)
	cstat=tk.Label(staff_op,text='Status (In/Out)',font=("bold",10))
	cstat.place(x=20,y=200)
	i_cstat=tk.Entry(staff_op)
	i_cstat.place(x=150,y=200)
	insert=tk.Button(staff_op,text="Insert Customer",command=c_insert)
	insert.place(x=20,y=250)
	delete=tk.Button(staff_op,text="Delete Customer",command=c_delete)
	delete.place(x=180,y=250)
	update=tk.Button(staff_op,text="Update Customer Status",command=c_update)
	update.place(x=20,y=300)
	global List
	List=tk.Listbox(staff_op,height=40,width=100)
	List.place(x=350,y=20)
	Display=tk.Button(staff_op,text="Display Customer",command=c_show)
	Display.place(x=20,y=350)		
	staff_exit=tk.Button(staff_op,text="Exit",command=staff_op.destroy)
	staff_exit.place(x=1120,y=760)

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
