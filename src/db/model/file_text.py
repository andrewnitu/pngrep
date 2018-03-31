import peewee

database = peewee.SqliteDatabase("storage.db")


class FileText(peewee.Model):
    path = peewee.CharField()
    text = peewee.CharField()

    class Meta:
        database = database
