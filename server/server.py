#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/23 2:58
#@Author: steven.wang
#@File  : server.py


import asyncio
from async_couchdb_influxdb.server.received_format import received
from async_couchdb_influxdb.server.send_format import send
from async_couchdb_influxdb.server.message_type import messageProcess



async def handle_echo(reader, writer):
    data = await reader.read()
    addr = writer.get_extra_info('peername')
    serverReceived = received(data, addr)
    hostInformationDB, receivedMessage = serverReceived.receivedFormat()
    mp = messageProcess(hostinfo=hostInformationDB)
    mpr = mp.messageType(message=receivedMessage)
    if mpr != None:
        serverSend = send(hostInformationDB['password'], str(mpr))
        sendMessage = serverSend.sendFormat()
        writer.write(sendMessage)
        await writer.drain()
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '192.168.1.179', 8888)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())

