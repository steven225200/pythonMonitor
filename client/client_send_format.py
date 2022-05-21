#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/24 3:53
#@Author: steven.wang
#@File  : client_send_format.py

import random
import string
from async_couchdb_influxdb.client.client_encryption_decryption import prpcrypt


class send():

    def __init__(self, password, data):
        self.password = password
        self.data = str(data)

    def saltpassword(self):
        if len(self.password) <= 24:
            randomNum = 32 - len(self.password)
            randomSalt = ''.join(random.sample(string.ascii_letters + string.digits, randomNum))
            saltPassword = randomSalt + self.password
        else:
            randomSalt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            saltPassword = randomSalt + self.password[0:24]
        randomSalt = randomSalt + ((32 - len(randomSalt)) * '#')
        return randomSalt, saltPassword

    def encryption(self, saltPassword):
        encryp = prpcrypt(saltPassword)
        newdata = encryp.encrypt(self.data)
        return newdata


    def sendFormat(self):
        try:
            randomSalt, saltPassword = self.saltpassword()
            newdata = self.encryption(saltPassword)
            return randomSalt.encode('gbk') + newdata
        except Exception as e:
            print(e)
