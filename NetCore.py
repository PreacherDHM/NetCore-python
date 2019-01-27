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
s = socket.socket()
class Sockets:


	
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
	#this runs the Console in the program
	def Connsole():

		while True:

			command = input('$')
			CommandList = ['Port Scan','Connect','Start Server','Send Packet']
			

			#Help
			if command == 'help':
				i = 0
				while i < len(CommandList):
					print(CommandList[i])
					i += 1
			if command == 'quit':
				quit()
			#Port Scan
			if command == CommandList[0]:
				pass
			#Connect
			if command == CommandList[1]:
				try:
					Ip = input('IP:')
					port = int(input('Port'))
					Sockets.Connechion((Ip,Port))
				except KeyboardInterrupt:
					Sockets.CloseSocket()
					print('Stoped')
				except:
					print('Connection was a falear')
			#Start Server
			if command == CommandList[2]:
				pass
			#Send Packet
			if command == CommandList[3]:
				pass
			




    


