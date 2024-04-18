import requests
import threading
from typing import Callable


def request(
		method: str,
		url: str,
		proxy: dict = None,
		cookie: dict = None,
		data: dict = None,
		print_response: Callable = None,
		return_list: list = None
):
	def sub_request():
		make_request = None
		match method:
			case 'GET':
				make_request = requests.get
			case 'POST':
				make_request = requests.post
			case 'HEAD':
				make_request = requests.head
			case 'OPTIONS':
				make_request = requests.options
			case _:
				print('[ERROR]: Unknown method')
		
		response = make_request(url, proxies=proxy, cookies=cookie, data=data)
		
		if print_response is not None:
			print_response(response.text)
		
		if return_list is not None:
			return_list.append(response.status_code)
			return_list.append(response.text)
	
	thread = threading.Thread(target=sub_request)
	thread.start()
	if return_list is not None:
		thread.join()
