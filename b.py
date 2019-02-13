#coding=utf-8
import re
def checkHomeWork(msg, partten):
    if re.match(partten, msg) != None:
        return True
    return False
#print(check('^\s*###作业###(周|日)作业###\d{8}###.+', '###作业###日作业###20180221###🚗 🚗 🚗 🚗 🚗'))
print(checkHomeWork('###作业###日作业###20180221###🚗 🚗 🚗 🚗 🚗', '^\s*###作业###(周|日)作业###\d{8}###.+'))
