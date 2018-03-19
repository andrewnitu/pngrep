import peewee
from src.db.model.file_text import FileText


database = peewee.SqliteDatabase("storage.db")


def init(db_name):
    global database
    database = peewee.SqliteDatabase(db_name)
    try:
        FileText.create_table()
    except peewee.OperationalError:
        pass


def save_file_text(path, text):
    file_text = FileText(path, text)
    file_text.save()


def read_file_text(path):
    text = FileText.get(FileText.path == path)
    return text


def clear_all_file_text():
    FileText.delete()


def clear_file_text(path):
    FileText.delete().where(FileText.path == path)
