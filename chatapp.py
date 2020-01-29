# Write a simple program to implement a chat application in python. It should consist of a sender & receiver module. Both should be able to chat with each other.
# PS: Look at Sockets & UDP.

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


hostname = socket.gethostname()
portno = 3333


s.bind((hostname,portno))

while True:
	data,addr = s.recvfrom(1024)
	print("Received :", data , " from ",addr)
