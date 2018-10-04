[![Build Status](https://travis-ci.org/andrewnitu/pngrep.svg?branch=master)](https://travis-ci.org/andrewnitu/pngrep)

## About ##
`pngrep` is a CLI utility similar to `grep`, just that it operates on images instead of text. It's intended to extract certain lines from images (and in the future PDFs) for easy searching of scanned papers, documents, etc. It supports similar syntax to `grep` as well as regex.

## Syntax ##
Invoke `pngrep` with `python3 src/__main.py__` from the root directory.

From here, invoke a subcommand. Current subcommands are `search` and `clear`. If you do not explicitly invoke a subcommand, `search` is assumed by default.

#### search ####
This is the main function of pngrep.

The general syntax should look like:
```
python3 src/__main__.py [FLAGS] PATTERN [FILES]
```

The flags that are currently supported are:
- `-p (--parallel)`: Will run the OCR in parallel on a per-file basis, thus if you are only scanning one file this should have negligible effect. However, if you are scanning more than a handful of files it will make the OCR phase significantly faster. It will use all available cores/threads on your CPU.
- `-n (--no-cached)`: Avoids using the SQLite cache to lookup the text.

`PATTERN` should be a string or regex, very similar to `grep`.

`FILES` should simply be the list of all the files you want to scan in. Both absolute and relative paths are supported.

#### clear ####
The `clear` subcommand simply clears the local SQLite cache, such that any subsequent searches will need to re-scan the images.

### How It Works ###
`pngrep` starts with the `click` Python library. It parses the command line options and parameters.

Next, the request is passed to the lookup handler, which handles most of the logic. It checks in the SQLite database for previous records of the requested files, and uses that info if it exists and is not outdated.

Otherwise, it makes a call to `tesseract` to scan the files and return the text. Parallel processing here is enabled by the `multiprocessing` module from the `pythos` module. The results are then stored in the SQLite database for later retrieval.

Lastly, the output is matched for the given string/regex and highlighted before printing to the console.
