import socket

HEADERSIZE = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:

	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16)
		msg = msg.decode("utf-8")
		if new_msg:
			print(f'new message length: {msg}')
			try:
				msglen = int(msg[:HEADERSIZE])
			except ValueError:
				pass		
			new_msg = False

		full_msg += msg # we decode the message

		if len(full_msg)-HEADERSIZE == msglen:
			print("-- Full message received --")
			print(full_msg [HEADERSIZE:])
			new_msg = True
			full_msg = ''

	print(full_msg)
