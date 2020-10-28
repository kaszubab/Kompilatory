import ply.lex as lex

# List of token names.   This is always required
tokens = [
    "DOTADD",
    "DOTSUB",
    "DOTMUL",
    "DOTDIV",
    "ADDASSIGN",
    "SUBASSIGN",
    "MULASSIGN",
    "DIVASSIGN",
    "LT",
    "GT",
    "LE",
    "GE",
    "NEQ",
    "EQ",
    "ID",
    "INT",
    "FLOAT",
    "STRING"
]

# key words
reserved = {
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'if': "IF",
    'else': "ELSE",
    'for': "FOR",
    'while': "WHILE",
    'return': "RETURN",
    'eye': "EYE",
    'zeros': "ZEROS",
    'ones': "ONES",
    'print': "PRINT"
}

literals = "+-*/=()\{\}[]:',;"
tokens = tokens + list(reserved.values())

t_ignore = ' \t'

t_ignore_COMMENT = r'\#.*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


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


# identifiers
def t_ID(t):
    r'[a-zA-Z_](\w|_)*'
    t.type = reserved.get(t.value, "ID")
    return t

# floats
def t_FLOAT(t):
    r'(([1-9][0-9]*|0)\.[0-9]*|\.[0-9]+)(E[0-9]+)?'
    t.value = float(t.value)
    return t


# Integers
def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# strings
t_STRING = r'\"[^\"]*\"'


# errors
def t_error(t):
    print("error", t.value)


# Build the lexer
lexer = lex.lex()
