import matching.regex as regex
from termcolor import colored

FILENAME_COLOR = 'green'
REGEX_COLOR = 'red'


def format_results(results, regex_string):
    output = ""

    for result in results:
        lines = result[1].splitlines()

        for line in lines:
            regex_match_indices = regex.regex_match_indices(regex_string, line)

            if not regex_match_indices:
                continue

            output += colored(result[0] + ": ", FILENAME_COLOR)

            for i in range(0, len(line)):
                if any(lower <= i < upper for (lower, upper) in regex_match_indices):
                    output += colored(line[i], REGEX_COLOR)
                else:
                    output += line[i]

            output += "\n"

    return output