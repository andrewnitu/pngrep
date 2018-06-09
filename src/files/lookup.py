from unipath import Path
from ocr import ocr
from datetime import datetime
from termcolor import colored
import db.db as db

FILENAME_COLOR = 'green'


def __absolute_path_string(path):
    return str(path.absolute())


def __file_name_string(path):
    return path.name


# Returns a formatted and colored string of results, including the filename of each result
def lookup_no_cache(string, filenames):
    files = map(lambda x: Path(x), filenames)

    answer = ""

    for file in files:
        answer += colored(file.name + ": ", FILENAME_COLOR)
        answer += db.read_file_text(__absolute_path_string(file)).text
        answer += "\n"

    return answer


# Returns a formatted and colored string of results, including the filename of each result
def lookup_with_cache(string, filenames):
    files = map(lambda x: Path(x), filenames)

    answer = ""

    for file in files:
        absolute_path_string = __absolute_path_string(file)
        file_name_string = __file_name_string(file)

        # if there's no cache entry
        if not db.exists_file_text(absolute_path_string):
            current_text = ocr.get_text(absolute_path_string)
            answer += colored(file_name_string + ": ", FILENAME_COLOR)
            answer += ocr.get_text(absolute_path_string)
            answer += "\n"
            db.save_file_text(absolute_path_string, current_text)
        # if there's an old cache entry (before the file was updated)
        elif db.read_file_text(absolute_path_string).updated_date < \
                datetime.fromtimestamp(file.stat().st_mtime):
            current_text = ocr.get_text(absolute_path_string)
            answer += colored(file_name_string + ": ", FILENAME_COLOR)
            answer += ocr.get_text(absolute_path_string)
            answer += "\n"
            db.clear_file_text(absolute_path_string)
            db.save_file_text(absolute_path_string, current_text)
        # if the cache entry is current
        else:
            answer += colored(file_name_string + ": ", FILENAME_COLOR)
            answer += db.read_file_text(absolute_path_string).text
            answer += "\n"

    return answer
