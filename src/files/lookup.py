from unipath import Path
from ocr import ocr
from datetime import datetime
import db.db as db


def __absolute_path_string(path):
    return str(path.absolute())


def __file_name_string(path):
    return path.name


# Returns an array of files and their text
def lookup_no_cache(filenames):
    files = map(lambda x: Path(x), filenames)

    answer = []

    for file in files:
        answer.append((__file_name_string(file), ocr.get_text(__absolute_path_string(file))))

    return answer


# Returns an array of files and their text
def lookup_with_cache(filenames):
    files = map(lambda x: Path(x), filenames)

    answer = []

    for file in files:
        absolute_path_string = __absolute_path_string(file)
        file_name_string = __file_name_string(file)

        # if there's no cache entry
        if not db.exists_file_text(absolute_path_string):
            current_text = ocr.get_text(absolute_path_string)
            answer.append((file_name_string, ocr.get_text(absolute_path_string)))
            db.save_file_text(absolute_path_string, current_text)
        # if there's an old cache entry (before the file was updated)
        elif db.read_file_text(absolute_path_string).updated_date < \
                datetime.fromtimestamp(file.stat().st_mtime):
            current_text = ocr.get_text(absolute_path_string)
            answer.append((file_name_string, ocr.get_text(absolute_path_string)))
            db.clear_file_text(absolute_path_string)
            db.save_file_text(absolute_path_string, current_text)
        # if the cache entry is current
        else:
            answer.append((file_name_string, db.read_file_text(absolute_path_string).text))

    return answer
