from os import path
import tkinter as tk
from tkinter import ttk

from theme import black_theme_settings


IMG_DIR = path.abspath(path.join(path.dirname(__file__), path.pardir, 'img'))


def gui():
	class Tab:
		def __init__(self, parent: ttk.Notebook, title: str, image_png: str):
			self.frame = ttk.Frame(parent)
			self.__logo = tk.PhotoImage(file=path.join(IMG_DIR, image_png))
			parent.add(self.frame, text=title, image=self.__logo, compound='left')
	
	root = tk.Tk()
	root.title("EMail Client")
	root.geometry('600x500')
	root.update()
	root.minsize(root.winfo_width(), root.winfo_height())
	
	style = ttk.Style()
	style.theme_create(themename='black_theme', settings=black_theme_settings)
	style.theme_use('black_theme')
	
	notebook = ttk.Notebook(root)
	notebook.pack(expand=True, fill='both')
	user = Tab(notebook, " User", "user.png")
	inbox = Tab(notebook, " Inbox", 'inbox.png')
	outbox = Tab(notebook, " Outbox", 'outbox.png')
	message = Tab(notebook, " Message", 'message.png')
	
	label1 = tk.Label(inbox.frame, text="Hello, Inbox!")
	label1.pack(padx=10, pady=10, anchor='w')
	
	login_frame = ttk.Frame(user.frame)
	login_frame.pack(pady=20)
	ttk.Label(login_frame, text="Username: ").grid(row=0, column=0)
	ttk.Entry(login_frame, font=('Arial', 12, 'bold'), width=30).grid(row=0, column=1)
	ttk.Label(login_frame, text="Password: ").grid(row=1, column=0)
	ttk.Entry(login_frame, font=('Arial', 12, 'bold'), width=30, show='*').grid(row=1, column=1)
	
	root.mainloop()


if __name__ == '__main__':
	gui()
