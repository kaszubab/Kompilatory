import sys
import ply.yacc as yacc
import scanner
import Mparser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(
            sys.argv) > 1 else "lab3_examples/example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    # ast.printTree()
    typeChecker = TypeChecker()   
    typeChecker.visit(ast)
