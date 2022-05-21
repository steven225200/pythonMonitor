#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/24 23:22
#@Author: steven.wang
#@File  : client.py

import asyncio
import time
from async_couchdb_influxdb.client.client_send_format import send
from async_couchdb_influxdb.client.client_received_format import received
from async_couchdb_influxdb.client.asyncio_monitor_command import asyncMonitorCommand



PASSWORD = '123456'
SERVERIP = '192.168.1.179'
PORT = 8888
HOSTNAME = 'containerd'
WAITTIME = 600



async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        SERVERIP, PORT)
    clentSend = send(password=PASSWORD, data=message)
    sendMessage = clentSend.sendFormat()
    writer.write(sendMessage)
    writer.write_eof()

    data = await reader.read()
    clentRecevied = received(PASSWORD, data)
    receivedMessage = clentRecevied.receivedFormat()
    writer.close()
    return receivedMessage



def loopmain():
    while True:
        try:
            amc = asyncMonitorCommand(HOSTNAME)
            lr = amc.monitorListRequest()
            rm = asyncio.run(tcp_echo_client(lr))
            cmd = amc.main(rm['serverMonitor'])
            asyncio.run(tcp_echo_client(cmd))
            if rm['monitorWaitTime']:
                time.sleep(int(rm['monitorWaitTime']))
        finally:
            time.sleep(WAITTIME)


if __name__ == '__main__':
    loopmain()

