from Mysql import Mysql

class GroupMsg(Mysql):
    table = 'aide_group_msg'

    def addMsg(self, msgInfo=[]):
        fields = 'group_id, group_name, friend_id, friend_nick_name, message, work_type, work_date, work_key, work_message'
        msgInfo.insert(0, fields)
        msgInfo.insert(0, self.table)
        sql = 'insert into %s (%s) values(%d, "%s", %d, "%s", "%s", %d, "%s", "%s", "%s")' % tuple(msgInfo)
        self.execute(sql)
        return
