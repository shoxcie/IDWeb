from os import path
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from theme import black_theme_settings
from email_client import SMTP, IMAP

IMG_DIR = path.abspath(path.join(path.dirname(__file__), path.pardir, 'img'))
WIDTH_MIN = 600
HEIGHT_MIN = 400


def gui(smtp_client: SMTP, imap_client: IMAP):
	class Tab:
		def __init__(self, parent: ttk.Notebook, title: str, image_png: str):
			self.frame = ttk.Frame(parent)
			self.__notebook = parent
			self.__id = len(self.__notebook.tabs())
			self.__logo = tk.PhotoImage(file=path.join(IMG_DIR, image_png))
			parent.add(self.frame, text=title, image=self.__logo, compound='left')
		
		def show(self):
			self.__notebook.add(self.__notebook.tabs()[self.__id])
		
		def hide(self):
			self.__notebook.hide(self.__id)
			return self
	
	class AutoScrollbar(ttk.Scrollbar):
		def set(self, low, high):
			if float(low) <= 0.0 and float(high) >= 1.0:
				self.pack_forget()
			else:
				self.pack(side='left', fill='y')
			ttk.Scrollbar.set(self, low, high)
	
	def login_onclick():
		username = username_entry.get()
		password = password_entry.get()
		
		if smtp_client.login(username, password) and imap_client.login(username, password):
			inbox.show()
			outbox.show()
			message.show()
			inbox_table_refresh_onclick()
		else:
			messagebox.showerror(title="Error", message="Failed to log in :(")
	
	def logout_onclick():
		smtp_client.logout()
		imap_client.logout()
		username_entry.delete(0, tk.END)
		password_entry.delete(0, tk.END)
		inbox.hide()
		outbox.hide()
		message.hide()
	
	def inbox_table_onclick(event):
		if inbox_table.selection():
			item = inbox_table.selection()[0]
			index = inbox_table.index(item)
			print("Clicked row index:", index)
	
	def inbox_table_refresh_onclick():
		for item in inbox_table.get_children():
			inbox_table.delete(item)
		
		messages = imap_client.read()
		messages.reverse()
		
		for msg in messages:
			inbox_table.insert('', tk.END, values=msg)
	
	def send_onclick():
		email = email_entry.get()
		subject = subject_entry.get()
		text = text_entry.get('1.0', 'end-1c').strip()
		confirm = messagebox.askyesno("Confirmation", "Are you certain you want to send this email message?")
		if confirm:
			smtp_client.send(email, subject, text)
	
	root = tk.Tk()
	root.title("EMail Client")
	root.geometry(f'{WIDTH_MIN}x{HEIGHT_MIN}')
	root.update()
	root.minsize(root.winfo_width(), root.winfo_height())
	
	style = ttk.Style()
	style.theme_create(themename='black_theme', settings=black_theme_settings)
	style.theme_use('black_theme')
	
	notebook = ttk.Notebook(root)
	notebook.pack(expand=True, fill='both')
	user = Tab(notebook, " User", 'user.png')
	inbox = Tab(notebook, " Inbox", 'inbox.png').hide()
	outbox = Tab(notebook, " Outbox", 'outbox.png').hide()
	message = Tab(notebook, " Message", 'message.png').hide()
	
	# User #
	login_frame = ttk.Frame(user.frame)
	login_frame.pack(padx=40, pady=20, fill='x')
	login_frame.columnconfigure(1, weight=1)
	ttk.Label(login_frame, text="Username: ").grid(row=0, column=0)
	username_entry = ttk.Entry(login_frame, font=('Arial', 14, 'bold'))
	username_entry.grid(row=0, column=1, sticky='ew')
	ttk.Label(login_frame, text="Password: ").grid(row=1, column=0)
	password_entry = ttk.Entry(login_frame, font=('Arial', 14, 'bold'), show='*')
	password_entry.grid(row=1, column=1, sticky='ew')
	ttk.Button(user.frame, text="Login", command=login_onclick).pack(padx=(WIDTH_MIN / 3), fill='x')
	ttk.Button(user.frame, text="Logout", command=logout_onclick).pack(padx=(WIDTH_MIN / 3), fill='x', pady=20)
	
	# # # # # # # # # #
	notebook.select(1)
	test_data = []
	for n in range(0, 20):
		test_data.append((f"Datetime{n}", f"Subject{n}", f"Email{n}"))
	# # # # # # # # # #
	
	# Inbox #
	inbox_table_frame = ttk.Frame(inbox.frame)
	inbox_table_frame.pack(fill='both', expand=True)
	inbox_table = ttk.Treeview(inbox_table_frame, columns=("Date", "Subject", "Email"), show='headings', height=0)
	inbox_table.pack(side='left', fill='both', expand=True)
	inbox_table_vsb = AutoScrollbar(inbox_table_frame, orient='vertical', command=inbox_table.yview)
	inbox_table.configure(yscrollcommand=inbox_table_vsb.set)
	inbox_table.bind('<ButtonRelease-1>', inbox_table_onclick)
	inbox_table.heading('Date', text="Date")
	inbox_table.heading('Subject', text="Subject")
	inbox_table.heading('Email', text="Email")
	inbox_table.column('Date', width=150, stretch=False)
	inbox_table.column('Email', width=50)
	ttk.Button(inbox.frame, text="Refresh", command=inbox_table_refresh_onclick).pack(side='bottom', fill='x')
	
	# # # # # # # # # #
	for data in test_data:
		inbox_table.insert('', tk.END, values=data)
	# # # # # # # # # #
	
	# Message #
	header_frame = ttk.Frame(message.frame)
	header_frame.pack(padx=40, pady=20, fill='x')
	header_frame.columnconfigure(1, weight=1)
	ttk.Label(header_frame, text="   Email: ").grid(row=0, column=0)
	email_entry = ttk.Entry(header_frame, font=('Arial', 14, 'bold'))
	email_entry.grid(row=0, column=1, sticky='ew')
	ttk.Label(header_frame, text="Subject: ").grid(row=1, column=0)
	subject_entry = ttk.Entry(header_frame, font=('Arial', 14, 'bold'))
	subject_entry.grid(row=1, column=1, sticky='ew')
	text_frame = ttk.Frame(message.frame)
	text_frame.pack(expand=True, fill='both')
	text_entry = tk.Text(
		text_frame,
		background='black',
		foreground='white',
		insertbackground='white',
		selectbackground='gray30',
		insertwidth=2,
		font=('Arial', 14),
		border=4,
		width=0,
		height=0
	)
	text_entry.pack(side='left', expand=True, fill='both')
	text_vsb = AutoScrollbar(text_frame, orient='vertical', command=text_entry.yview)
	text_entry.configure(yscrollcommand=text_vsb.set)
	ttk.Button(message.frame, text="Send", command=send_onclick).pack(side='bottom', fill='x')
	
	root.mainloop()


if __name__ == '__main__':
	with SMTP() as smtp, IMAP() as imap:
		gui(smtp, imap)
