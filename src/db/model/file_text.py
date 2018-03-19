import peewee


class FileText(peewee.Model):
    path = peewee.CharField()
    text = peewee.CharField()
