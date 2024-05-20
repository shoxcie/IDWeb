import socket
import threading
import pyperclip


def broadcast(clients: list, message: str, ignore: socket.socket | None = None):
	for client, _ in clients:
		if client != ignore:
			client.send(message.encode('utf-8'))


def handle_client(clients: list, client_socket: socket.socket, client_address):
	nickname = client_socket.recv(1024).decode('utf-8')
	print(f"New client {client_address} as {nickname} connected")
	broadcast(clients, f"[SERVER]: {nickname} joined")
	clients.append((client_socket, nickname))
	
	try:
		while True:
			data = client_socket.recv(1024).decode('utf-8')
			if data:
				broadcast(clients, f"({nickname}): {data}", client_socket)
			else:
				clients.remove((client_socket, nickname))
				client_socket.close()
				print(f"Client {client_address} aka {nickname} disconnected")
				broadcast(clients, f"[SERVER]: {nickname} lost")
				break
	except OSError:
		return


def accept_connections(clients: list, server_socket: socket.socket):
	try:
		while True:
			client_socket, client_address = server_socket.accept()
			threading.Thread(target=handle_client, args=(clients, client_socket, client_address)).start()
	except OSError:
		return


def run_server(server_port: int = 5000):
	# server_ip = socket.gethostbyname(socket.gethostname())
	server_ip = 'localhost'
	server_socket = socket.create_server((server_ip, server_port), backlog=3)
	print(f"Server started on {server_ip}:{server_port}")
	pyperclip.copy(server_ip)
	
	clients = []
	
	threading.Thread(target=accept_connections, args=(clients, server_socket)).start()
	
	try:
		while True:
			pass
	except KeyboardInterrupt:
		for cl, _ in clients:
			cl.shutdown(socket.SHUT_RDWR)
			cl.close()
		server_socket.close()
		print("Server closed")


if __name__ == '__main__':
	run_server()
