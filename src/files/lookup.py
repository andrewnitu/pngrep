from unipath import Path
from processing import processing
from datetime import datetime
from processing.processing_params import ProcessingParams
import db.db as db
from files.reason import Reason


def __absolute_path_string(path):
    return str(path.absolute())


def __file_name_string(path):
    return path.name


# Returns an array of files and their text
def lookup_no_cache(filenames, parallel):
    files = list(map(lambda x: Path(x), filenames))

    return zip(map(lambda y: __file_name_string(y), files),
               map(lambda a: a.text,
                   processing.get_batch_text(map(lambda b: ProcessingParams(0, __absolute_path_string(b), 0), files),
                                             parallel)))


# Returns an array of files and their text
def lookup_with_cache(filenames, parallel):
    files = map(lambda x: Path(x), filenames)

    answer = []
    to_process = []

    for index, file in enumerate(files):
        absolute_path_string = __absolute_path_string(file)
        file_name_string = __file_name_string(file)

        # if there's no cache entry
        if not db.exists_file_text(absolute_path_string):
            to_process.append(ProcessingParams(index, absolute_path_string, Reason.no_cache_entry))
            answer.append([file_name_string, absolute_path_string])

        # if there's an old cache entry (before the file was updated)
        elif db.read_file_text(absolute_path_string).updated_date < \
                datetime.fromtimestamp(file.stat().st_mtime):
            to_process.append(ProcessingParams(index, absolute_path_string, Reason.outdated_cache_entry))
            answer.append([file_name_string, absolute_path_string])

        # if the cache entry is current
        else:
            answer.append([file_name_string, db.read_file_text(absolute_path_string).text])

    results = processing.get_batch_text(to_process, parallel)

    for result in results:
        index = result.index
        text = result.text
        reason = result.reason

        file_name_string = answer[index][0]
        absolute_path_string = answer[index][1]
        answer[index] = [file_name_string, text]

        if reason == Reason.outdated_cache_entry:
            db.save_file_text(absolute_path_string, text)
        elif reason == Reason.no_cache_entry:
            db.clear_file_text(absolute_path_string)
            db.save_file_text(absolute_path_string, text)

    return answer
