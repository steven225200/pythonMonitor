#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/25 1:52
#@Author: steven.wang
#@File  : message_type.py


class messageProcess():

    def __init__(self, hostinfo):
        self.hostinfo = hostinfo


    def messageType(self, message):
        if message['messageType'] == 'shellCommand':
            try:
                from async_couchdb_influxdb.server.message_process.linux_base_info import baseInfoFormat
                bf = baseInfoFormat(msg=message)
                return bf.interfaceFormat()
            except Exception as e:
                print(e)
                return None
        elif message['messageType'] == 'monitorList':
            try:
                from async_couchdb_influxdb.server.message_process.monitors import montiorList
                ml = montiorList(hostinfo=self.hostinfo, message=message)
                return ml.monitorResponse()
            except Exception as e:
                print(e)
                return None
        elif message['messageType'] == 'errorMessage':
            pass
        else:
            pass




