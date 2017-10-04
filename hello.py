# Created by Fabian Montemayor

# Token list
reserved = {
    # Value types
    'int' : 'INT',
    'decimal' : 'DECIMAL',
    'boolean' : 'BOOL',
    'void' : 'VOID',
    'false' : 'FALSE',
    'true' : 'TRUE',

    # Logical operators
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',

    # Key words
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'list' : 'LIST',
    'function' : 'FUNC',
    'return' : 'RETURN',
    'print' : 'PRINT',
    'readto' : 'READ',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
}

tokens = [
    # Constant values
    'C_INT',
    'C_DEC',
    'C_STR',
    'C_BOOL',
    'ID',

    # Arithmetic operators
    'ASSIGN',
    'PLUS', 'MINUS',
    'MULT', 'DIV',
    # 'DOT', 'EX',

    # Rel operators
    'GT', 'GE', 'LT', 'LE', 'EE', 'NE',

    # Others
    'COLON', 'SCOLON', 'COMMA',
    'LK', 'RK',
    'LB', 'RB',
    'LP', 'RP',
]

tokens += reserved.values()

# Token regular expressions
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
#t_DOT = r'\.'
#t_EX = r'(E | e)'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_EE = r'=='
t_NE = r'!='
t_COLON = r':'
t_SCOLON = r';'
t_COMMA = r'\,'
t_LK = r'{'
t_RK = r'}'
t_LB = r'\['
t_RB = r'\]'
t_LP = r'\('
t_RP = r'\)'
t_C_STR = r'\"[^\"]*\"'

def t_ID(t):
    r'[a-zA-Z]([a-zA-Z0-9])*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_C_DEC(t):
    r'[0-9]+\.[0-9]+([Ee][\+-]?[0-9]+)?'
    #r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Decimal value too large %d", t.value)
        t.value = 0
    return t

def t_C_INT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_C_BOOL(t):
    r'(false | true)'
    t.value = bool(t.value)
    return t

# Ignored characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

# Building the lexer
import ply.lex as lex
lexer = lex.lex()

# Test example
data = '''
var int numero, decimal expo;
program programa 
{
    print(numero + 2);
    0a;
    &&
    3.423
    expo = 1.345;
    expo = 2.3E3;
}
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


# PARSER

# Grammar Rules
