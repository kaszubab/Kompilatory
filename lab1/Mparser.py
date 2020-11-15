#!/usr/bin/python

import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("left", '+', '-', 'DOTADD', 'DOTSUB'),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),
    ('left', 'TRANSPOSE')
    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """

def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """

def p_instruction(p):
    """instruction : assignment ';'
                   | print ';'
                   | control_instruction
    """

def p_control_instruction(p):
    """control_instruction : if
    """

def p_if(p):
    """if : IF '(' boolean ')' instruction
          | IF '(' boolean ')' block
          | IF '(' boolean ')' instruction else
          | IF '(' boolean ')' block else
    """

def p_else(p):
    """else : ELSE instruction
            | ELSE block
    """

def p_instructions_block(p):
    """block : '{' instructions '}' """


def p_print(p):
    """print : PRINT  expr
             | PRINT  ID
             | PRINT  STRING
             | PRINT  assignment
    """

def p_assignment(p):
    """assignment : ID '=' expr
                  | ID '=' STRING
                  | ID '=' boolean
                  | ID ADDASSIGN expr
                  | ID SUBASSIGN expr
                  | ID MULASSIGN expr
                  | ID DIVASSIGN expr
    """

def p_parentheses(p):
    """expr : '(' expr ')'
            | '[' expr ']'
            | '{' expr '}'
    """


def p_expr_uminus(p):
    """expr : '-' expr %prec UMINUS"""

def p_expr(p):
    """expr : bin_expr
            | matrix_expr
    """


def p_matrix_operators(p):
    """matrix_expr : matrix_expr DOTADD matrix_expr
                   | matrix_expr DOTSUB matrix_expr
                   | matrix_expr DOTMUL matrix_expr
                   | matrix_expr DOTDIV matrix_expr
                   | matrix_expr TRANSPOSE
                   | matrix
    """

def p_matrix(p):
    """matrix : EYE '(' bin_expr ')'
              | ZEROS '(' bin_expr ')'
              | ONES '(' bin_expr ')'
              | '[' matrix_rows ']'
              | ID

    """

def p_matrix_rows(p):
    """matrix_rows : matrix_rows ',' '[' matrix_row ']'
                    | '[' matrix_row ']'
    """

def p_matrix_row(p):
    """matrix_row : matrix_row ',' bin_expr
                   | bin_expr
    """

def p_boolean(p):
    """boolean : ID
    """
def p_relational_operators(p):
    """boolean : bin_expr LT bin_expr
               | bin_expr GT bin_expr
               | bin_expr LE bin_expr
               | bin_expr GE bin_expr
               | bin_expr NEQ bin_expr
               | bin_expr EQ bin_expr
    """

def p_binary_operators(p):
    """bin_expr : bin_expr '+' bin_expr
            | bin_expr '-' bin_expr
            | bin_expr '*' bin_expr
            | bin_expr '/' bin_expr
    """

def p_bin_expr(p):
    """bin_expr : INT
                | FLOAT
                | ID
    """




# to finish the grammar
# ....


parser = yacc.yacc()

