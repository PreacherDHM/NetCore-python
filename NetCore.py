import socket
import sys
import io
import threading

#Aother of NetCore:Preacher

#this appucation is for sudying only and not ment for black hat use.
#if you use this code for molishes use I am not responsible for your actchions.
#and if you use this libary for your self pleaze aske for promishion ferst, thanks.


#have Fun!!!
#test



#Sockets is the interface to the web and all the payload are diploid

class Sockets:


	#s = socket.socket()
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
	def PortScan(ip,minPort,MaxPort,curentThread):
		curentPort = minPort
		while minPort < MaxPort:
			curentPort += 1
			try:
				s = socket.socket()
				s.connect((ip,port))
				print('Connected to port:',port,'Thread:',curentThread)
				s.close()
			except:
				print(curentPort)

	def ThreadedPortScan(ip,minPort,maxPort,ThreadCount):
		curentThreadPort = minPort
		curentThreadCount = 0
		

		while curentThreadCount <= ThreadCount:
			#curentThreadPort += 1
			curentThreadCount += 1

			print('\rThread:',curentThreadCount,'Ports:',curentThreadCount * maxPort,end = '\r')

			pst = threading.Thread(target = Sockets.PortScan,args=(ip, curentThreadCount * minPort,curentThreadCount * maxPort,curentThreadCount))
			pst.start()

			#Sockets.PortScan(ip,curentThreadPort)
			
			
			
		
		#pass

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