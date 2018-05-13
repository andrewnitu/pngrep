import peewee
from datetime import datetime
from db.model.file_text import FileText
from unipath import Path


def init():
    global database
    database = peewee.SqliteDatabase("storage.db")
    try:
        FileText.create_table()
    except peewee.OperationalError:
        pass


def __absolute_path(path):
    absolute_path = Path(path).absolute()
    return str(absolute_path)


def save_file_text(path, text):
    file_text = FileText(__absolute_path(path), text, datetime.now)
    file_text.save()


def read_file_text(path):
    file_text = FileText.get(FileText.path == __absolute_path(path))
    return file_text


def clear_all_file_text():
    FileText.delete()


def clear_file_text(path):
    FileText.delete().where(FileText.path == __absolute_path(path))
