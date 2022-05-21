#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/25 2:06
#@Author: steven.wang
#@File  : monitors.py


from async_couchdb_influxdb.server.python_couchDB import groupInfo


#返回主机需要执行的命令字典
class montiorList():
    def __init__(self, hostinfo, message):
        self.hostinfo = hostinfo
        self.message = message

    def monitorResponse(self):
        groupInformation = groupInfo(groupName=self.hostinfo['group'])
        serverMonitor = groupInformation['groupShell']
        if self.hostinfo['localWaitTime'] != '':
            monitorWaitTime = self.hostinfo['localWaitTime']
        else:
            monitorWaitTime = groupInformation['groupWaitTime']
        if self.hostinfo['localShell'] != {}:
            for commandName, commandShell in self.hostinfo['localShell'].items():
                if commandName not in serverMonitor:
                    serverMonitor.update({commandName: commandShell})
        return {"serverMonitor": serverMonitor, 'monitorWaitTime': monitorWaitTime}