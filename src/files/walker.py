import os
import stat

def walktree(path):
    files = []

    for entry in os.scandir(path):
        if entry.is_file():
            files.append(entry)

    files = map(lambda x: x.stat, files)

