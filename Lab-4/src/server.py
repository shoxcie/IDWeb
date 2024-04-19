import socket
import threading
import queue


def receive_data(sock: socket.socket, received_packets):
	try:
		while True:
			data, addr = sock.recvfrom(1024)
			received_packets.put((data, addr))
	except OSError:
		pass


def run_server():
	host = socket.gethostbyname(socket.gethostname())
	port = 5000
	print(f"[LOG]: Starting server at {host}:{port}")
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	clients = {}
	received_packets = queue.Queue()
	
	threading.Thread(target=receive_data, args=(s, received_packets)).start()
	
	try:
		while True:
			while not received_packets.empty():
				data, addr = received_packets.get()
				data = data.decode('utf-8')
				if addr not in clients:
					print(f"[LOG]: New client {addr} added as {data}")
					clients[addr] = data
					continue
				if data.endswith('qqq'):
					print(f"[LOG]: Client {addr} aka {clients[addr]} disconnected")
					clients.pop(addr)
					continue
				# print(f"({addr[0]}, {addr[1]}, {clients[addr]}) << {data}")
				for c in clients:
					if c != addr:
						msg = f"({clients[addr]}) << {data}"
						s.sendto(msg.encode('utf-8'), c)
	except KeyboardInterrupt:
		print("[LOG]: Shutting down...")
	finally:
		s.close()


if __name__ == '__main__':
	run_server()
