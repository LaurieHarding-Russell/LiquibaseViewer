class LiquibaseChangeLog(object):
    name = ""
    changeSets = []


class LiquibaseChangeSet(object):
    id = ""
    context = ""
    author = ""