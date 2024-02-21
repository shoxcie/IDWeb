from os import path
import tkinter as tk
from tkinter import ttk

from theme import black_theme_settings


IMG_DIR = path.abspath(path.join(path.dirname(__file__), path.pardir, 'img'))
WIDTH_MIN = 600
HEIGHT_MIN = 400


def gui():
	class Tab:
		def __init__(self, parent: ttk.Notebook, title: str, image_png: str):
			self.frame = ttk.Frame(parent)
			self.__logo = tk.PhotoImage(file=path.join(IMG_DIR, image_png))
			parent.add(self.frame, text=title, image=self.__logo, compound='left')
	
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
		print(username, password)           # Replace with IMAP login handle #
		
		ttk.Label(status_frame, text="Status:").pack(side='left')
		ttk.Label(status_frame, text="Logged in", foreground='green').pack(side='left')
	
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
	inbox = Tab(notebook, " Inbox", 'inbox.png')
	outbox = Tab(notebook, " Outbox", 'outbox.png')
	message = Tab(notebook, " Message", 'message.png')
	
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
	status_frame = ttk.Frame(user.frame)
	status_frame.pack(anchor='w', padx=40, pady=20)
	
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
	text = tk.Text(
		message.frame,
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
	text.pack(expand=True, fill='both')
	vsb = AutoScrollbar(message.frame, orient='vertical', command=text.yview)
	text.configure(yscrollcommand=vsb.set)
	ttk.Button(message.frame, text="Send").pack(side='bottom', fill='x')
	
	root.mainloop()


if __name__ == '__main__':
	gui()
