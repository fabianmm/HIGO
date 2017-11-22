from Constants import *
from pprint import *
from Cube import *

def buildQuad(operator, term1, term2, result):
  quad = {'operation' : operator, 'term1' : term1, 'term2' : term2, 'result' : result}
  #print(quad)
  return quad

def newQuad(quadruples, operation, left, right, result):
  quad = {'operation' : operation, 'left' : left, 'right' : right, 'result' : result}
  quadruples.append(quad)

def getOperationCode(operation):
  if operation == '+':
    return Operations.Plus
  if operation == '-':
    return Operations.Minus
  if operation == '*':
    return Operations.Times
  if operation == '/':
    return Operations.Divide
  if operation == '=':
    return Operations.Assign
  if operation == '>':
    return Operations.GreaterThan
  if operation == '<':
    return Operations.LessThan
  if operation == '>=':
    return Operations.GreaterEqual
  if operation == '<=':
    return Operations.LessEqual
  if operation == '==':
    return Operations.Equal
  if operation == '!=':
    return Operations.NotEqual
  if operation == 'and':
    return Operations.And
  if operation == 'or':
    return Operations.Or
  if operation == 'not':
    return Operations.Not
  if operation == 'print':
    return Operations.Print
  if operation == 'readto':
    return Operations.Read

def printStacks(operations, operands, types):
  print("Operations: ", operations) 
  print("Operands: ", operands)
  print("Types: ", types )

def printQuads(quads):
  i = 0
  print("QUADRUPLES")
  for item in quads:
    print(str(i) + ": ", str(item['operation']), str(item['left']), str(item['right']), str(item['result']))
    i = i + 1

def getTypeFromCode(typeCode):
  if typeCode == Types.Int:
    return "int"
  if typeCode == Types.Decimal:
    return "decimal"
  if typeCode == Types.Bool:
    return "bool"
  if typeCode == Types.String:
    return "string"

def getListTypeFromCode(typeCode):
  if typeCode == Types.Int:
    return "listint"
  if typeCode == Types.Decimal:
    return "listdec"
  if typeCode == Types.Bool:
    return "listbool"

def generateQuad(operationStack, operandStack, typesStack, temporalCounter, quadCounter):
  operation = operationStack.pop()
  term2 = operandStack.pop()
  type2 = typesStack.pop()
  term1 = operandStack.pop()
  type1 = typesStack.pop()
  resultType = Cube[operation, type1, type2]
  if resultType != Errors.TypeMismatch:
      temp = "t" + str(temporalCounter)
      quad = buildQuad(operation, term1, term2, temp)
      operandStack.append(temp)
      typesStack.append(resultType)
      return quad
  else:
      print("Error: Type mismatch {} and {}, with {} and {}".format(getTypeFromCode(type1), getTypeFromCode(type2), term1, term2))
      exit(1)

def generateOneArgQuadruple(operation, result):
  quad = {'operation' : operation, 'term1' : Operations.Null, 'term2' : Operations.Null, 'result' : result}
  return quad

def fill(quadNumber, location, quadruples):
  quadruples[quadNumber]['result'] = location

def typeToString(typeCode):
  if typeCode == 0:
    return 'int'
  if typeCode == 1:
    return 'decimal'
  if typeCode == 2:
    return 'bool'
  if typeCode == 3:
    return 'string'
  if typeCode == 4:
    return 'void'