import tkinter as tk
from tkinter import ttk
from typing import Callable

from . import theme, notebook, scrollbar


class GUI:
	__instance = None
	
	def __new__(cls, title: str, width_min: int, height_min: int, scale: int | float = 1):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance
	
	def __init__(self, title: str, width_min: int, height_min: int, scale: int | float = 1):
		root = tk.Tk()
		root.title(title)
		root.minsize(width_min, height_min)
		root.geometry(f'{int(width_min * scale)}x{int(height_min * scale)}')
		
		for option in theme.tk:
			root.option_add(*option)
		
		style = ttk.Style()
		style.theme_create(themename='black_theme', settings=theme.ttk)
		style.theme_use('black_theme')
		
		self.__root = root
		self.__width = width_min
		self.__height = height_min
		self.__notebook = ttk.Notebook(self.__root)
		self.__notebook.pack(expand=True, fill='both')
	
	def notebook_init(self, send_request: Callable):
		def send_onclick():
			send_request(url_entry, method_combo, cookie_text)
		
		###########
		# Request #
		###########
		request_tab_frame = notebook.Tab(self.__notebook, "Request").frame
		
		url_frame = ttk.Frame(request_tab_frame)
		url_frame.pack(padx=40, pady=20, fill='x')
		url_frame.columnconfigure(1, weight=1)
		ttk.Label(url_frame, text="URL: ").pack(side='left')
		url_entry = ttk.Entry(url_frame)
		url_entry.pack(side='left', expand=True, fill='x')
		
		method_frame = ttk.Frame(request_tab_frame)
		method_frame.pack(pady=20)
		ttk.Label(method_frame, text="Method: ").pack(side='left')
		method_combo = ttk.Combobox(method_frame, values=['GET', 'POST', 'HEAD', 'OPTIONS'], state='readonly')
		method_combo.current(0)
		method_combo.pack(side='left')
		
		ttk.Button(request_tab_frame, text="Send", command=send_onclick).pack(
			padx=(self.__width / 3), fill='x', pady=20
		)
		
		##########
		# Cookie #
		##########
		cookie_tab_frame = notebook.Tab(self.__notebook, "Cookie").frame
		
		cookie_text = tk.Text(cookie_tab_frame)
		cookie_text.pack(side='left', expand=True, fill='both')
		
		cookie_vsb = scrollbar.AutoScrollbar(cookie_tab_frame, orient='vertical', command=cookie_text.yview)
		cookie_text.configure(yscrollcommand=cookie_vsb.set)
		
		#########
		# Proxy #
		#########
		proxy_tab_frame = notebook.Tab(self.__notebook, "Proxy").frame
		
		login_frame = ttk.Frame(proxy_tab_frame)
		login_frame.pack(padx=40, pady=20, fill='x')
		login_frame.columnconfigure(1, weight=1)
		
		ttk.Label(login_frame, text="Username: ").grid(row=0, column=0)
		username_entry = ttk.Entry(login_frame)
		username_entry.grid(row=0, column=1, sticky='ew')
		
		ttk.Label(login_frame, text="Password: ").grid(row=1, column=0)
		password_entry = ttk.Entry(login_frame, show='*')
		password_entry.grid(row=1, column=1, sticky='ew')
		
		self.__root.mainloop()
