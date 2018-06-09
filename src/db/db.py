import peewee
from datetime import datetime
from db.model.file_text import FileText
from unipath import Path


def init():
    try:
        FileText.create_table()
    except peewee.OperationalError:
        pass


def __absolute_path(path):
    absolute_path = Path(path).absolute()
    return str(absolute_path)


def __last_modified_microseconds(path):
    return Path(path).stat().st_mtime


def save_file_text(path, text):
    file_text = FileText(path=__absolute_path(path),
                         text=text,
                         updated_date=datetime.fromtimestamp(__last_modified_microseconds(path)))
    file_text.save()


def exists_file_text(path):
    return FileText.select().where(FileText.path == __absolute_path(path)).exists()


def read_file_text(path):
    file_text = FileText.get(FileText.path == __absolute_path(path))
    return file_text


def clear_all_file_text():
    FileText.delete().execute()


def clear_file_text(path):
    FileText.delete().where(FileText.path == __absolute_path(path)).execute()
