#import thing we need
import network
import socket
#config the net
ap = network.WLAN(network.AP_IF)
ap.config(essid='yournetwork',password='12345678')
ap.active(True)
#more config
print('wifi')
print(ap.ifconfig())

socket_ap = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_ap.bind(('YourIPadress',80))
socket_ap.listen(1)
#print the web message
while True:
  client_ap = socket_ap.accept()
  print("client_ap :" , client_ap[0])
  client_ap[0].send('<h1>Hello!</h1>')
  client_ap[0].close()
