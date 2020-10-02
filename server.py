import os
from socket import *

def send_file_list(connection):
	pass

def send_file(connection):
	pass

def main():
	files = os.listdir(".")
	files_as_string = ""
	index = 0
	for file in files:
		files_as_string += str(index) + " " + file + "\n"
		index = index + 1

	serverPort = 12000 
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	print("Server is ready and listening on port " + str(serverPort))
	while True:
		connectionSocket, addr = serverSocket.accept()
		query = connectionSocket.recv(1024).decode()
		print(query)
		if query == "ls":
			connectionSocket.send(files_as_string.encode());
			connectionSocket.close()
		elif "get" in query:
			#handle file sending here
			fileNo = int(query.split()[1])
			fileName = files[fileNo]
			print(fileName)
			connectionSocket.send(fileName.encode())
			fp = open(fileName, "rb")
			index = 0
			while True:
				chunk = fp.read(1024 * 1000)
				if len(chunk) <= 0:
					break
				print(str(index) + " : " + str(len(chunk)) + " bytes")
				index = index + 1
				connectionSocket.send(chunk)
			connectionSocket.close()

if __name__ == "__main__":
	main()
