import mysql.connector as msc
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import *
from tkinter import ttk

import mysql.connector as ms
mydb =  ms.connect(host="localhost",user="root",passwd="Password123#@!",database="HotelDB")
cur = mydb.cursor()
cur.execute("Select * from password_hotel")
data=cur.fetchall()
pswd_dict={}
for i in data:
	pswd_dict[str(i[0])]=i[1]

def show_win2():
   win.deiconify()
   cust_win.destroy()

def customer():
	global cust_win
	cust_win=tk.Toplevel(win)
	cust_win.geometry('600x400')
	cust_win.resizable(width=False,height=False)
	win.withdraw()
	tree=ttk.Treeview(cust_win,height=10,columns=("c1","c2","c3"))
	tree.column("#0",width=0,stretch=NO)
	tree.column("#1",anchor=CENTER,width=80,stretch=NO)
	tree.heading("#1",text="Room type")
	tree.column("#2",anchor=CENTER,width=80,stretch=NO)
	tree.heading("#2",text="Cost")
	tree.column("#3",anchor=CENTER,width=80)
	tree.heading("#3",text="Availability")
	tree.pack()

	con=msc.connect(host="localhost",user="root",passwd="Password123#@!",database="HotelDB")
	curr=con.cursor()
	curr.execute("select room_type,cost,room_remaining from hotel")
	rows=curr.fetchall()
	for item in tree.get_children():
		tree.delete(item)
	for i in rows:
		data=(str(i[0]),str(i[1]),str(i[2]))
		tree.insert("","end",values=data)
	con.close()
	
	cust_exit=tk.Button(cust_win,text="Exit",command=show_win2)
	cust_exit.pack()

def room_view():
	con=msc.connect(host="localhost",user="root",passwd="Password123#@!",database="HotelDB")
	curr=con.cursor()
	curr.execute("select * from room where room_status='Available'")
	rows=curr.fetchall()
	for item in List.get_children():
		List.delete(item)
	data=("room_no","room_id","room_status")
	List.insert("","end",values=data)
	for i in rows:
		data=(str(i[0]),str(i[1]),str(i[2]))
		List.insert("","end",values=data)
	con.close()

