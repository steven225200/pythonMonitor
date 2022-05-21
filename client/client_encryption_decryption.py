#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/22 23:19
#@Author: steven.wang
#@File  : client_encryption_decryption.py



from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import urllib.parse

class prpcrypt():

    def __init__(self, key):
        self.ciphertext = None
        self.key = key.encode()
        self.mode = AES.MODE_ECB

    def encrypt(self, message):
        urlmessage = urllib.parse.quote(str(message))
        cryptor = AES.new(self.key, self.mode)
        length = 16
        addNum = length - (len(urlmessage) % length)
        newMessage = urlmessage + ('#' * addNum)
        self.ciphertext = cryptor.encrypt(newMessage.encode())
        return b2a_hex(self.ciphertext)


    def decrypt(self, message):
        cryptor = AES.new(self.key, self.mode)
        plain_text = cryptor.decrypt(a2b_hex(message))
        messageUrlUnquote = urllib.parse.unquote(plain_text.decode('utf-8').rstrip('#'))
        return messageUrlUnquote

