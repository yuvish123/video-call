import socket, cv2, pickle,struct


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
print("\t\t\t\n=================================================")
port = 9999
socket_address = ('192.168.43.219',port)
print("Socket Created")
print("\t\t\t\n=================================================")

server_socket.bind(socket_address)
print("Socket Bind Successfully")
print("\t\t\t\n=================================================")


server_socket.listen(5)
print("LISTENING AT:",socket_address)
print("\t\t\t\n=================================================")

print("Socket Accept")
print("\t\t\t\n=================================================")
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
		
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()

print("Thank you guy's")
print("\t\t\t\n=================================================")
