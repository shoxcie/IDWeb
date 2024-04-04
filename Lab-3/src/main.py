import my_gui
import my_http


def app():
	def send_request(username_entry, request_type_combo, cookie_text):
		print(username_entry.get(), request_type_combo.get(), cookie_text.get('1.0', 'end-1c').strip())
	
	my_gui.GUI("HTTP Client", 600, 400).notebook_init(send_request)


if __name__ == '__main__':
	app()
