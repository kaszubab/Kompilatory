import sys
import ply.lex as lex
import scanner  # scanner.py is a file you create, (it is not an external library)

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    to_file = False
    if to_file:
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
        to_file and file_handle.write("(%d,%d): %s(%s)\n" % (tok.lineno, column, tok.type, tok.value))
        print("(%d,%d): %s(%s)" % (tok.lineno, column, tok.type, tok.value))
