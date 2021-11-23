import mysql.connector as msc
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import *
from tkinter import ttk

import mysql.connector as ms
mydb =  ms.connect(host="localhost",user="root",passwd="system",database="HotelDB")
cur = mydb.cursor()
cur.execute("Select * from password_hotel")
data=cur.fetchall()
pswd_dict={}
for i in data:
	pswd_dict[str(i[0])]=i[1]
print(pswd_dict)

def customer():
	cust_win=tk.Toplevel(win)
	cust_win.geometry('600x400')
	cust_win.resizable(width=False,height=False)
	cust_label=tk.Label(cust_win,text="Do customer operations here")
	cust_exit=tk.Button(cust_win,text="Exit",command=cust_win.destroy)
	cust_label.pack()
	cust_exit.pack()

def room_view():
	con=msc.connect(host="localhost",user="root",passwd="system",database="HotelDB")
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
		con=msc.connect(host="localhost",user="root",password="system",database="HotelDB")
		curr=con.cursor()
		curr.execute("update room set room_status='"+ room_status +"' where room_no='"+ room_no +"'")
		curr.execute("commit")
		i_room_no.delete(0,END)
		i_room_status.delete(0,END)
		tkmsg.showinfo("Update Status","Updation Successfull")
		con.close()

def staff_view():
	con=msc.connect(host="localhost",user="root",passwd="system",database="HotelDB")
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
		con=msc.connect(host="localhost",user="root",password="system",database="HotelDB")
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
		con=msc.connect(host="localhost",user="root",password="system",database="HotelDB")
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
		con=msc.connect(host="localhost",user="root",password="system",database="HotelDB")
		curr=con.cursor()
		curr.execute("delete from staff where staff_id='"+staff_id+"'")
		curr.execute("commit")
		i_staff_id.delete(0,END)
		tkmsg.showinfo("Delete Status","Deletion Successfull")
		con.close()

def room():
	global room_win
	room_win=tk.Toplevel(staff_op)
	room_win.geometry('800x500')
	room_win.resizable(width=False,height=False)

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

	staff_exit=tk.Button(room_win,text="Exit",command=room_win.destroy)
	staff_exit.pack()

	global List
	List=ttk.Treeview(room_win,height=10,columns=("c1","c2","c3","c4"))
	List.column("#0",width=0,stretch=NO)
	List.column("#1",anchor=CENTER,width=80,stretch=NO)
	List.column("#2",anchor=CENTER,width=80,stretch=NO)
	List.column("#3",anchor=CENTER,width=80,stretch=NO)
	List.column("#4",anchor=CENTER,width=80)
	List.place(x=380,y=30)

def staff_operations():
	global staff_op
	staff_op=tk.Toplevel(staff_win)
	staff_op.geometry('600x400')
	staff_op.resizable(width=False,height=False)
	staff_oper=tk.Label(staff_op,text="Do staff operations here")
	staff_oper.pack()
	room_button=tk.Button(staff_op,text="Hotel details",command=room)
	room_button.pack()
	staff_exit=tk.Button(staff_op,text="Exit",command=staff_op.destroy)
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
