import socket

hostname = socket.gethostname()
print("Hostname:", hostname)
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("IP:", ip)
