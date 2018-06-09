from unipath import Path
from ocr import ocr
from datetime import datetime
import db.db as db


def __absolute_path(path):
    absolute_path = Path(path).absolute()
    return str(absolute_path)


def lookup_no_cache(string, files):
    files = map(lambda x: __absolute_path(x), files)

    answer = ""

    for file in files:
        answer += ocr.get_text(file)

    return answer


def lookup_with_cache(string, files):
    files = map(lambda x: __absolute_path(x), files)

    answer = ""

    for file in files:
        if not db.exists_file_text(file):
            current_text = ocr.get_text(file)
            answer += ocr.get_text(file)
            db.save_file_text(file, current_text)
        elif db.read_file_text(file).updated_date < datetime.fromtimestamp(Path(file).stat().st_mtime):
            current_text = ocr.get_text(file)
            answer += ocr.get_text(file)
            db.clear_file_text(file)
            db.save_file_text(file, current_text)
        else:
            answer += db.read_file_text(file).text

    return answer
