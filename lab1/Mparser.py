#!/usr/bin/python

import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("left", "LT", "GT", "LE", "GE", "NEQ", "EQ"),
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", 'DOTADD', 'DOTSUB'),
    ("left", 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),
    ('left', "\'"),
    ("nonassoc", 'IFX'),
    ("nonassoc", 'ELSE'),
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
                   | control_instruction
                   | print
                   | block
    """

def p_print_instruction(p):
    """print : PRINT row ';'
    """

def p_row(p):
    """row : row ',' expr
          | row ',' boolean
          | expr
          | boolean
    """

def p_control_instruction(p):
    """control_instruction : if
                           | while
                           | for
                           | break
                           | continue
                           | return
    """

def p_break_instruction(p):
    """break : BREAK ';'"""

def p_continue_instruction(p):
    """continue : CONTINUE ';'"""

def p_return_instruction(p):
    """return : RETURN expr ';'"""

def p_for(p):
    """for : FOR ID '=' range instruction"""

def p_range_operator(p):
    """range : expr ':' expr """

def p_while(p):
    """while : WHILE '(' boolean ')' instruction """

def p_if(p):
    """if : IF '(' boolean ')' instruction %prec IFX
          | IF '(' boolean ')' instruction else
    """

def p_else(p):
    """else : ELSE instruction
    """

def p_instructions_block(p):
    """block : '{' instructions '}' """

def p_assignment(p):
    """assignment : id_part '=' expr
                  | id_part '=' boolean
                  | id_part ADDASSIGN expr
                  | id_part SUBASSIGN expr
                  | id_part MULASSIGN expr
                  | id_part DIVASSIGN expr
    """

def p_id_index(p):
    """id_part : ID '[' matrix_row ']'
               | ID
    """


def p_parentheses(p):
    """expr : '(' expr ')'
    """

def p_relational_operators(p):
    """boolean : expr LT expr
               | expr GT expr
               | expr LE expr
               | expr GE expr
               | expr NEQ expr
               | expr EQ expr
    """

def p_matrix_transposition(p):
    """expr : expr "\'"
    """

def p_expr_uminus(p):
    """expr : '-' expr %prec UMINUS"""

def p_matrix_operators(p):
    """expr : expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr
    """

def p_binary_operators(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
    """

def p_expr_def(p):
    """expr : ID
            | STRING
            | FLOAT
            | INT
    """

def p_matrix(p):
    """expr : EYE '(' expr ')'
              | ZEROS '(' expr ')'
              | ONES '(' expr ')'
              | '[' matrix_rows ']'
    """

def p_matrix_rows(p):
    """matrix_rows : matrix_rows ',' '[' matrix_row ']'
                    | '[' matrix_row ']'
    """

def p_matrix_row(p):
    """matrix_row : matrix_row ',' expr
                   | expr
    """






# to finish the grammar
# ....


parser = yacc.yacc()

