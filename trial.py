import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
	sid=e_id.get()
	name=e_name.get()
	if(sid=="" or name==""):
		MessageBox.showinfo("Insert Status","All Fields are Mandatory")
	else:
		con=mysql.connect(host="localhost",user="root",password="Password123#@!",database="tkinter_test")
		curr=con.cursor()
		curr.execute("insert into stu values('"+ sid +"','"+ name +"')")
		curr.execute("commit")
		e_id.delete(0,'end')
		e_name.delete(0,'end')
		MessageBox.showinfo("Insert Status","Insertion Successfull")
		con.close()

def delete():
	sid=e_id.get()
	if(sid==""):
		MessageBox.showinfo("Delete Status","Field is Mandatory")
	else:
		con=mysql.connect(host="localhost",user="root",password="Password123#@!",database="tkinter_test")
		curr=con.cursor()
		curr.execute("delete from stu where sid='"+ sid +"'")
		curr.execute("commit")
		e_id.delete(0,'end')
		MessageBox.showinfo("Delete Status","Deletion Successfull")
		con.close()

def update():
	sid=e_id.get()
	name=e_name.get()
	if(sid=="" or name==""):
		MessageBox.showinfo("Update Status","Field is Mandatory")
	else:
		con=mysql.connect(host="localhost",user="root",password="Password123#@!",database="tkinter_test")
		curr=con.cursor()
		curr.execute("update stu set name='"+ name +"' where sid='"+ sid +"'")
		curr.execute("commit")
		e_id.delete(0,'end')
		e_name.delete(0,'end')
		MessageBox.showinfo("Update Status","Updation Successfull")
		con.close()
		
def fetch():
	sid=e_id.get()
	if(sid==""):
		MessageBox.showinfo("Fetch Status","Field is Mandatory")
	else:
		con=mysql.connect(host="localhost",user="root",password="Password123#@!",database="tkinter_test")
		curr=con.cursor()
		curr.execute("select * from stu where sid='"+ sid +"'")
		rows=curr.fetchall()
		for i in rows:
			e_name.insert(0,i[1])
		con.close()

def show():
	con=mysql.connect(host="localhost",user="root",password="Password123#@!",database="tkinter_test")
	curr=con.cursor()
	curr.execute("select * from stu ")
	rows=curr.fetchall()
	List.delete(0,List.size())
	data="ID     Name"
	List.insert(List.size()+1, data)
	for i in rows:
		data=str(i[0])+"       "+i[1]
		List.insert(List.size()+1, data)
	con.close()
	
win = tk.Tk()
win.title("Trial")
win.geometry("700x300")
#mylabel=tk.Label(win,text="Hello World",font=("ubuntu",60,"bold"), fg = "red" )
#mylabel.pack()
sid=tk.Label(win,text='Enter ID',font=("bold",10))
sid.place(x=20,y=30)
e_id=tk.Entry()
e_id.place(x=150,y=30)
name=tk.Label(win,text='Enter Name',font=("bold",10))
name.place(x=20,y=60)
e_name=tk.Entry()
e_name.place(x=150,y=60)
insert=tk.Button(win,text="Insert",font=("italic",10), bg="green",command=insert)
insert.place(x=20,y=140)
delete=tk.Button(win,text="Delete",font=("italic",10), bg="green",command=delete)
delete.place(x=120,y=140)
update=tk.Button(win,text="Update",font=("italic",10), bg="green",command=update)
update.place(x=220,y=140)
fetch=tk.Button(win,text="Fetch",font=("italic",10), bg="green",command=fetch)
fetch.place(x=320,y=140)
List=tk.Listbox(win)
List.place(x=520,y=30)
