#import thing we need
import network
from machine import Pin,ADC
import socket
#config the net
ap = network.WLAN(network.AP_IF)
ap.config(essid='yournetwork',password='12345678')
ap.active(True)
#more config
print('wifi')
print(ap.ifconfig())
#set the sensor
yl69 = ADC(0)
#Conf The IP
socket_ap = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_ap.bind(('YourIPadress',80))
socket_ap.listen(1)
#print the web message

while True:
    client_ap = socket_ap.accept()
    print("client_ap :" , client_ap[0])
    a=yl69.read()
    if a >= 1000:
        client_ap[0].send('<h1>Time to Water!</h1>')
    elif a >= 600:
        client_ap[0].send('<h1>Medium</h1>')
    else:
        client_ap[0].send('<h1>Perfect</h1>')
    client_ap[0].close()
