#!/usr/bin/python

import scanner
from AST import *
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
    p[0] = Print(p[2])

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
    p[0] = Break()

def p_continue_instruction(p):
    """continue : CONTINUE ';'"""
    p[0] = Continue()

def p_return_instruction(p):
    """return : RETURN expr ';'"""
    p[0] = Return(p[2])

def p_for(p):
    """for : FOR ID '=' range instruction"""
    p[0] = For(Variable(p[2]), p[3], p[4])

def p_range_operator(p):
    """range : expr ':' expr """
    p[0] = Range(p[1], p[3])

def p_while(p):
    """while : WHILE '(' boolean ')' instruction """
    p[0] = While(p[3], p[5])

def p_if(p):
    """if : IF '(' boolean ')' instruction %prec IFX
          | IF '(' boolean ')' instruction else 
    """
    if len(p) == 6:
        p[0] = If(p[3], p[5], None)
    else:
        p[0] = If(p[3], p[5], p[6])
        
def p_else(p):
    """else : ELSE instruction
    """
    p[0] = Else(p[2])

def p_instructions_block(p):
    """block : '{' instructions '}' """
    p[0] = Block(p[2])

def p_assignment(p):
    """assignment : id_part '=' expr
                  | id_part '=' boolean
                  | id_part ADDASSIGN expr
                  | id_part SUBASSIGN expr
                  | id_part MULASSIGN expr
                  | id_part DIVASSIGN expr
    """
    p[0] = Assigment(p[2], p[1], p[3])

def p_id_index(p):
    """id_part : ID '[' matrix_row ']'
               | ID
    """
    if len(p) == 2:
        p[0] = Variable(p[1])
    else:
        p[0] = Ref(p[1], p[3])


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
    p[0] = Comparsion(p[2], p[1], p[3])

def p_matrix_transposition(p):
    """expr : expr "\'"
    """
    p[0] = Transposition(p[0])


def p_expr_uminus(p):
    """expr : '-' expr %prec UMINUS"""
    p[0] = UnaryMinus(p[2])

def p_matrix_operators(p):
    """expr : expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr
    """
    p[0] = BinExpr(p[2], p[1], p[3])

def p_binary_operators(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
    """
    p[0] = BinExpr(p[2], p[1], p[3])

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
    if len(p) == 5:
        p[0] = MartixInitalization(p[1], p[3])
    else:
        p[0] = Vector([2])

def p_matrix_rows(p):
    """matrix_rows : matrix_rows ',' '[' matrix_row ']'
                    | '[' matrix_row ']'
    """
    if len(p) == 4:
        p[0] = Vector(p[2])
    else:
        p[0] = Vector(p[4])

def p_matrix_row(p):
    """matrix_row : matrix_row ',' expr
                   | expr
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[3]






# to finish the grammar
# ....


parser = yacc.yacc()

