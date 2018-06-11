import re


def regex_match_indices(regex, text):
    return [(x.start(), x.end()) for x in re.finditer(regex, text)]
