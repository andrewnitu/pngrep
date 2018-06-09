import peewee


class FileText(peewee.Model):
    path = peewee.CharField()
    text = peewee.CharField()
    updated_date = peewee.DateTimeField()

    class Meta:
        database = peewee.SqliteDatabase("../pngrep.sqlite")
