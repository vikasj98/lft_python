from socket import *
import sys

def main():
	if(len(sys.argv)<2):
		print("usage : server.py server_ip [file number]")
		return
	serverName = sys.argv[1]
	serverPort = 12000 
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	listResponse = ""
	if(len(sys.argv) == 2):
		#servername was only provided, we need to get the file_list
		query = "ls"
		clientSocket.send(query.encode())
		listResponse = clientSocket.recv(1024)
		listResponse = listResponse.decode()
		print(listResponse)
		clientSocket.close()
		pass
	elif(len(sys.argv) == 3):
		#servername and file number provided, get the file
		query = "get " + sys.argv[2]
		clientSocket.send(query.encode())
		fileName = clientSocket.recv(1024).decode()
		print(fileName)
		f = open(fileName, "wb")
		index = 0
		while True:
			chunk = clientSocket.recv(500 * 1024)
			if len(chunk) <= 0:
				break
			print(str(index) + " : " + str(len(chunk)) + " bytes")
			index = index + 1
			f.write(chunk)
		f.close()
#	print(sys.argv)

if __name__ == "__main__":
	main()
