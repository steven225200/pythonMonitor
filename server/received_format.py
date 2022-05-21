#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/24 3:45
#@Author: steven.wang
#@File  : client_received_format.py


from async_couchdb_influxdb.server.encryption_decryption import prpcrypt
from async_couchdb_influxdb.server.python_couchDB import hostInfo, groupInfo, pythonErrorMessage, shellErrorMessage

class received():

    def __init__(self, data, addr):
        self.data = data
        self.addr = addr[0]
        self.receivedSalt = data[0:32].decode('gbk').rstrip('#')
        self.hostInformationDB = None
        self.message = None


    def hostindb(self):
        self.hostInformationDB = hostInfo(self.addr)[0]


    def decrypt(self):
        hostPassword = self.hostInformationDB['password']
        decryptPassword = self.receivedSalt + hostPassword
        decryptobj = prpcrypt(decryptPassword)
        message = decryptobj.decrypt(self.data[32:])
        self.message = eval(message)


    def checkhostname(self):
        return self.message['hostname'] == self.hostInformationDB['hostname']


    def receivedFormat(self):
        try:
            self.hostindb()
            self.decrypt()
            if self.checkhostname():
                return self.hostInformationDB, self.message
        except Exception as e:
            print(e)

