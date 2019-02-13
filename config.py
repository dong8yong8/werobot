#coding=utf-8

GROUPNAME   = '💤' #要抓取的群名称
IS_WORK     = 1 #作业消息
IS_NOT_WORK = 0 #非作业消息

database = {
        'host': 'localhost', 
        'user': 'root', 
        'passwd': '123456', 
        'db': 'we', 
        'charset': 'utf8mb4', 
        'port': 3306
}

workPartten = '^\s*###作业###(周|日)作业###\d+###.+'
youdaoBaseUrl = 'https:\/\/note\.youdao\.com.*'

