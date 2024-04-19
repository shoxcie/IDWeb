import socket
import threading
import random
import sys


def receive_data(sock: socket.socket):
	try:
		while True:
			data, addr = sock.recvfrom(1024)
			print(data.decode('utf-8'))
	except OSError:
		pass


def run_client(server_ip: str):
	host = socket.gethostbyname(socket.gethostname())
	port = random.randint(6000, 10000)
	print(f"[LOG]: Starting client at {host}:{port}")
	server = (server_ip, 5000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	
	try:
		username = input("[INPUT]: Username >> ")
		if username == '':
			username = "Guest_" + str(random.randint(1000, 9999))
			print(f"[LOG]: Set username: {username}")
		s.sendto(username.encode('utf-8'), server)
	except KeyboardInterrupt:
		print()
		exit(0)
	
	threading.Thread(target=receive_data, args=(s,)).start()
	
	try:
		while True:
			data = input()
			if data == '':
				continue
			if data == 'qqq':
				break
			s.sendto(data.encode('utf-8'), server)
	except KeyboardInterrupt:
		pass
	finally:
		s.sendto('qqq'.encode('utf-8'), server)
		s.close()


if __name__ == '__main__':
	if len(sys.argv) == 1:
		try:
			ip = input("[INPUT]: Server IP >> ")
			run_client(ip)
		except KeyboardInterrupt:
			print()
	elif len(sys.argv) == 2:
		run_client(sys.argv[1])
