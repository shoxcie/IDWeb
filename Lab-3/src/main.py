import tkinter as tk
from tkinter import ttk

import my_gui
import my_http


TITLE = "HTTP Client"
WIDTH_MIN = 600
HEIGHT_MIN = 400
SCALE = 1


def app():
	def print_response(text: str):
		response_text.delete(1.0, tk.END)
		response_text.insert(tk.END, text)
		notebook.select(3)
	
	def send_onclick():
		def text_to_dict(text: str):
			dictionary = {}
			for line in text.strip().splitlines():
				if '=' in line:
					key, value = line.split('=')
					dictionary[key.strip()] = value.strip()
			return dictionary
		
		url = url_entry.get()
		proxy = {'https': proxy_entry.get()}
		method = method_combo.get()
		cookie = text_to_dict(cookie_text.get('1.0', 'end-1c'))
		data = text_to_dict(data_text.get('1.0', 'end-1c'))
		
		my_http.request(method, url, proxy, cookie, data, print_response)
	
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
	
	##########
	# Data #
	##########
	data_tab_frame = my_gui.notebook.Tab(notebook, "Data").frame
	
	data_text = tk.Text(data_tab_frame)
	data_text.pack(side='left', expand=True, fill='both')
	
	data_vsb = my_gui.scrollbar.AutoScrollbar(data_tab_frame, orient='vertical', command=data_text.yview)
	data_text.configure(yscrollcommand=data_vsb.set)
	
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
