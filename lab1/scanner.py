# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV',
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'LPAREN',
    'RPAREN',
)

# binary operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# matrix binary operators
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'

# assignment operators
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

# relational operators
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NEQ = r'!='
t_EQ = r'=='

# brackets
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQBRACKET = r'\('
t_ = r'\('
t_LPAREN = r'\('
t_LPAREN = r'\('

#spread
t_LPAREN = r'\('
t_RPAREN = r'\)'



# Build the lexer
lexer = lex.lex()