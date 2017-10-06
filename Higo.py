# Created by Fabian Montemayor
import sys




############ LEXER ############

# Token list
reserved = {
    # Value types
    'int' : 'int',
    'decimal' : 'decimal',
    'bool' : 'bool',
    'void' : 'void',
    'false' : 'false',
    'true' : 'true',

    # Logical operators
    'and' : 'and',
    'or' : 'or',
    'not' : 'not',

    # Key words
    'program' : 'program',
    'var' : 'var',
    'list' : 'list',
    'function' : 'function',
    'return' : 'return',
    'print' : 'print',
    'readto' : 'readto',
    'if' : 'if',
    'else' : 'else',
    'while' : 'while',
}

tokens = [
    # Constant values
    'c_int',
    'c_decimal',
    'c_string',
    'id',

    # Arithmetic operators
    'equal',
    'plus', 'minus',
    'times', 'divide',

    # Relational operators
    'gt', 'ge', 'lt', 'le', 'ee', 'ne',

    # Others
    'semicolon', 'comma',
    'lk', 'rk',
    'lb', 'rb',
    'lp', 'rp',
]

tokens += reserved.values()

# Token regular expressions
t_equal = r'\='
t_plus = r'\+'
t_minus = r'\-'
t_times = r'\*'
t_divide = r'\/'
t_gt = r'\>'
t_ge = r'\>\='
t_lt = r'\<'
t_le = r'\<\='
t_ee = r'\=\='
t_ne = r'\!\='
t_semicolon = r'\;'
t_comma = r'\,'
t_lk = r'\{'
t_rk = r'\}'
t_lb = r'\['
t_rb = r'\]'
t_lp = r'\('
t_rp = r'\)'
t_c_string = r'\"[^\"]*\"'

def t_c_decimal(t):
    r'[0-9]+\.[0-9]+([Ee][\+-]?[0-9]+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Decimal value too large %d", t.value)
        t.value = 0
    return t

def t_c_int(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_id(t):
    r'[a-zA-Z]([a-zA-Z0-9])*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'

t_ignore = ' \t'

# Building the lexer
import ply.lex as lex
lexer = lex.lex()


############ PARSER ############

# Grammar Rules

def p_PROGRAM(p):
    '''PROGRAM : DECLARATIONS FUNCTIONS program id BLOCK'''
    print("Parse successful")

def p_DECLARATIONS(p):
    '''DECLARATIONS : VARDEC DECLARATIONS
                    | LISTDEC DECLARATIONS
                    | empty'''

def p_VARDEC(p):
    '''VARDEC : var TYPE VARIDS semicolon'''

def p_VARIDS(p):
    '''VARIDS : id 
              | id comma VARIDS'''

def p_LISTDEC(p):
    '''LISTDEC : list TYPE VARIDS semicolon'''

def p_TYPE(p):
    '''TYPE : int
            | decimal
            | bool'''

def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
                 | empty'''

def p_FUNCTION(p):
    '''FUNCTION : function FUNCTYPE id lp FUNCPARAMETERS rp lk DECLARATIONS STATEMENTS rk'''

def p_FUNCTYPE(p):
    '''FUNCTYPE : void
                | TYPE'''

def p_FUNCPARAMETERS(p):
    '''FUNCPARAMETERS : TYPE id
                      | TYPE id comma FUNCPARAMETERS
                      | empty'''

def p_BLOCK(p):
    '''BLOCK : lk STATEMENTS rk'''

def p_STATEMENTS(p):
    '''STATEMENTS : STATEMENT STATEMENTS
                  | empty'''

def p_STATEMENT(p):
    '''STATEMENT : ASSIGN
                 | READ
                 | PRINT
                 | FUNCCALL
                 | CONDITION
                 | LOOP 
                 | RETURN'''

def p_ASSIGN(p):
    '''ASSIGN : id LISTINDEX equal EXPRESSION semicolon'''

def p_LISTINDEX(p):
    '''LISTINDEX : lb EXP rb LISTINDEX
                 | empty'''

def p_READ(p):
    '''READ : readto lp id rp semicolon'''

def p_PRINT(p):
    '''PRINT : print lp EXPRESSION rp semicolon'''

def p_FUNCCALL(p):
    '''FUNCCALL : id lp CALLPARAMETERS rp semicolon'''

def p_CALLPARAMETERS(p):
    '''CALLPARAMETERS : EXPRESSION
                      | EXPRESSION comma CALLPARAMETERS
                      | empty'''

def p_CONDITION(p):
    '''CONDITION : if lp EXPRESSION rp BLOCK ELSEBLOCK'''

def p_ELSEBLOCK(p):
    '''ELSEBLOCK : else BLOCK
                 | empty'''

def p_LOOP(p):
    '''LOOP : while lp EXPRESSION rp BLOCK'''

def p_RETURN(p):
    '''RETURN : return EXPRESSION semicolon'''
                
def p_EXPRESSION(p):
    '''EXPRESSION : NOT SUPEREXP
                  | NOT SUPEREXP and NOT SUPEREXP
                  | NOT SUPEREXP or NOT SUPEREXP'''

def p_NOT(p):
    '''NOT : not 
           | empty'''

def p_SUPEREXP(p):
    '''SUPEREXP : EXP
                | EXP RELOP EXP'''

def p_RELOP(p):
    '''RELOP : gt
             | ge
             | lt
             | le
             | ee
             | ne'''

def p_EXP(p): 
    '''EXP : TERM
           | TERM plus TERM
           | TERM minus TERM'''

def p_TERM(p):
    '''TERM : FACTOR
            | FACTOR times FACTOR
            | FACTOR divide FACTOR'''

def p_FACTOR(p):
    '''FACTOR : lp EXPRESSION rp
              | CONSTANT
              | plus CONSTANT
              | minus CONSTANT'''

def p_CONSTANT(p):
    '''CONSTANT : id LISTINDEX
                | id lp CALLPARAMETERS rp
                | c_int
                | c_decimal
                | c_string
                | false
                | true'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error at '%s', '%s'" % (p.value, p))

# Building the parser with a test
import ply.yacc as yacc

filename = "test1.txt"

parser = yacc.yacc()

# Print tokens
with open(filename, 'r') as f:
    input = f.read()
    lexer.input(input)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Parse
with open(filename, 'r') as f:
    input = f.read()
    print(parser.parse(input, lexer=lexer))