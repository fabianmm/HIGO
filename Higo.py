# Created by Fabian Montemayor
import sys
from Constants import *
from Cube import *
from Functions import *
from pprint import pprint
from VirtualMachine import *

filename = "./Tests/program-5.txt"

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
eraStack = []
temporalCounter = 0
jumpStack = []
paramCounter = 0
currentFunction = ''
negative = False
currentSign = None

# Address counters
globalVarCount = {}
globalVarCount['int'] = AddressStart.Global.Int
globalVarCount['decimal'] = AddressStart.Global.Decimal
globalVarCount['bool'] = AddressStart.Global.Bool
globalVarCount['listint'] = AddressStart.Global.ListInt
globalVarCount['listdec'] = AddressStart.Global.ListDec
globalVarCount['listbool'] = AddressStart.Global.ListBool

localVarCount = {}

tempVarCount = {}


# -----------------------------------------------------
# ----------------------- LEXER -----------------------
# -----------------------------------------------------

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

    # Lists
    'add' : 'add',
    'remove' : 'remove',
    'sort' : 'sort',
    'find' : 'find',
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
    'semicolon', 'comma', 'dot',
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
t_dot = r'\.'
t_c_string = r'[\'\"][^\'^\"]*[\'\"]'

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


# -----------------------------------------------------
# ---------------------- PARSER -----------------------
# -----------------------------------------------------

# Grammar Rules

def p_PROGRAM(p):
    '''PROGRAM : SEM_CODE_STARTS DECLARATIONS FUNCTIONS program id SEM_PROGRAM_STARTS BLOCK SEM_FILL_ERAS SEM_PROGRAM_END'''

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
    '''LISTDEC : list TYPE LISTIDS semicolon'''

def p_LISTIDS(p):
    '''LISTIDS : id SEM_ADD_LIST
               | id SEM_ADD_LIST comma LISTIDS'''

def p_TYPE(p):
    '''TYPE : int SEM_STORE_TYPE
            | decimal SEM_STORE_TYPE
            | bool SEM_STORE_TYPE'''

def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
                 | empty'''

def p_FUNCTION(p):
    '''FUNCTION : function FUNCTYPE id SEM_ADD_FUNC lp FUNCPARAMETERS rp lk DECLARATIONS SEM_ADD_FUNC_START STATEMENTS rk SEM_END_FUNC'''

def p_FUNCTYPE(p):
    '''FUNCTYPE : void SEM_STORE_TYPE
                | TYPE'''

def p_FUNCPARAMETERS(p):
    '''FUNCPARAMETERS : TYPE id SEM_ADD_PARAM
                      | TYPE id SEM_ADD_PARAM comma FUNCPARAMETERS
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
                 | RETURN
                 | LISTADD
                 | LISTREMOVE
                 | LISTSORT'''

def p_ASSIGN(p):
    '''ASSIGN : id SEM_PUSH_OPERAND LISTINDEX equal SEM_PUSH_OPERATOR EXPRESSION SEM_ASSIGN semicolon'''

def p_LISTINDEX(p):
    '''LISTINDEX : lb EXP rb SEM_LIST_INDEX
                 | empty'''

def p_READ(p):
    '''READ : readto SEM_PUSH_OPERATOR lp id SEM_PUSH_OPERAND SEM_GEN_READ rp semicolon'''

def p_PRINT(p):
    '''PRINT : print SEM_PUSH_OPERATOR lp EXPRESSION rp SEM_PRINT semicolon'''

def p_FUNCCALL(p):
    '''FUNCCALL : id SEM_VERIFY_FUNC lp SEM_GEN_ERA CALLPARAMETERS rp SEM_VERIFY_NUM_PARAMS semicolon SEM_GEN_GOSUB'''

def p_CALLPARAMETERS(p):
    '''CALLPARAMETERS : EXPRESSION SEM_MATCH_PARAM
                      | EXPRESSION SEM_MATCH_PARAM comma CALLPARAMETERS
                      | empty'''

def p_CONDITION(p):
    '''CONDITION : if lp EXPRESSION rp SEM_GEN_GOTOF BLOCK ELSEBLOCK SEM_FILL_END'''

def p_ELSEBLOCK(p):
    '''ELSEBLOCK : else SEM_GENANDFILL_GOTO BLOCK
                 | empty'''

def p_LOOP(p):
    '''LOOP : while SEM_PUSH_START lp EXPRESSION rp SEM_GEN_GOTOF BLOCK SEM_FILL_LOOP'''

def p_RETURN(p):
    '''RETURN : return EXPRESSION SEM_RETURN semicolon'''
                
def p_EXPRESSION(p):
    '''EXPRESSION : NOT SUPEREXP SEM_RESOLVE_NOT
                  | NOT SUPEREXP SEM_RESOLVE_NOT and SEM_PUSH_OPERATOR NOT SUPEREXP SEM_RESOLVE_NOT SEM_RESOLVE_ANDOR
                  | NOT SUPEREXP SEM_RESOLVE_NOT or SEM_PUSH_OPERATOR NOT SUPEREXP SEM_RESOLVE_NOT SEM_RESOLVE_ANDOR'''

def p_NOT(p):
    '''NOT : not SEM_PUSH_OPERATOR
           | empty'''

def p_SUPEREXP(p):
    '''SUPEREXP : EXP
                | EXP RELOP EXP SEM_RESOLVE_RELOP'''

def p_RELOP(p):
    '''RELOP : gt SEM_PUSH_OPERATOR
             | ge SEM_PUSH_OPERATOR
             | lt SEM_PUSH_OPERATOR
             | le SEM_PUSH_OPERATOR
             | ee SEM_PUSH_OPERATOR
             | ne SEM_PUSH_OPERATOR'''

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
              | plus SEM_PUSH_SIGN CONSTANT
              | minus SEM_PUSH_SIGN CONSTANT'''