def room_update():
	room_no=i_room_no.get()
	room_status=i_room_status.get()
	if(room_no=="" or room_status==""):
		tkmsg.showinfo("Update Status","Field is Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("update room set room_status='"+ room_status +"' where room_no='"+ room_no +"'")
		curr.execute("commit")
		i_room_no.delete(0,END)
		i_room_status.delete(0,END)
		tkmsg.showinfo("Update Status","Updation Successfull")
		con.close()

def staff_view():
	con=msc.connect(host="localhost",user="root",passwd="Password123#@!",database="HotelDB")
	curr=con.cursor()
	curr.execute("select * from staff")
	rows=curr.fetchall()
	for item in List.get_children():
		List.delete(item)
	data=("staff id","staff name","salary","Designation")
	List.insert("","end",values=data)
	for i in rows:
		data=(str(i[0]),str(i[1]),str(i[2]),str(i[3]))
		List.insert("","end",values=data)
	con.close()

def staff_update():
	staff_id=i_staff_id.get()
	salary=i_salary.get()
	if(staff_id=="" or salary==""):
		tkmsg.showinfo("Update Status","Field is Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("update staff set salary='"+ salary +"' where staff_id='"+ staff_id +"'")
		curr.execute("commit")
		i_staff_id.delete(0,END)
		i_salary.delete(0,END)
		tkmsg.showinfo("Update Status","Updation Successfull")
		con.close()

def staff_insert():
	staff_id1=i_staff_id.get()
	staff_name1=i_staff_name.get()
	salary1=i_salary.get()
	designation1=i_designation.get()
	if(staff_id1=="" or salary1=="" or staff_name1=="" or designation1==""):
		tkmsg.showinfo("Insertion Status","Field is Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("insert into staff values('"+staff_id1+"','"+staff_name1+"','"+salary1+"','"+designation1+"')")
		curr.execute("commit")
		i_staff_id.delete(0,END)
		i_staff_name.delete(0,END)
		i_salary.delete(0,END)
		i_designation.delete(0,END)
		tkmsg.showinfo("Insertion Status","Insertion Successfull")
		con.close()

def staff_delete():
	staff_id=i_staff_id.get()
	if(staff_id==""):
		tkmsg.showinfo("Delete Status","Field is Mandatory")
	else:
		con=msc.connect(host="localhost",user="root",password="Password123#@!",database="HotelDB")
		curr=con.cursor()
		curr.execute("delete from staff where staff_id='"+staff_id+"'")
		curr.execute("commit")
		i_staff_id.delete(0,END)
		tkmsg.showinfo("Delete Status","Deletion Successfull")
		con.close()

def show_staff_op2():
   staff_op.deiconify()
   room_win.destroy()

def room():
	global room_win
	room_win=tk.Toplevel(staff_op)
	room_win.geometry('850x550')
	room_win.resizable(width=False,height=False)
	staff_op.withdraw()
	#Room details
	global i_room_no
	global i_room_status
	room_no=IntVar
	room_status=StringVar
	t_room_no=tk.Label(room_win,text='Enter room_no')
	t_room_no.place(x=20,y=30)
	i_room_no=tk.Entry(room_win,textvariable=room_no)
	i_room_no.place(x=150,y=30)
	t_room_status=tk.Label(room_win,text='Enter room status')
	t_room_status.place(x=20,y=60)
	i_room_status=tk.Entry(room_win,textvariable=room_status)
	i_room_status.place(x=150,y=60)

	#staff details
	global i_staff_id
	global i_staff_name
	global i_salary
	global i_designation
	staff_id=IntVar
	staff_name=StringVar
	salary=IntVar
	designation=StringVar
	t_staff_id=tk.Label(room_win,text='Enter staff id')
	t_staff_id.place(x=20,y=200)
	i_staff_id=tk.Entry(room_win,textvariable=staff_id)
	i_staff_id.place(x=150,y=200)
	t_staff_name=tk.Label(room_win,text='Enter staff name')
	t_staff_name.place(x=20,y=230)
	i_staff_name=tk.Entry(room_win,textvariable=staff_name)
	i_staff_name.place(x=150,y=230)
	t_salary=tk.Label(room_win,text='Enter salary')
	t_salary.place(x=20,y=260)
	i_salary=tk.Entry(room_win,textvariable=salary)
	i_salary.place(x=150,y=260)
	t_designation=tk.Label(room_win,text='Enter designation')
	t_designation.place(x=20,y=290)
	i_designation=tk.Entry(room_win,textvariable=designation)
	i_designation.place(x=150,y=290)

	roomview=tk.Button(room_win,text='room details',command=room_view)
	roomview.place(x=20,y=140)
	roomupdate=tk.Button(room_win,text='room update',comman=room_update)
	roomupdate.place(x=120,y=140)
	staffview=tk.Button(room_win,text='staff details',command=staff_view)
	staffview.place(x=20,y=320)
	staffupdate=tk.Button(room_win,text='staff salary update',command=staff_update)
	staffupdate.place(x=120,y=320)
	staffinsert=tk.Button(room_win,text='insert staff',command=staff_insert)
	staffinsert.place(x=260,y=320)
	staffdelete=tk.Button(room_win,text='delete staff',command=staff_delete)
	staffdelete.place(x=20,y=350)

	staff_exit=tk.Button(room_win,text="Exit",command=show_staff_op2)
	staff_exit.pack()

	global List
	List=ttk.Treeview(room_win,height=10,columns=("c1","c2","c3","c4"))
	List.column("#0",width=0,stretch=NO)
	List.column("#1",anchor=CENTER,width=80,stretch=NO)
	List.column("#2",anchor=CENTER,width=80,stretch=NO)
	List.column("#3",anchor=CENTER,width=80,stretch=NO)
	List.column("#4",anchor=CENTER,width=80)
	List.place(x=380,y=30)

def c_insert():
	cid=i_cid.get()
	cfname=i_cfname.get()
	clname=i_clname.get()
	crno=i_crno.get()
	cphno=i_cphno.get()
	cstat=i_cstat.get()
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

def c_tree():
	con=msc.connect(host="localhost",user="root",passwd="Password123#@!",database="HotelDB")
	curr=con.cursor()
	curr.execute("select * from customer")
	rows=curr.fetchall()
	for item in List1.get_children():
		List1.delete(item)
	for i in rows:
		data=(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]))
		List1.insert("","end",values=data)
	con.close()

def show_staff_op1():
   staff_op.deiconify()
   customer_op.destroy()

def customer_det():
	global customer_op
	customer_op=tk.Toplevel(staff_op)
	customer_op.geometry('1200x800')
	customer_op.resizable(width=False,height=False)
	customer_lab=tk.Label(customer_op,text="Customer Details",font=('Helvetica 15 underline'))
	customer_lab.place(x=20,y=20)
	staff_op.withdraw()
	global i_cid
	global i_cfname
	global i_clname
	global i_crno
	global i_cphno
	global i_cstat

	cid=tk.Label(customer_op,text='Customer ID',font=("bold",10))
	cid.place(x=20,y=50)
	i_cid=tk.Entry(customer_op)
	i_cid.place(x=150,y=50)
	cfname=tk.Label(customer_op,text='First Name',font=("bold",10))
	cfname.place(x=20,y=80)
	i_cfname=tk.Entry(customer_op)
	i_cfname.place(x=150,y=80)
	clname=tk.Label(customer_op,text='Last Name',font=("bold",10))
	clname.place(x=20,y=110)
	i_clname=tk.Entry(customer_op)
	i_clname.place(x=150,y=110)
	crno=tk.Label(customer_op,text='Room No:',font=("bold",10))
	crno.place(x=20,y=140)
	i_crno=tk.Entry(customer_op)
	i_crno.place(x=150,y=140)
	cphno=tk.Label(customer_op,text='Phone No:',font=("bold",10))
	cphno.place(x=20,y=170)
	i_cphno=tk.Entry(customer_op)
	i_cphno.place(x=150,y=170)
	cstat=tk.Label(customer_op,text='Status (In/Out)',font=("bold",10))
	cstat.place(x=20,y=200)
	i_cstat=tk.Entry(customer_op)
	i_cstat.place(x=150,y=200)
	insert=tk.Button(customer_op,text="Insert Customer",command=c_insert)
	insert.place(x=20,y=250)
	delete=tk.Button(customer_op,text="Delete Customer",command=c_delete)
	delete.place(x=180,y=250)
	update=tk.Button(customer_op,text="Update Customer Status",command=c_update)
	update.place(x=20,y=300)
	global List1
	List1=ttk.Treeview(customer_op,column=("c1", "c2", "c3","c4","c5","c6"), show='headings', height=15)
	List1.column("# 1", anchor=CENTER,width=100)
	List1.heading("# 1", text="Cust_ID")
	List1.column("# 2", anchor=CENTER,width=100)
	List1.heading("# 2", text="FName")
	List1.column("# 3", anchor=CENTER,width=100)
	List1.heading("# 3", text="LName")
	List1.column("# 4", anchor=CENTER,width=100)
	List1.heading("# 4", text="RoomNo")
	List1.column("# 5", anchor=CENTER,width=100)
	List1.heading("# 5", text="PhoneNo")
	List1.column("# 6", anchor=CENTER,width=100)
	List1.heading("# 6", text="Status")
	List1.place(x=350,y=20)
	Display=tk.Button(customer_op,text="Display Customer",command=c_tree)
	Display.place(x=20,y=350)		
	cust_exit=tk.Button(customer_op,text="Exit",command=show_staff_op1)
	cust_exit.place(x=1020,y=700)

def show_staff_win():
   staff_win.deiconify()
   staff_op.destroy()

def staff_operations():
	global staff_op
	staff_op=tk.Toplevel(staff_win)
	staff_op.geometry('600x400')
	staff_op.resizable(width=False,height=False)
	staff_oper=tk.Label(staff_op,text="Do staff operations here")
	staff_oper.pack()
	staff_win.withdraw()
	room_button=tk.Button(staff_op,text="Hotel details",command=room)
	room_button.pack()
	customer_button=tk.Button(staff_op,text="Customer details",command=customer_det)
	customer_button.pack()
	staff_exit=tk.Button(staff_op,text="back",command=show_staff_win)
	staff_exit.pack()

def login_verify():
	user1=user.get()
	pswd1=pswd.get()
	user_entry.delete(0, END)
	pswd_entry.delete(0, END)
	if user1 in pswd_dict and pswd1==pswd_dict[user1]:
		staff_operations()
	else:
		tkmsg.showinfo("Error","Incorrext staff id or password")

def show_win():
   win.deiconify()
   staff_win.destroy()

def staff():
	global staff_win
	staff_win=tk.Toplevel(win)
	staff_win.geometry('600x400')
	staff_win.resizable(width=False,height=False)
	win.withdraw()
	#staff_label=tk.Label(staff_win,text="This is the staff page")
	global user
	global pswd
	global user_entry
	global pswd_entry
	user=StringVar()
	pswd=StringVar()
	user_label=tk.Label(staff_win,text='Staff ID ')
	user_label.pack()
	user_entry=tk.Entry(staff_win,textvariable=user)
	user_entry.pack()
	pswd_label=tk.Label(staff_win,text='Password ')
	pswd_label.pack()
	pswd_entry=tk.Entry(staff_win,textvariable=pswd,show='*')
	pswd_entry.pack()
	login_button=tk.Button(staff_win,text='Log in',command=login_verify)
	login_button.pack()
	staff_back=tk.Button(staff_win, text="Back" ,command=show_win)
	staff_back.pack()


win=tk.Tk()
win.geometry('600x400')
win.resizable(width=False,height=False)
cust_button=tk.Button(win,text="Customer - Click here",command=customer)
staff_button=tk.Button(win,text="Staff - Click here",command=staff)
cust_button.pack()
staff_button.pack()
win.mainloop()
