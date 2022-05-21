#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/29 0:29
#@Author: steven.wang
#@File  : linux_base_info.py

from influxdb_client import Point
from async_couchdb_influxdb.server.python_influxDB import influxdbObj

#interface信息获取示例
#'timeStamp': 1616871007.5392575, 'hostname': 'containerd', 'messageType': 'shellCommand', 'shellMonitor': {'interface': 'Inter-|   Receive                                                |  Transmit\n face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed\nenp0s3: 51309156   50715    0    0    0     0          0         0 38319065   29755    0    0    0     0       0          0\n    lo: 175472925   42555    0    0    0     0          0         0 175472925   42555    0    0    0     0       0          0\ndocker0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0\n'}}

class baseInfoFormat():

    def __init__(self, msg):
        self.influxdb = influxdbObj()
        self.msg = msg


    def interfaceFormat(self):
        myu_bucket = "interface"
        write_api = self.influxdb.interfaceRecord()
        print(self.msg)
        ifList = self.msg['shellMonitor']['interface'].split('\n')[2:]
        for i in ifList:
            infor = i.split(':').replace(' ', '')
            netName = infor[0]
            netNum = [num for num in infor[1].split(' ') if num != 0]
            if netNum != []:
                print(netNum)
                netDatePoint = Point(self.msg['hostname']).tag('interfaceName', netName).field('timeStamp', self.msg['timeStamp']).field('ReceiveBytes', netNum[0]).field('ReceivePackets', netNum[1]).field('TransmitBytes', netNum[2]).field('TransmitPackets', netNum[3])
                write_api.write(bucket=myu_bucket, Point=netDatePoint)
        return None

