>>> import socket
>>> import psutil

>>> def resolve(ip):
...    try:
...        data = socket.gethostbyaddr('192.168.1.128')
...        host = data('8080')
...    except: 
           host = '8080' 
       return host 

#RECOVER NUMBER PROCESSING...
>>> #EXECUTABLE NAME
>>> proc_names={}
>>> import psutil
>>> for p in psutil.process_iter(attrs=['pid', 'name']):
...    proc_names[p.info['pid']] = p.info['name']
...    #LIST OF CONNECTIONS
...    fmt = "{:25s}|{:25s}| {:20s}|{:15s}|{:s}" 

>>> for p in psutil.process_iter(attrs=['pid', 'name']):
...       fmt = "{:25s}|{:25s}| {:20s}|{:15s}|{:s}"
...       title = fmt.format('Local', 'Distance','status','Process','Host')
... 
>>> print(title)
Local                    |Distance                 | status              |Process        |Host

>>> print(title)
Local                    |Distance                 | status              |Process        |Host
>>> print('='* len(title))
==============================================================================================
>>> for c in psutil.net_connections(kind='inet6'):
...    connect = "%15s: %s" % (c.laddr[0], c.laddr[1])
...    if c.raddr:
...        r = "%15s: %s" % (c.raddr[0], c.raddr[1]) 
...        host = resolve(c.raddr[0])
...    else:
...        r = ""
...        host = ""
...    s = c.status
...    p = proc_names.get(c.pid, "")