def p_CONSTANT(p):
    '''CONSTANT : id SEM_PUSH_OPERAND LISTINDEX
                | id SEM_VERIFY_FUNC lp SEM_PUSH_PAREN SEM_GEN_ERA CALLPARAMETERS rp SEM_POP_PAREN SEM_VERIFY_NUM_PARAMS SEM_GEN_GOSUB_ASSIGN
                | c_int SEM_PUSH_CONSTANT
                | c_decimal SEM_PUSH_CONSTANT
                | c_string SEM_PUSH_CONSTANT
                | false SEM_PUSH_CONSTANT
                | true SEM_PUSH_CONSTANT
                | id SEM_PUSH_OPERAND dot find lp SEM_PUSH_PAREN EXP rp SEM_POP_PAREN SEM_LIST_FIND'''

def p_LISTADD(p):
    '''LISTADD : id SEM_PUSH_OPERAND dot add lp SEM_PUSH_PAREN EXP rp SEM_POP_PAREN SEM_ADD_TO_LIST semicolon'''

def p_LISTREMOVE(p):
    '''LISTREMOVE : id SEM_PUSH_OPERAND LISTINDEX dot remove semicolon SEM_REMOVE_FROM_LIST'''

def p_LISTSORT(p):
    '''LISTSORT : id SEM_PUSH_OPERAND dot sort semicolon SEM_SORT_LIST'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error at '{}', '{}', '{}".format(p.value, p.lineno, p))
    exit(1)

# -----------------------------------------------------
# --------------------- SEMANTICS ---------------------
# -----------------------------------------------------

# -------- BREAKPOINTS ---------

# Creates first 4 quadruples: 3 global eras & goto main
#   Sets curent scope to global and current type to void
def p_SEM_CODE_STARTS(p):
    '''SEM_CODE_STARTS : empty'''
    global functionDirectory, currentScope, currentType, quadCounter
    currentScope = 'global'
    currentType = Types.Void
    functionDirectory[currentScope] = { 'type' : currentType, 'varTable' : {}}
    newQuad(quadruples, Operations.GlobalEra, None, None, None)
    newQuad(quadruples, Operations.GlobalEra, None, None, None)
    newQuad(quadruples, Operations.GlobalEra, None, None, None)
    newQuad(quadruples, Operations.Goto, None, None, None)
    quadCounter += 4
    tempVarCount[currentScope] = {}
    tempVarCount[currentScope]['int'] = AddressStart.Temp.Int
    tempVarCount[currentScope]['decimal'] = AddressStart.Temp.Decimal
    tempVarCount[currentScope]['bool'] = AddressStart.Temp.Bool

# Fills Goto main
def p_SEM_PROGRAM_STARTS(p):
    '''SEM_PROGRAM_STARTS : empty'''
    global currentScope, currentType
    currentScope = 'global'
    currentType = Types.Void
    # Fill initial Goto to main
    fill(3, quadCounter, quadruples)

def p_SEM_PROGRAM_END(p):
    '''SEM_PROGRAM_END : empty'''
    global quadCounter
    # End Quadruple
    newQuad(quadruples, Operations.End, None, None, None)
    quadCounter += 1
    # Get global var counts and fill first era
    globalInts = globalVarCount['int'] - AddressStart.Global.Int
    globalDecs = globalVarCount['decimal'] - AddressStart.Global.Decimal
    globalBools = globalVarCount['bool'] - AddressStart.Global.Bool
    quadruples[0]['left'] = globalInts
    quadruples[0]['right'] = globalDecs
    quadruples[0]['result'] = globalBools
    # Get global temporal var counts and fill second era
    tempInts = tempVarCount['global']['int'] - AddressStart.Temp.Int
    tempDecs = tempVarCount['global']['decimal'] - AddressStart.Temp.Decimal
    tempBools = tempVarCount['global']['bool'] - AddressStart.Temp.Bool
    quadruples[1]['left'] = tempInts
    quadruples[1]['right'] = tempDecs
    quadruples[1]['result'] = tempBools
    # Get global list counts and fill third era
    listInts = globalVarCount['listint'] - AddressStart.Global.ListInt
    listdecs = globalVarCount['listdec'] - AddressStart.Global.ListDec
    listBools = globalVarCount['listbool'] - AddressStart.Global.ListBool
    quadruples[2]['left'] = listInts
    quadruples[2]['right'] = listdecs
    quadruples[2]['result'] = listBools

# --------- Stack pushers / Storers ---------

# Stores newly declared type
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
        print("Error: Cannot recognize type {}".format(t))
        exit(1)

# Pushes operator to the stack
def p_SEM_PUSH_OPERATOR(p):
    '''SEM_PUSH_OPERATOR : empty'''
    operator = p[-1]
    opCode = getOperationCode(operator)
    operatorStack.append(opCode)

# Pushes a parenthesis to the stack
def p_SEM_PUSH_PAREN(p):
    '''SEM_PUSH_PAREN : empty'''
    operatorStack.append(Operations.Parenthesis)

# Pops a parenthesis from the stack
def p_SEM_POP_PAREN(p):
    '''SEM_POP_PAREN : empty'''
    operatorStack.pop()

# Pushes a constant value to the stack, with '#' as a prefix
def p_SEM_PUSH_CONSTANT(p):
    '''SEM_PUSH_CONSTANT : empty''' 
    global currentSign   
    operand = p[-1]  
    if operand == 'false' or operand == 'true':
        if currentSign != None:
            print("Cannot precede a boolean constant with a sign.")
            exit(1)
        typesStack.append(Types.Bool)
        newOperand = "#" + str(operand)
        operandStack.append(newOperand) 
    elif isinstance(operand, float):
        typesStack.append(Types.Decimal)
        if currentSign == '-':
            operand = '-' + operand
            currentSign = None
        newOperand = "#" + str(operand)
        operandStack.append(newOperand) 
    elif isinstance(operand, int):
        typesStack.append(Types.Int)
        if currentSign == '-':
            operand = '-' + operand
            currentSign = None
        newOperand = "#" + str(operand)
        operandStack.append(newOperand) 
    else:
        # Quitar comillas
        if currentSign != None:
            print("Cannot precede a string constant with a sign.")
            exit(1)
        newOperand = "#" + operand.strip("\"").strip("\'")
        operandStack.append(newOperand) 
        typesStack.append(Types.String)

# Pushes an operand to the stack, generally a variable
def p_SEM_PUSH_OPERAND(p):
    '''SEM_PUSH_OPERAND : empty'''
    operand = p[-1]
    if currentSign != None:
        print("Cannot precede a variable  with a sign.")
        exit(1)
    if functionDirectory[currentScope]['varTable'].has_key(operand):
        t = functionDirectory[currentScope]['varTable'][operand]['type']
        o = functionDirectory[currentScope]['varTable'][operand]['address']
        typesStack.append(t)
        operandStack.append(o)
    elif functionDirectory['global']['varTable'].has_key(operand):
        t = functionDirectory['global']['varTable'][operand]['type']
        o = functionDirectory['global']['varTable'][operand]['address']
        typesStack.append(t)
        operandStack.append(o)
    else:
        print("Error: Undeclared variable '{}'".format(operand))
        exit(1)

def p_SEM_PUSH_SIGN(p):
    '''SEM_PUSH_SIGN : empty'''
    global currentSign
    sign = p[-1]
    if sign == '+':
        currentSign = '+'
    else:
        currentSign = '-'

# ------------ Expressions ------------

# Resolves a '+' or '-'
def p_SEM_RESOLVE_PLUSMINUS(p):
    '''SEM_RESOLVE_PLUSMINUS : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.Plus or top[0] == Operations.Minus:
            right = operandStack.pop()
            left = operandStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()
            resultType = Cube[operator, leftType, rightType]
            if resultType >= 0:
                newQuad(quadruples, operator, left, right, tempVarCount[currentScope][getTypeFromCode(resultType)])
                quadCounter += 1
                operandStack.append(tempVarCount[currentScope][getTypeFromCode(resultType)])
                typesStack.append(resultType)
                tempVarCount[currentScope][getTypeFromCode(resultType)] += 1
            else:
                print("Operation type mismatch: {} {} {}".format(getTypeFromCode(leftType), operator, getTypeFromCode(rightType)))
                exit(1)

