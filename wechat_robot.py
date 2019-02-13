#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import itchat, time
import json
import Mysql
import socket
from datetime import datetime
from functions import *
from GroupModel import Group
from GroupMsgModel import GroupMsg
from FriendModel import Friend
from itchat.content import *
from config import *


#个人消息
#@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print '=============================================='
    print (msg.ActualNickName)
    print(msg.type)
    print(msg.text)
    #msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)
#
#@itchat.msg_register(FRIENDS)
#def add_friend(msg):
#    msg.user.verify()
#    msg.user.send('Nice to meet you!')

#群消息
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def text_reply(msg):
    #自己发言则直接返回
#    if msg.ActualNickName==msg.User.Self.NickName or msg.ActualNickName=='': return 
    #不是指定群直接返回
    if msg.User.NickName != GROUPNAME: return

#    print(json.dumps(msg))
    print '-----------------------------------'
    print('===群===%s' % msg.User.NickName)
    print (msg.ActualNickName)
    print(msg.text)

    #链接数据库
    #获取群
#    groupModel = Group()
#    group = groupModel.getGroupByName(msg.User.NickName)
#    groupId = group[0]
#
#    #获取成员信息
#    friendModel = Friend()
#    friend = friendModel.getFriendByName(groupId, msg.ActualNickName)
#    if friend == None:
#        friendModel.addFriend([groupId, msg.User.NickName, msg.ActualNickName])
#        newFriendId = friendModel.cursor.lastrowid
#    else:
#        newFriendId = friend[0]
#
#    # 查看是不是作业
#    workType    = IS_NOT_WORK
#    workDate    = '20000101'
#    workKey     = ''
#    workMessage = ''
#    if checkHomeWork(msg.text.encode('utf8'), workPartten):
#        workType    = IS_WORK
#        msgDic      = splitWorkMsg(msg.text)
#        workDate    = msgDic['workDate']
#        workKey     = msgDic['workKey']
#        workMessage = msgDic['workMessage']
#    elif msg.Url != '':
#        if checkYDShare(msg.Url.encode('utf8'), youdaoBaseUrl):
#            msgDic      = splitWorkMsg(msg.text)
#            workDate    = msgDic['workDate']
#            workKey     = msgDic['workKey']
#            workMessage = msg.Url
#
     #检查日期格式
#     res = checkWorkDate(workDate)
#     if res != True:
#         msg.user.send('@%s %s' % (msg.ActualNickName, res))
     
#    #存消息
#    groupmsgModel = GroupMsg()
#    msgData = [groupId, msg.User.NickName, newFriendId, msg.ActualNickName, msg.text, workType, datetime.strptime(workDate, '%Y%m%d'), workKey, workMessage]
#    groupmsgModel.addMsg(msgData)


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(True)
