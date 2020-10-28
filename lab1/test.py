import sys
import re

if __name__ == '__main__':

    try:
        file = open("log_file.txt", "r")
        result = open("result_text.txt", "w")
    except IOError:
        sys.exit(0)

    last_line = 1

    for line in file.readlines():
        hits = re.findall("\(([0-9]+),[0-9]+\).*?\((.*)\)", line)[0]
        if last_line != hits[0]:
            result.write("\n"*(int(hits[0]) - last_line))
            last_line = int(hits[0])
        result.write("{} ".format(hits[1]))
