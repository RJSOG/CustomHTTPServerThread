from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import threading

class RequestHandler(BaseHTTPRequestHandler):
	def __init__(self, parent):
		self.parent = parent

	def __call__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	#Custom Headers
	def returnHeaders(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()

	def do_GET(self):
		self.parent.addReq(self.path, self.headers)

	#You can log your own msg here
	def log_message(self, format, *args):
		return 

class HTTPServerThread(threading.Thread):
	def __init__(self, PORT):
		super(HTTPServerThread, self).__init__()
		self.PORT = PORT
		
	def run(self):
		self.buffReq = []
		try:
			self.handler = RequestHandler(self)
			self.WebServ = ThreadingHTTPServer(('0.0.0.0', self.PORT), self.handler)
			self.WebServ.serve_forever()
		except Exception as e:
			print(f"[X_X] - ERROR : {e}")
	
	def stopServer(self):
		self.WebServ.shutdown()

	def addReq(self, path, headers):
		obj = {"path" : path, "headers": headers}
		self.buffReq.append(obj)
		return True

	def getLastReqPath(self):
		return self.buffReq[-1]['path']

	def getLastReqObj(self):
		return self.buffReq[-1]