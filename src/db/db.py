import peewee
from db.model.file_text import FileText


def init():
    global database
    database = peewee.SqliteDatabase("storage.db")
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
