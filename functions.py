#coding=utf-8
import re
import time 

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

def checkWorkDate(date):
    if len(date) != 8:
        return '作业日期格式不对, 日期为8位数字，如20001010'
    elif date > time.strftime('%Y%m%d', time.localtime(time.time())):
        return '作业日期过大'
    else:
        return True
