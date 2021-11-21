import mysql.connector as msc
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import *

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
	List.delete(0,List.size())
	data="room_no   room_id    room_status"
	List.insert(List.size()+1,data)
	for i in rows:
		data=str(i[0])+"              "+str(i[1])+"            "+i[2]
		List.insert(List.size()+1, data)
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

def room():
	global room_win
	room_win=tk.Toplevel(staff_op)
	room_win.geometry('700x400')
	room_win.resizable(width=False,height=False)

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

	roomview=tk.Button(room_win,text='room details',command=room_view)
	roomview.place(x=20,y=140)
	roomupdate=tk.Button(room_win,text='room update',comman=room_update)
	roomupdate.place(x=120,y=140)
	global List
	List=tk.Listbox(room_win,height=20,width=30)
	List.place(x=500,y=30)

def staff_operations():
	global staff_op
	staff_op=tk.Toplevel(staff_win)
	staff_op.geometry('600x400')
	staff_op.resizable(width=False,height=False)
	staff_oper=tk.Label(staff_op,text="Do staff operations here")
	staff_oper.pack()
	room_button=tk.Button(staff_op,text="room details",command=room)
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
		verify=Label(staff_win,text="Incorrect staff_id or password")
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
