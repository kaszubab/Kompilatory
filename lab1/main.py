import sys
import ply.yacc as yacc
import scanner
import Mparser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(
            sys.argv) > 1 else "lab5_examples/example2.m"
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

    interpreter = Interpreter()
    interpreter.visit(ast)

