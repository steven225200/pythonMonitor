#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/3/18 0:09
#@Author: steven.wang
#@File  : python_couchDB.py

import couchdb

#couchdb.Server('http://python_deve:123456@192.168.1.207:5984/')
DBIP = '192.168.1.207'
DBPORT = '5984'
DBUSERNAME = 'python_deve'
DBPASSWORD = '123456'
DBURI = 'http://' + DBUSERNAME + ':' + DBPASSWORD + '@' + DBIP + ':' + DBPORT + '/'

def hostInfo(ip):
    couch = couchdb.Server(DBURI)
    hostInformation = couch['host_info']
    hostSelect = {'selector': {'ip': ip}, 'fields': ['hostname', 'ip', 'password', 'group', '_id', 'localWaitTime', 'localShell']}
    return [{'hostname': row['hostname'], 'ip': row['ip'], 'password': row['password'], 'group': row['group'], 'couch_id': row['_id'], 'localWaitTime': row['localWaitTime'], 'localShell': row['localShell']} for row in hostInformation.find(hostSelect)]


def groupInfo(groupName):
    couch = couchdb.Server(DBURI)
    groupInformation = couch['host_groups']
    groupSelect = {'selector': {'groupName': groupName}, 'fields': ["groupName", "groupWaitTime", "groupShell"]}
    return [{'groupName': row['groupName'], "groupWaitTime": row["groupWaitTime"], "groupShell": row["groupShell"]} for row in groupInformation.find(groupSelect)]


def pythonErrorMessage(errorMessageValue):
    couch = couchdb.Server(DBURI)
    pythonErrorLog = couch['python_error_log']
    pythonErrorLog.save(errorMessageValue)


def shellErrorMessage(errorMessageValue):
    couch = couchdb.Server(DBURI)
    shellErrorLog = couch['shell_error_log']
    shellErrorLog.save(errorMessageValue)

