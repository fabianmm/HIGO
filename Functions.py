from Constants import *
from pprint import *
from Cube import *

def buildQuad(operator, term1, term2, result):
  quad = {'operator' : operator, 'term1' : term1, 'term2' : term2, 'result' : result}
  # print(quad)
  return quad

def getOperationCode(operand):
  if operand == '+':
    return Operations.Plus
  if operand == '-':
    return Operations.Minus
  if operand == '*':
    return Operations.Times
  if operand == '/':
    return Operations.Divide
  if operand == '=':
    return Operations.Assign

def printStacks(operations, operands, types):
  print("Operations: ", operations) 
  print("Operands: ", operands)
  print("Types: ", types )

def printQuads(quads):
  i = 0
  print("QUADRUPLES")
  for item in quads:
    print(str(i) + ": ", str(item['operator']), str(item['term1']), str(item['term2']), str(item['result']))
    i = i + 1

def getTypeFromCode(typeCode):
  if typeCode == Types.Int:
    return "int"
  if typeCode == Types.Decimal:
    return "decimal"
  if typeCode == Types.Bool:
    return "bool"

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
      print("Error: Type mismatch {} and {}".format(getTypeFromCode(type1), getTypeFromCode(type2)))
      exit(1)