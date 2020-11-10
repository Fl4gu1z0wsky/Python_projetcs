import socket

HEADERSIZE = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5) # queue of 5

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")

	msg = "Welcome to the server!"
	msg = f'{len(msg):<{HEADERSIZE}}'+ msg # < means that it will put the headersize on the left (^ for the center)

	clientsocket.send(bytes(msg, "utf-8")) # we send a message
	clientsocket.close()
