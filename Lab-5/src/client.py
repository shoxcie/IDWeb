import socket
import threading
import random
import sys


def read(client_socket: socket.socket):
	try:
		while True:
			data = client_socket.recv(1024).decode('utf-8')
			if data:
				print(data)
			else:
				print("[LOG]: Server closed")
				break
	except OSError:
		pass
	finally:
		client_socket.close()


def run_client(server_ip: str, server_port: int = 5000):
	# client_ip = socket.gethostbyname(socket.gethostname())
	client_ip = 'localhost'
	client_port = random.randint(6000, 60000)
	
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f"[LOG]: Client started on {client_ip}:{client_port}")
	
	try:
		username = str(input("[INPUT]: Username: "))
		if username == '':
			username = "Guest_" + str(client_port)
			print(f"[LOG]: Set username: {username}")
	except KeyboardInterrupt:
		print()
		return
	
	client_socket.connect((server_ip, server_port))
	client_socket.send(username.encode('utf-8'))
	print(f"[LOG]: Connected to {server_ip}:{server_port}")
	
	threading.Thread(target=read, args=(client_socket,)).start()
	
	try:
		while True:
			message = str(input()).encode('utf-8')
			client_socket.send(message)
	except KeyboardInterrupt:
		try:
			client_socket.shutdown(socket.SHUT_RDWR)
		except OSError:
			pass
		client_socket.close()
		print("[LOG]: Client closed")


if __name__ == '__main__':
	if len(sys.argv) == 1:
		try:
			ip = str(input("[INPUT]: Server IP >> "))
			run_client(ip)
		except KeyboardInterrupt:
			print()
	elif len(sys.argv) == 2:
		run_client(sys.argv[1])
