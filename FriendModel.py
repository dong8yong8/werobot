from Mysql import Mysql

class Friend(Mysql):
    table = 'aide_friend'

    def getFriendByName(self, friendName, groupId):
        sql = 'select * from %s where group_id=%d and nick_name="%s"' % (self.table,friendName, groupId)
        friend = self.getOne(sql)
        return friend

    def addFriend(self, friendInfo=[]):
        fields = 'group_id, group_name, nick_name'
        friendInfo.insert(0, fields)
        friendInfo.insert(0, self.table)
        sql = 'insert into %s (%s) values(%d, "%s", "%s")' % tuple(friendInfo)
        self.execute(sql)
        return
