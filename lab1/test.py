import sys
import re
import scanner

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    file_handle = open("log_file.txt", "w")
    text = file.read()
    lexer = scanner.lexer
    lexer.input(text)  # Give the lexer some input

    # Tokenize

    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        column = scanner.find_column(text, tok)
        file_handle.write("(%d,%d): %s(%s)\n" % (tok.lineno, column, tok.type, tok.value))

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
