# Created by Fabian Montemayor
import sys
from Constants import *
from Cube import *
from Functions import *
from pprint import pprint


# Variables
functionDirectory = {}  # { functionName : { functionType, {varTable} }
                        # varTable = { varName : { type } }
currentScope = ''
currentType = ''
quadCounter = 0
quadruples = []         # { operation, term1, term2, result }
operandStack = []
operatorStack = []
typesStack = []
temporalCounter = 0

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
        print("Decimal value too large {}".format(t.value))
        t.value = 0
    return t

def t_c_int(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large {}".format(t.value))
        t.value = 0
    return t

def t_id(t):
    r'[a-zA-Z]([a-zA-Z0-9])*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_error(t):
    print("Illegal character '{}'".format(t.value[0]))
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
    '''PROGRAM : SEM_CODE_STARTS DECLARATIONS FUNCTIONS program id BLOCK'''
    print("Parse successful")

def p_DECLARATIONS(p):
    '''DECLARATIONS : VARDEC DECLARATIONS
                    | LISTDEC DECLARATIONS
                    | empty'''

def p_VARDEC(p):
    '''VARDEC : var TYPE VARIDS semicolon'''

def p_VARIDS(p):
    '''VARIDS : id SEM_ADD_VAR
              | id SEM_ADD_VAR comma VARIDS'''

def p_LISTDEC(p):
    '''LISTDEC : list TYPE VARIDS semicolon'''

def p_TYPE(p):
    '''TYPE : int SEM_STORE_TYPE
            | decimal SEM_STORE_TYPE
            | bool SEM_STORE_TYPE'''

def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
                 | empty'''

def p_FUNCTION(p):
    '''FUNCTION : function FUNCTYPE id SEM_ADD_FUNC lp FUNCPARAMETERS rp lk DECLARATIONS STATEMENTS rk SEM_END_FUNC'''

def p_FUNCTYPE(p):
    '''FUNCTYPE : void SEM_STORE_TYPE
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
    '''ASSIGN : id SEM_PUSH_OPERAND LISTINDEX equal SEM_PUSH_OPERATOR EXPRESSION SEM_ASSIGN semicolon'''

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
    '''EXP : TERM SEM_RESOLVE_PLUSMINUS
           | TERM SEM_RESOLVE_PLUSMINUS plus SEM_PUSH_OPERATOR EXP
           | TERM SEM_RESOLVE_PLUSMINUS minus SEM_PUSH_OPERATOR EXP'''

def p_TERM(p):
    '''TERM : FACTOR SEM_RESOLVE_TIMESDIVIDE
            | FACTOR SEM_RESOLVE_TIMESDIVIDE times SEM_PUSH_OPERATOR TERM
            | FACTOR SEM_RESOLVE_TIMESDIVIDE divide SEM_PUSH_OPERATOR TERM'''

def p_FACTOR(p):
    '''FACTOR : lp SEM_PUSH_PAREN EXPRESSION rp SEM_POP_PAREN
              | CONSTANT
              | plus CONSTANT
              | minus CONSTANT'''

def p_CONSTANT(p):
    '''CONSTANT : id SEM_PUSH_OPERAND LISTINDEX
                | id SEM_PUSH_OPERAND lp CALLPARAMETERS rp
                | c_int SEM_PUSH_CONSTANT
                | c_decimal SEM_PUSH_CONSTANT
                | c_string SEM_PUSH_CONSTANT
                | false SEM_PUSH_CONSTANT
                | true SEM_PUSH_CONSTANT'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error at '{}', '{}'".format(p.value, p))


#### SEMANTICS #####

def p_SEM_CODE_STARTS(p):
    '''SEM_CODE_STARTS : empty'''
    global functionDirectory, currentScope, currentType
    currentScope = 'global'
    currentType = Types.Void
    functionDirectory[currentScope] = { 'type' : currentType, 'varTable' : {}}

def p_SEM_STORE_TYPE(p):
    '''SEM_STORE_TYPE : empty'''
    global currentType
    t = p[-1]
    if t == 'int':
        currentType = Types.Int
    elif t == 'decimal':
        currentType = Types.Decimal
    elif t == 'bool':
        currentType = Types.Bool
    elif t == 'void':
        currentType = Types.Void
    else:
        pass
    # print(currentType)

def p_SEM_ADD_FUNC(p):
    '''SEM_ADD_FUNC : empty'''
    global currentScope
    functionName = p[-1]
    # Check if function doesn't already exist
    if functionDirectory.has_key(functionName):
        print("Function '{}' has already been declared".format(functionName))
        exit(1)
    else:
        # Create function
        functionDirectory[functionName] = {'type' : currentType, 'varTable' : {} }
        currentScope = functionName

def p_SEM_END_FUNC(p):
    '''SEM_END_FUNC : empty'''
    global functionDirectory
    pprint(functionDirectory)
    functionDirectory[currentScope]['varTable'].clear()

def p_SEM_ADD_VAR(p):
    '''SEM_ADD_VAR : empty'''
    varName = p[-1]
    if functionDirectory['global']['varTable'].has_key(varName) or functionDirectory[currentScope]['varTable'].has_key(varName):
        print("Variable '{}' has already been declared".format(varName))
        exit(1)
    else:
        functionDirectory[currentScope]['varTable'][varName] = {'type' : currentType}    

def p_SEM_PUSH_OPERAND(p):
    '''SEM_PUSH_OPERAND : empty'''
    operand = p[-1]
    operandStack.append(operand)
    # print("Push '%s' to operand stack" % operand)

    if functionDirectory[currentScope]['varTable'].has_key(operand):
        t = functionDirectory[currentScope]['varTable'][operand]['type']
        typesStack.append(t)
    elif functionDirectory['global']['varTable'].has_key(operand):
        t = functionDirectory['global']['varTable'][operand]['type']
        typesStack.append(t)
    else:
        print("Error: Undeclared variable '{}'".format(operand))
        # exit(1)
    
    # printStacks(operatorStack, operandStack, typesStack)
    # print(" ")

def p_SEM_PUSH_OPERATOR(p):
    '''SEM_PUSH_OPERATOR : empty'''
    operator = p[-1]
    opCode = getOperationCode(operator)
    # print("Push '%s' to operation stack" % operator)
    operatorStack.append(opCode)
    # printStacks(operatorStack, operandStack, typesStack)
    # print(" ")

def p_SEM_RESOLVE_PLUSMINUS(p):
    '''SEM_RESOLVE_PLUSMINUS : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.Plus or top[0] == Operations.Minus:
            quad = generateQuad(operatorStack, operandStack, typesStack, temporalCounter, quadCounter)
            quadruples.append(quad)
            temporalCounter = temporalCounter + 1
            quadCounter = quadCounter + 1

def p_SEM_RESOLVE_TIMESDIVIDE(p):
    '''SEM_RESOLVE_TIMESDIVIDE : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.Times or top[0] == Operations.Divide:
            quad = generateQuad(operatorStack, operandStack, typesStack, temporalCounter, quadCounter)
            quadruples.append(quad)
            temporalCounter = temporalCounter + 1
            quadCounter = quadCounter + 1

def p_SEM_PUSH_PAREN(p):
    '''SEM_PUSH_PAREN : empty'''
    operatorStack.append(Operations.Parenthesis)

def p_SEM_POP_PAREN(p):
    '''SEM_POP_PAREN : empty'''
    operatorStack.pop()

def p_SEM_ASSIGN(p):
    '''SEM_ASSIGN : empty'''
    global quadCounter
    operation = operatorStack.pop()
    term1 = operandStack.pop()
    type1 = typesStack.pop()
    result = operandStack.pop()
    resultType = typesStack.pop()
    if type1 == resultType:
        quad = buildQuad(operation, term1, Operations.Null, result)
        quadruples.append(quad)
        quadCounter = quadCounter + 1

def p_SEM_PUSH_CONSTANT(p):
    '''SEM_PUSH_CONSTANT : empty'''
    
    operand = p[-1]
    operandStack.append(str(operand))
    

    if operand == 'false' or operand == 'true':
        typesStack.append(Types.Bool)
    else:
        found = False
        try:
            value = int(operand)
            print(value)
            typesStack.append(Types.Int)
            found = True
        except ValueError:
            pass
        
        if not found:
            try:
                value = float(operand)
                typesStack.append(Types.Decimal)
                found = True
            except ValueError:
                pass
        
        if not found:
            typesStack.append(Types.String)
    printStacks(operatorStack, operandStack, typesStack)
    print(" ")

# Building the parser with a test
import ply.yacc as yacc

filename = "test2.txt"

parser = yacc.yacc()

# Print tokens
def printTokens():
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

printQuads(quadruples)