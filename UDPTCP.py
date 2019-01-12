# Simple UDP/TCP Client 
# Useage: python.py UDPTCP.py Hostname Port Data TCP/UDP
# Example: python.py UDPTCP.py 127.0.0.1 80 MyData UDP
# By Matija Krolo

# Import Libraries
import socket, sys, random

# Error Checking
if len(sys.argv) != 5:
	print("Useage: python.py UDPsend.py Hostname Port Data UDP/TCP")
	exit()

# Data -> Variables & Confirm Inputs for user
ip, port, data, method = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
print 'Host: ' + ip + ':' + port
print 'Data: ' + data
print 'Using: ' + method

if str(method).lower() == "udp":
	try:
		destination = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
		destination.sendto(str("data"), (str(ip), int(port))) 
	except socket.timeout:
		print 'Request Has Timed Out' 

if str(method).lower() == "tcp":
	try:
		destination = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		destination.connect((str(ip), int(port)))
		destination.send(str(data))
	except socket.timeout:
		print 'Request Has Timed Out'



