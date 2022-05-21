#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/26 1:25
#@Author: steven.wang
#@File  : asyncio_monitor_command.py



import asyncio
import time
import copy

class asyncMonitorCommand():

    def __init__(self, hostname):
        self.time = time.time()
        self.hostname = hostname

    def baseInfo(self):
        return {'timeStamp': self.time, 'hostname': self.hostname}


    def monitorListRequest(self):
        baseInfo = copy.deepcopy(self.baseInfo())
        return baseInfo.update({'messageType': 'monitorList'})


    def errorMessage(self, shellName, errorInfo):
        print(shellName, errorInfo)
        baseInfo = copy.deepcopy(self.baseInfo())
        return baseInfo.update({'messageType': 'errorMessage', 'shellName': shellName, 'shellStderr': str(errorInfo)})


    async def shellCommand(self, fut, shellName, shell):
        try:
            proc = await asyncio.create_subprocess_shell(
                shell,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await proc.communicate()
            if proc.returncode == 0:
                fut.set_result({shellName: stdout.decode()})
            else:
                raise Exception(shellName + " - shell command error or no response !" + '\n' + stderr.decode())
        except Exception as e:
            self.errorMessage(shellName=shellName, errorInfo=e)


    async def main(self, shellDict):
        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        lock = asyncio.Lock()
        shellMonitor = {}
        for shellName, shell in shellDict.items():
            async with lock:
                loop.create_task(self.shellCommand(fut, shellName, shell))
                shellMonitor.update(await fut)
        baseInfo = copy.deepcopy(self.baseInfo())
        #update这个函数没有返回值，在原字典上进行了修改
        return baseInfo.update({'messageType': 'shellCommand', 'shellMonitor': shellMonitor})
        #return baseInfo





