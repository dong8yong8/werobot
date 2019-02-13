#coding=utf-8
import re
def checkHomeWork(msg, partten):
    if re.match(partten, msg) != None:
        return True
    return False

def checkYDShare(url, partten):
    if re.match(partten, url) != None:
        return True
    return False

def splitWorkMsg(workMsg):
    workMsgList = workMsg.split('###')
    returnDic = {
        'workDate':    workMsgList[3],
        'workKey':     workMsgList[2],
        'workMessage': workMsgList[4]
    } 

    return returnDic
