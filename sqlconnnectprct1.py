
import tkinter as tk

def customer():
	cust_win=tk.Toplevel(win)
	cust_win.geometry('600x400')
	cust_win.resizable(width=False,height=False)
	cust_label=tk.Label(cust_win,text="This is the customer page")
	cust_exit=tk.Button(cust_win,text="Exit",command=cust_win.destroy)
	cust_label.pack()
	cust_exit.pack()

def staff():
	staff_win=tk.Toplevel(win)
	staff_win.geometry('600x400')
	staff_win.resizable(width=False,height=False)
	staff_label=tk.Label(staff_win,text="This is the staff page")
	staff_exit=tk.Button(staff_win,text="Exit",command=staff_win.destroy)
	staff_label.pack()
	staff_exit.pack()

win=tk.Tk()
win.geometry('600x400')
win.resizable(width=False,height=False)
cust_button=tk.Button(win,text="go to customer page",command=customer)
staff_button=tk.Button(win,text="go to staff page",command=staff)
cust_button.pack()
staff_button.pack()
win.mainloop()