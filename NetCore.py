import socket
import sys
import io

#Aother of NetCore:Preacher

#this appucation is for sudying only and not ment for black hat use.
#if you use this code for molishes use I am not responsible for your actchions.
#and if you use this libary for your self pleaze aske for promishion ferst, thanks.


#have Fun!!!
#test



#Sockets is the interface to the web and all the payload are diploid
class Sockets:


	s = socket.socket()
	def CloseSocket():
         s.Close()
	def Connechion(Socket):
		s.connect(Socket)
	#SendToServer Sends a seres of bytes to the server
	def SendToServer(Message):
		NetCore.Sockets.s.sendall(b"{}".join(Message))
	#ReseveFomeServer returns a string and needs a buffer size 1042 is recumendid
	def ReseveFromeServer(bufferSize):
		Message = str(NetCore.Sockets.s.recv(bufferSize).decode('ASCII'))
		return Message

class IoInterface():
	def Connsole():
		pass

    


