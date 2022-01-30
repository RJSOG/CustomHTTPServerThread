#!/usr/bin/python3
import HTTPServer, requests

def getHTTPServerThread(PORT):
	return HTTPServer.HTTPServerThread(PORT)

def getRequest(url):
	print(f'[$_$] - Get {url}')
	return requests.get(url)

def startServerThread(ServerThread):
	print("[O_o] - Starting Server Thread...")
	ServerThread.start()
	print(f"[o_O] - Listening on 0.0.0.0:{ServerThread.PORT}")
	return


def checkWorkingServer(URL, ServerThread, ENDPOINT):
	URL = URL + ENDPOINT
	resp = getRequest(URL)
	lastRequestPath = ServerThread.getLastReqPath()
	if(lastRequestPath == ENDPOINT):
		return True
	else:
		return False

def main(URL, PORT):
	run = True
	start = True
	ServerThread = None
	check = False
	while(run):
		if(start):
			ServerThread = getHTTPServerThread(PORT)
			startServerThread(ServerThread)
			check = checkWorkingServer(URL, ServerThread, '/testEndpoint')
		if(check):
			if(start):
				print('[V_V] - Server is working!!')
				start = False
			#do stuff
		else:
			run = False
	ServerThread.stopServer()


if __name__ == "__main__":
	URL = input('[o_O] - LOCAL URL OR NGROK_URL: ')
	SERVER_PORT = int(input("[O_o] - Server Port : "))
	main(URL, SERVER_PORT)