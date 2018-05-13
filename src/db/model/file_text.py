import peewee

database = peewee.SqliteDatabase("storage.db")


class FileText(peewee.Model):
    path = peewee.CharField()
    text = peewee.CharField()
    updated_date = peewee.DateTimeField()

    class Meta:
        database = database
