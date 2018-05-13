from unipath import Path
from ocr import ocr


def __absolute_path(path):
    absolute_path = Path(path).absolute()
    return str(absolute_path)


def lookup_no_cache(string, files):
    files = map(lambda x: __absolute_path(x), files)

    answer = ""

    for file in files:
        answer += ocr.get_text(file)

    return answer
