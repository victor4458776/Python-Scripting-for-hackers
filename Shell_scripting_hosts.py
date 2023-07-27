>>> import socket
>>> import psutil

>>> def resolve(ip):
...    try:
...        data = socket.gethostbyaddr('192.168.1.128')
...        host = data('8080')
...    except: 
           host = '' 
       return host 

#RECOVER NUMBER PROCESSING...

