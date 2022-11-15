import socket

import numpy as np

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.3.20',9900))
print('Bind UDP to 9900')
while True:
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s' %addr)
    data = np.fromstring(data)
    print(data)
    s.sendto(data,addr)
