# Author GLaDOSDan <gladosdan@gmail.com>

import socket
import sys
import time
import json

# Confirm we have enough arguments to proceed
if len(sys.argv) < 3:
	print "ARGV_ERROR"
	sys.exit()

# Open connection to Extron IPL
try:
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(1) # Set timeout to 1 second
	client_socket.connect((sys.argv[1], 23))

# Catch any connection errors
except socket.error:
	print "CONNECT_ERROR"
	sys.exit()

# Execute commands
try:

	# Send commands
	for command in sys.argv[2::]:
		client_socket.send(command)

	# Read responses into response array
	response = []
	while len(response) < (1 + len(sys.argv)):
		data = client_socket.recv(512)
		response = response + data.splitlines()

# Catch any read errors
except socket.error:
	print "READ_ERROR"
	sys.exit()

# Format and print final response
print json.dumps(response[3::])
