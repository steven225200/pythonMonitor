#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/29 0:29
#@Author: steven.wang
#@File  : python_influxDB.py



from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class influxdbObj():

    def __init__(self):
        self.serverUri = 'http://192.168.1.207:8086'

    def interfaceRecord(self):
        token = "pvIt9TUeK04PecIidlwBMknY80CRm6FDdmdbJm8vqOCghOl9XxHvKCv_RJIlobPKXvelbQ1CBt2U-2lfhNIz7w=="
        my_org = "admin"
        client = InfluxDBClient(url=self.serverUri, token=token, org=my_org)
        return client.write_api(write_options=SYNCHRONOUS)


