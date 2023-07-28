[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pymongo import MongoClient
>>> session = MongoClient("mongodb://localhost:27017/")
>>> db = session.test
>>> contacts = db.contacts
>>> contacts.drop()

# SERVER ERRORS pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [Errno 111] 
# Connection refused, Timeout: 30s, Topology Description: <TopologyDescription id: 64c420b79b35acaec6e47d83, topology_type: 
# Unknown, servers: 
# [<ServerDescription ('localhost', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('localhost:27017: [Errno 111] Connection refused')

>>> contact = {
...    'name'
...    'tel': '0503513515125',
...    'key': 'dawdna#@#1'
... }
>>> print(contact)
{'nametel': '0503513515125', 'key': 'dawdna#@#1'}
# Hack mongodb databases accessing to the server 27017, you can create your own server to hack users
>>> result = contacts.insert_one(contact)
