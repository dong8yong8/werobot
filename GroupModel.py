from Mysql import Mysql

class Group(Mysql):
    table = 'aide_group'

    def getGroupByName(self, groupName):
        sql = 'select * from %s where name="%s"' % (self.table, groupName)
        group = self.getOne(sql)

        return group
