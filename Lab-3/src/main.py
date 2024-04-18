import tkinter as tk
from tkinter import ttk

import my_gui


TITLE = "HTTP Client"
WIDTH_MIN = 600
HEIGHT_MIN = 400
SCALE = 1


def app():
	def print_response(text: str):
		response_text.delete(1.0, tk.END)
		response_text.insert(tk.END, text)
		notebook.select(2)
	
	def send_onclick():
		url = url_entry.get()
		proxy = proxy_entry.get()
		method = method_combo.get()
		cookies = cookie_text.get('1.0', 'end-1c').strip()
		
		print(url, proxy, method, cookies)
	
	root = tk.Tk()
	root.title(TITLE)
	root.minsize(WIDTH_MIN, HEIGHT_MIN)
	root.geometry(f'{int(WIDTH_MIN * SCALE)}x{int(HEIGHT_MIN * SCALE)}')
	
	for option in my_gui.theme.tk:
		root.option_add(*option)
	
	style = ttk.Style()
	style.theme_create(themename='black_theme', settings=my_gui.theme.ttk)
	style.theme_use('black_theme')
	
	notebook = ttk.Notebook(root)
	notebook.pack(expand=True, fill='both')
	
	###########
	# Request #
	###########
	request_tab_frame = my_gui.notebook.Tab(notebook, "Request").frame
	
	url_frame = ttk.Frame(request_tab_frame)
	url_frame.pack(padx=40, pady=20, fill='x')
	url_frame.columnconfigure(1, weight=1)
	ttk.Label(url_frame, text="URL: ").grid(row=0, column=0)
	url_entry = ttk.Entry(url_frame)
	url_entry.grid(row=0, column=1, sticky='ew')
	ttk.Label(url_frame, text="Proxy: ").grid(row=1, column=0)
	proxy_entry = ttk.Entry(url_frame)
	proxy_entry.grid(row=1, column=1, sticky='ew')
	
	method_frame = ttk.Frame(request_tab_frame)
	method_frame.pack(pady=20)
	ttk.Label(method_frame, text="Method: ").pack(side='left')
	method_combo = ttk.Combobox(method_frame, values=['GET', 'POST', 'HEAD', 'OPTIONS'], state='readonly')
	method_combo.current(0)
	method_combo.pack(side='left')
	
	ttk.Button(request_tab_frame, text="Send", command=send_onclick).pack(
		padx=(WIDTH_MIN / 3), fill='x', pady=20
	)
	
	##########
	# Cookie #
	##########
	cookie_tab_frame = my_gui.notebook.Tab(notebook, "Cookie").frame
	
	cookie_text = tk.Text(cookie_tab_frame)
	cookie_text.pack(side='left', expand=True, fill='both')
	
	cookie_vsb = my_gui.scrollbar.AutoScrollbar(cookie_tab_frame, orient='vertical', command=cookie_text.yview)
	cookie_text.configure(yscrollcommand=cookie_vsb.set)
	
	############
	# Response #
	############
	response_tab_frame = my_gui.notebook.Tab(notebook, "Response").frame
	
	response_text = tk.Text(response_tab_frame)
	response_text.pack(side='left', expand=True, fill='both')
	
	response_vsb = my_gui.scrollbar.AutoScrollbar(response_tab_frame, orient='vertical', command=response_text.yview)
	response_text.configure(yscrollcommand=response_vsb.set)
	
	root.mainloop()


if __name__ == '__main__':
	app()