# Resolves a '*' or '/'
def p_SEM_RESOLVE_TIMESDIVIDE(p):
    '''SEM_RESOLVE_TIMESDIVIDE : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.Times or top[0] == Operations.Divide:
            right = operandStack.pop()
            left = operandStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()
            resultType = Cube[operator, leftType, rightType]
            if resultType >= 0:
                newQuad(quadruples, operator, left, right, tempVarCount[currentScope][getTypeFromCode(resultType)])
                quadCounter += 1
                operandStack.append(tempVarCount[currentScope][getTypeFromCode(resultType)])
                typesStack.append(resultType)
                tempVarCount[currentScope][getTypeFromCode(resultType)] += 1
            else:
                print("Operation type mismatch: {} {} {}".format(getTypeFromCode(leftType), operator, getTypeFromCode(rightType)))
                exit(1)

# Resolves a relational operation
def p_SEM_RESOLVE_RELOP(p):
    '''SEM_RESOLVE_RELOP : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.GreaterThan or top[0] == Operations.GreaterEqual or top[0] == Operations.LessThan or top[0] == Operations.LessEqual or top[0] == Operations.Equal or top[0] == Operations.NotEqual:
            right = operandStack.pop()
            left = operandStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()
            resultType = Cube[operator, leftType, rightType]
            if resultType >= 0:
                newQuad(quadruples, operator, left, right, tempVarCount[currentScope][getTypeFromCode(resultType)])
                quadCounter += 1
                operandStack.append(tempVarCount[currentScope][getTypeFromCode(resultType)])
                typesStack.append(resultType)
                tempVarCount[currentScope][getTypeFromCode(resultType)] += 1
            else:
                print("Operation type mismatch: {} {} {}".format(getTypeFromCode(leftType), operator, getTypeFromCode(rightType)))
                exit(1)

