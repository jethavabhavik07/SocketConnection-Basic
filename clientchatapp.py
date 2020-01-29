import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

hostname = socket.gethostname()
portno = 3333

msg = 'HELLO WORLD !!'

s.sendto(msg,(hostname,portno))





