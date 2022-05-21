#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/24 3:45
#@Author: steven.wang
#@File  : client_received_format.py



from async_couchdb_influxdb.client.client_encryption_decryption import prpcrypt


class received():

    def __init__(self, password, data):
        self.data = data
        self.password = password
        self.receivedSalt = data[0:32].decode('gbk').rstrip('#')
        self.message = None


    def decrypt(self):
        decryptPassword = self.receivedSalt + self.password
        decryptobj = prpcrypt(decryptPassword)
        message = decryptobj.decrypt(self.data[32:])
        self.message = eval(message)


    def receivedFormat(self):
        try:
            self.decrypt()
            return self.message
        except Exception as e:
            print(e)