# Resolves an 'and' or 'or'
def p_SEM_RESOLVE_ANDOR(p):
    '''SEM_RESOLVE_ANDOR : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.And or top[0] == Operations.Or:
            right = operandStack.pop()
            left = operandStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()
            resultType = Cube[operator, leftType, rightType]
            if resultType >= 0:
                newQuad(quadruples, operator, left, right, tempVarCount[currentScope][getTypeFromCode(resultType)])
                quadCounter += 1
                operandStack.append(tempVarCount[currentScope][getTypeFromCode(resultType)])
                typesStack.append(resultType)
                tempVarCount[currentScope][getTypeFromCode(resultType)] += 1
            else:
                print("Operation type mismatch: {} {} {}".format(getTypeFromCode(leftType), operator, getTypeFromCode(rightType)))
                exit(1)

# Resolves a 'not'
def p_SEM_RESOLVE_NOT(p):
    '''SEM_RESOLVE_NOT : empty'''
    global temporalCounter, quadCounter
    top = operatorStack[-1:]
    if top:
        if top[0] == Operations.Not:
            left = operandStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()
            if leftType == Types.Bool:
                newQuad(quadruples, operator, left, None, tempVarCount[currentScope][getTypeFromCode(Types.Bool)])
                quadCounter += 1
                operandStack.append(tempVarCount[currentScope][getTypeFromCode(Types.Bool)])
                typesStack.append(Types.Bool)
                tempVarCount[currentScope][getTypeFromCode(Types.Bool)] += 1
            else:
                print("Operation type mismatch: {} {}".format(operator, getTypeFromCode(leftType)))
                exit(1)

# ------------- Variables -------------

# Adds a variable to the varTable
def p_SEM_ADD_VAR(p):
    '''SEM_ADD_VAR : empty'''
    varName = p[-1]
    if functionDirectory['global']['varTable'].has_key(varName) or functionDirectory[currentScope]['varTable'].has_key(varName):
        print("Variable '{}' has already been declared".format(varName))
        exit(1)
    else:
        functionDirectory[currentScope]['varTable'][varName] = {'type' : currentType, 'address' : 0}   
        if currentScope == 'global':
            functionDirectory[currentScope]['varTable'][varName]['address'] = globalVarCount[getTypeFromCode(currentType)]
            globalVarCount[getTypeFromCode(currentType)] += 1
        else:
            functionDirectory[currentScope]['varTable'][varName]['address'] = localVarCount[currentScope][getTypeFromCode(currentType)]
            localVarCount[currentScope][getTypeFromCode(currentType)] += 1

# ------------- Simple Expressions -------------

# Assigns a value to a variable
def p_SEM_ASSIGN(p):
    '''SEM_ASSIGN : empty'''
    global quadCounter
    operation = operatorStack.pop()
    left = operandStack.pop()
    leftType = typesStack.pop()
    result = operandStack.pop()
    resultType = typesStack.pop()
    if Cube[Operations.Assign, resultType, leftType] >= 0:
        newQuad(quadruples, operation, left, None, result)
        quadCounter += 1
    else:
        print("Error: Cannot assign type {} to {}".format(getTypeFromCode(leftType), getTypeFromCode(resultType)))
        exit(1)

# Reads from input into a variable
def p_SEM_GEN_READ(p):
    '''SEM_GEN_READ : empty'''
    global quadCounter
    varName = operandStack.pop()
    varType = typesStack.pop()
    if functionDirectory.has_key(varName):
        print("Error: Cannot read to a function.")
        exit(1)
    elif functionDirectory[currentScope]['varTable'].has_key(varName):
        newQuad(quadruples, Operations.Read, None, None, varName)
    else:
        print("Error: Cannot read to an unknown identifier {}".format(varName))
        
# Prints a value
def p_SEM_PRINT(p):
    '''SEM_PRINT : empty'''
    global quadCounter
    operation = operatorStack.pop()
    typesStack.pop()
    result = operandStack.pop()
    newQuad(quadruples, operation, None, None, result)
    quadCounter += 1

# ------------- Conditions / Loops -------------

# Creates the GotoF quadruple
def p_SEM_GEN_GOTOF(p):
    '''SEM_GEN_GOTOF : empty'''
    global quadCounter
    top = operandStack[-1:]
    if top:
        exp = operandStack.pop()
        expType = typesStack.pop()
        if expType != Types.Bool:
            print("Error: Expression not boolean")
            exit(1)
        else:
            newQuad(quadruples, Operations.GotoF, exp, None, None)
            quadCounter += 1
            jumpStack.append(quadCounter - 1)

# Creates a Goto and fills a previous empty Goto
def p_SEM_GENANDFILL_GOTO(p):
    '''SEM_GENANDFILL_GOTO : empty'''
    global quadCounter
    newQuad(quadruples, Operations.Goto, None, None, None)
    quadCounter += 1
    jumpToFill = jumpStack.pop()
    jumpStack.append(quadCounter - 1)
    fill(jumpToFill, quadCounter, quadruples)

# Fills the last goto
def p_SEM_FILL_END(p):
    '''SEM_FILL_END : empty'''
    end = jumpStack.pop()
    fill(end, quadCounter, quadruples)

# Pushes the start of the loop
def p_SEM_PUSH_START(p):
    '''SEM_PUSH_START : empty'''
    jumpStack.append(quadCounter)

# Fills the loop gotos
def p_SEM_FILL_LOOP(p):
    '''SEM_FILL_LOOP : empty'''
    global quadCounter
    end = jumpStack.pop()
    ret = jumpStack.pop()
    newQuad(quadruples, Operations.Goto, None, None, ret)
    quadCounter += 1
    fill(end, quadCounter, quadruples)

# ------------- Functions -------------

# Adds function to the function directory
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
        functionDirectory[functionName] = {'type' : currentType, 'params' : [], 'numParams' : 0, 'numVars' : 0, 'varTable' : {}, 'int' : 0, 'decimal': 0, 'bool': 0 , 'quadStart' : quadCounter}
        currentScope = functionName
        localVarCount[functionName] = {}
        localVarCount[functionName]['int'] = AddressStart.Local.Int
        localVarCount[functionName]['decimal'] = AddressStart.Local.Decimal
        localVarCount[functionName]['bool'] = AddressStart.Local.Bool
        localVarCount[functionName]['listint'] = AddressStart.Local.ListInt
        localVarCount[functionName]['listdec'] = AddressStart.Local.ListDec
        localVarCount[functionName]['listbool'] = AddressStart.Local.ListBool
        tempVarCount[functionName] = {}
        tempVarCount[functionName]['int'] = AddressStart.Temp.Int
        tempVarCount[functionName]['decimal'] = AddressStart.Temp.Decimal
        tempVarCount[functionName]['bool'] = AddressStart.Temp.Bool

# Creates the end function quad
def p_SEM_END_FUNC(p):
    '''SEM_END_FUNC : empty'''
    global functionDirectory, quadCounter
    functionDirectory[currentScope]['varTable'].clear()
    newQuad(quadruples, Operations.EndProc, None, None, None)
    quadCounter += 1

# Adds a parameter to the varTable
def p_SEM_ADD_PARAM(p):
    '''SEM_ADD_PARAM : empty'''
    paramName = p[-1]
    functionDirectory[currentScope]['varTable'][paramName] = { 'type' : currentType, 'address' : localVarCount[currentScope][getTypeFromCode(currentType)] }
    functionDirectory[currentScope]['params'].append(currentType)
    functionDirectory[currentScope]['numParams'] += 1
    localVarCount[currentScope][getTypeFromCode(currentType)] += 1

# Adds the initial function quadruple
def p_SEM_ADD_FUNC_START(p):
    '''SEM_ADD_FUNC_START : empty'''
    functionDirectory[currentScope]['quadStart'] = quadCounter

# Verifies the the function called exists
def p_SEM_VERIFY_FUNC(p):
    '''SEM_VERIFY_FUNC : empty'''
    global currentFunction
    funcName = p[-1]
    if not functionDirectory.has_key(funcName):
        print("Error: Function {} does not exist".format(funcName))
        exit(1)
    else:
        currentFunction = funcName

# Creates the Era quadruples
def p_SEM_GEN_ERA(p):
    '''SEM_GEN_ERA : empty'''
    global paramCounter, quadCounter, currentFunction
    paramCounter = 0
    ints = localVarCount[currentFunction]['int'] - AddressStart.Local.Int
    decimals = localVarCount[currentFunction]['decimal'] - AddressStart.Local.Decimal
    bools = localVarCount[currentFunction]['bool'] - AddressStart.Local.Bool
    listInts = localVarCount[currentFunction]['listint'] - AddressStart.Local.ListInt
    listDecs = localVarCount[currentFunction]['listdec'] - AddressStart.Local.ListDec
    listBools = localVarCount[currentFunction]['listbool'] - AddressStart.Local.ListBool
    newQuad(quadruples, Operations.Era, ints, decimals, bools)
    newQuad(quadruples, Operations.Era, currentFunction, None, None)
    newQuad(quadruples, Operations.Era, listInts, listDecs, listBools)
    eraStack.append(quadCounter+1)
    quadCounter += 3

# Matches argument types with param types
def p_SEM_MATCH_PARAM(p):
    '''SEM_MATCH_PARAM : empty'''
    global paramCounter, quadCounter, currentFunction
    argument = operandStack.pop()
    argumentType = typesStack.pop()
    if functionDirectory[currentFunction]['numParams'] > 0:
        paramType = functionDirectory[currentFunction]['params'][paramCounter]
        if paramType != argumentType:
            print("Error: Argument sent does not match expected type. Sent {}, expected {}".format(getTypeFromCode(argumentType), getTypeFromCode(paramType)))
            exit(1)
        else:
            newQuad(quadruples, Operations.Param, argument, getTypeFromCode(argumentType), paramCounter)
            quadCounter += 1
            paramCounter += 1
    else:
        print("Error: function does not take parameters.")
        exit(1)

# Verifies the number of parameters was sent correctly
def p_SEM_VERIFY_NUM_PARAMS(p):
    '''SEM_VERIFY_NUM_PARAMS : empty'''
    global paramCounter
    if paramCounter != functionDirectory[currentFunction]['numParams']:
        print("Error: Expected {} but got {} parameters".format(functionDirectory[currentFunction]['numParams'], paramCounter))
        exit(1)

# Creates the Gosub quadruple
def p_SEM_GEN_GOSUB(p):
    '''SEM_GEN_GOSUB : empty'''
    global quadCounter
    newQuad(quadruples, Operations.GoSub, currentFunction, None, functionDirectory[currentFunction]['quadStart'])
    quadCounter += 1

# Creates the Gosub quadruple and the assignment of the return variable to a temporary variable 
def p_SEM_GEN_GOSUB_ASSIGN(p):
    '''SEM_GEN_GOSUB_ASSIGN : empty'''
    global quadCounter
    newQuad(quadruples, Operations.GoSub, currentFunction, None, functionDirectory[currentFunction]['quadStart'])
    quadCounter += 1
    globalFuncVarAddress = functionDirectory['global']['varTable'][currentFunction]['address']
    returnType = functionDirectory['global']['varTable'][currentFunction]['type']
    # Temporal assignment of global variable of that func name
    newQuad(quadruples, Operations.Assign, globalFuncVarAddress, None, tempVarCount[currentScope][getTypeFromCode(returnType)])
    quadCounter += 1
    operandStack.append(tempVarCount[currentScope][getTypeFromCode(returnType)])
    typesStack.append(returnType)
    tempVarCount[currentScope][getTypeFromCode(returnType)] += 1

# Creates the return quadruple
def p_SEM_RETURN(p):
    '''SEM_RETURN : empty'''
    global quadCounter
    funcType = functionDirectory[currentScope]['type']
    returnType = typesStack.pop()
    returnValue = operandStack.pop()
    if funcType != returnType:
        print("Error: Function should return {} type".format(getTypeFromCode(funcType)))
        exit(1)
    else:
        # Create global variable for function return
        if not functionDirectory['global']['varTable'].has_key(currentScope):
            functionDirectory['global']['varTable'][currentScope] =  {'type' : returnType, 'address' : 0} 
            functionDirectory['global']['varTable'][currentScope]['address'] = globalVarCount[getTypeFromCode(returnType)]
            globalVarCount[getTypeFromCode(returnType)] += 1
        
        varAddress = functionDirectory['global']['varTable'][currentScope]['address']
        # Create quad
        newQuad(quadruples, Operations.Return, returnValue, None, varAddress)
        newQuad(quadruples, Operations.EndProc, None, None, None)
        quadCounter += 2
        
# Fills temporal eras with the correct values
def p_SEM_FILL_ERAS(p):
    '''SEM_FILL_ERAS : empty'''
    while eraStack[-1:]:
        quadNum = eraStack.pop()
        funcName = quadruples[quadNum]['left']
        tempInts = tempVarCount[funcName]['int'] - AddressStart.Temp.Int
        tempDecs = tempVarCount[funcName]['decimal'] - AddressStart.Temp.Decimal
        tempBools = tempVarCount[funcName]['bool'] - AddressStart.Temp.Bool
        quadruples[quadNum]['left'] = tempInts
        quadruples[quadNum]['right'] = tempDecs
        quadruples[quadNum]['result'] = tempBools

# -------------- Lists -----------------

# Adds a list to the varTable
def p_SEM_ADD_LIST(p):
    '''SEM_ADD_LIST : empty'''
    listName = p[-1]
    # Check if it already exists
    if functionDirectory['global']['varTable'].has_key(listName) or functionDirectory[currentScope]['varTable'].has_key(listName):
        print("List '{}' has already been declared".format(listName))
        exit(1)
    else:
        # Add list name to varTable
        functionDirectory[currentScope]['varTable'][listName] = {'type' : currentType, 'address' : 0}   
        # Update address and counts
        if currentScope == 'global':
            functionDirectory[currentScope]['varTable'][listName]['address'] = globalVarCount[getListTypeFromCode(currentType)]
            globalVarCount[getListTypeFromCode(currentType)] += 1
        else:
            functionDirectory[currentScope]['varTable'][listName]['address'] = localVarCount[currentScope][getListTypeFromCode(currentType)]
            localVarCount[currentScope][getListTypeFromCode(currentType)] += 1

# Concats the list address with the index address in the format '&LISTADDRESS,INDEXADDRESS'
def p_SEM_LIST_INDEX(p):
    '''SEM_LIST_INDEX : empty'''
    # Get list id and index exp
    global quadCounter
    index = operandStack.pop()
    indexType = typesStack.pop()
    listId = operandStack.pop()
    listType = typesStack.pop()
    
    if indexType != Types.Int:
        print("Error: List index {} needs to be an integer".format(index))
        exit(1)
    else:
        operandStack.append("&" + str(listId) + ',' + str(index))
        typesStack.append(listType)

# Creates the .add quadruple
def p_SEM_ADD_TO_LIST(p):
    '''SEM_ADD_TO_LIST : empty'''
    # Check exp to add is of the same type as list
    global quadCounter
    value = operandStack.pop()
    valueType = typesStack.pop()
    listId = operandStack.pop()
    listType = typesStack.pop()
    if Cube[Operations.Assign, listType, valueType] >= 0:
        newQuad(quadruples, Operations.Add, value, None, listId)
        quadCounter += 1
    else:
        print("Error: Cannot add {} to list {}".format(value, listId))
        exit(1)

# Creates the remove quadruple
def p_SEM_REMOVE_FROM_LIST(p):
    '''SEM_REMOVE_FROM_LIST : empty'''
    global quadCounter
    listAddress = operandStack.pop()
    listType = typesStack.pop()
    newQuad(quadruples, Operations.Remove, None, None, listAddress)
    quadCounter += 1

# Creates the sort quadruple
def p_SEM_SORT_LIST(p):
    '''SEM_SORT_LIST : empty'''
    global quadCounter
    listAddress = operandStack.pop()
    listType = typesStack.pop()
    newQuad(quadruples, Operations.Sort, None, None, listAddress)
    quadCounter += 1

# Creates the find quadruple
def p_SEM_LIST_FIND(p):
    '''SEM_LIST_FIND : empty'''
    global quadCounter
    value = operandStack.pop()
    valueType = typesStack.pop()
    listAddress = operandStack.pop()
    listType = typesStack.pop()
    if Cube[Operations.Assign, listType, valueType] < 0:
        print("Error: Could not find {}".value)
        exit(1)
    else:
        newQuad(quadruples, Operations.Find, value, listAddress, tempVarCount[currentScope]['int'])
        operandStack.append(tempVarCount[currentScope]['int'])
        typesStack.append(Types.Int)
        tempVarCount[currentScope]['int'] += 1
        quadCounter += 1

# -----------------------------------------------------
# ------------------- MAIN PROGRAM --------------------
# -----------------------------------------------------

# Building the parser with a test
import ply.yacc as yacc



yacc.yacc()

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

with open(filename, 'r') as f:
    input = f.read()
    if (yacc.parse(input, tracking = True) == 'OK'):
        print(dirProc)

# printQuads(quadruples)

# Exectue virtual machine
execute(quadruples)