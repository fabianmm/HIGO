from Constants import *
from Cube import *
from Functions import *
from pprint import pprint
from fastnumbers import fast_real

currentPointer = 0
currentScope = 'global'
functionCount = 0
lastPointer = 0
scopeStack = []
pointerStack = []



# MEMORY
memory = {}
memory['global'] = {}
memory['global']['var'] = {}
memory['global']['temp'] = {}
memory['global']['var']['int'] = []
memory['global']['var']['decimal'] = []
memory['global']['var']['bool'] = []
memory['global']['temp']['int'] = []
memory['global']['temp']['decimal'] = []
memory['global']['temp']['bool'] = []
memory['local'] = {}



# PROGRAM

def activateGlobalMem(varQuad, tempQuad):
  varInt = varQuad['left']
  varDec = varQuad['right']
  varBool = varQuad['result']
  tempInt = tempQuad['left']
  tempDec = tempQuad['right']
  tempBool = tempQuad['result']
  
  for x in range(0, int(varInt)):
    memory['global']['var']['int'].append(0)
  
  for x in range(0, int(tempInt)):
    memory['global']['temp']['int'].append(0)

  for x in range(0, int(varDec)):
    memory['global']['var']['decimal'].append(0)

  for x in range(0, int(tempDec)):
    memory['global']['temp']['decimal'].append(0)

  for x in range(0, int(varBool)):
    memory['global']['var']['bool'].append(False)
  
  for x in range(0, int(tempBool)):
    memory['global']['temp']['bool'].append(False)
  
def activateLocalMem(varQuad, tempQuad):
  #print(varQuad, tempQuad)
  varInt = varQuad['left']
  varDec = varQuad['right']
  varBool = varQuad['result']
  tempInt = tempQuad['left']
  tempDec = tempQuad['right']
  tempBool = tempQuad['result']
  #print("Memory val:", varInt, varDec, varBool, tempInt, tempDec, tempBool)


  # Create memory 
  memory['local'][str(functionCount)] = {}
  memory['local'][str(functionCount)]['var'] = {}
  memory['local'][str(functionCount)]['temp'] = {}
  memory['local'][str(functionCount)]['var']['int'] = []
  memory['local'][str(functionCount)]['var']['decimal'] = []
  memory['local'][str(functionCount)]['var']['bool'] = []
  memory['local'][str(functionCount)]['temp']['int'] = []
  memory['local'][str(functionCount)]['temp']['decimal'] = []
  memory['local'][str(functionCount)]['temp']['bool'] = []

  # Initialize spaces
  for x in range(0, int(varInt)):
    memory['local'][str(functionCount)]['var']['int'].append(0)
  
  for x in range(0, int(tempInt)):
    memory['local'][str(functionCount)]['temp']['int'].append(0)

  for x in range(0, int(varDec)):
    memory['local'][str(functionCount)]['var']['decimal'].append(0)

  for x in range(0, int(tempDec)):
    memory['local'][str(functionCount)]['temp']['decimal'].append(0)

  for x in range(0, int(varBool)):
    memory['local'][str(functionCount)]['var']['bool'].append(False)
  
  for x in range(0, int(tempBool)):
    memory['local'][str(functionCount)]['temp']['bool'].append(False)




def extractValue(value):
  if isinstance(value, str):
    if value.startswith("#"):
      # Convert constant
      convertedValue = fast_real(value[1:])
      if convertedValue == "false":
        return False
      elif convertedValue == "true":
        return True
      return convertedValue
    elif value.startswith("&"):
      return value
  else:
    newValue = getValueFromMemory(value)
    return newValue

def getValueFromMemory(address):
  numAddress = int(address)
  realAddress = numAddress - AddressStart.Temp.Bool
  if realAddress >= 0:
    if currentScope == 'global':
      value = memory['global']['temp']['bool'][realAddress]
      return value
    else:
      value = memory['local'][currentScope]['temp']['bool'][realAddress]
      return value

  realAddress = numAddress - AddressStart.Temp.Decimal
  if realAddress >= 0:
    if currentScope == 'global':
      value = memory['global']['temp']['decimal'][realAddress]
      return value
    else:
      value = memory['local'][currentScope]['temp']['decimal'][realAddress]
      return value

  realAddress = numAddress - AddressStart.Temp.Int
  if realAddress >= 0:
    if currentScope == 'global':
      value = memory['global']['temp']['int'][realAddress]
      return value
    else:
      value = memory['local'][currentScope]['temp']['int'][realAddress]
      return value

  realAddress = numAddress - AddressStart.Local.Bool
  if realAddress >= 0:
    value = memory['local'][currentScope]['var']['bool'][realAddress]
    return value
  
  realAddress = numAddress - AddressStart.Local.Decimal
  if realAddress >= 0:
    value = memory['local'][currentScope]['var']['decimal'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Local.Int
  if realAddress >= 0:
    value = memory['local'][currentScope]['var']['int'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Global.Bool
  if realAddress >= 0:
    value = memory['global']['var']['bool'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Global.Decimal
  if realAddress >= 0:
    value = memory['global']['var']['decimal'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Global.Int
  if realAddress >= 0:
    value = memory['global']['var']['int'][realAddress]
    return value

  print("Address not found")
  exit(1)
  

def writeValueInMemory(address, value):
  numAddress = int(address)
  # print("Num address: ", numAddress)
  realAddress = numAddress - AddressStart.Temp.Bool
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    if currentScope == 'global':
      memory['global']['temp']['bool'][realAddress] = value
    else:
      memory['local'][currentScope]['temp']['bool'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Temp.Decimal
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    if currentScope == 'global':
      memory['global']['temp']['decimal'][realAddress] = value
    else:
      memory['local'][currentScope]['temp']['decimal'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Temp.Int
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    if currentScope == 'global':
      memory['global']['temp']['int'][realAddress] = value
    else:
      memory['local'][currentScope]['temp']['int'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Local.Bool
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['local'][currentScope]['var']['bool'][realAddress] = value
    return
  
  realAddress = numAddress - AddressStart.Local.Decimal
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['local'][currentScope]['var']['decimal'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Local.Int
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['local'][currentScope]['var']['int'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Global.Bool
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['global']['var']['bool'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Global.Decimal
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['global']['var']['decimal'][realAddress] = value
    return

  realAddress = numAddress - AddressStart.Global.Int
  # print("Real address: ", realAddress)
  if realAddress >= 0:
    memory['global']['var']['int'][realAddress] = value
    return

def writeArgInMemory(argType, argNum, value):
  numAddress = int(argNum)
  memory['local'][str(functionCount-1)]['var'][argType][numAddress] = value

def clearMemory(scope):
  memory['local'][scope].clear()

def execute(quadruples):
  global currentPointer, functionCount, currentScope, lastPointer
  # print(currentPointer)
  # print("Starting execution")
  while currentPointer < len(quadruples):
    #print("Memory State: ")
    #pprint(memory)
    # Get current quadruple
    current = quadruples[currentPointer]
    if current['operation'] == Operations.Plus:
      # Get both values and add
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      # print(left, "+", right)
      result = left + right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Minus:
      # Get both values and subtract
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      # print(left, "-", right)
      result = left - right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Times:
      # Get both values and multiply
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      # print(left, "*", right)
      result = left * right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Divide:
      # Get both values and divide
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      # print(left, "/", right)
      result = left / right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Assign:
      # Get value
      value = extractValue(current['left'])
      # Write in memory
      # print("Assigning: ", value, " to ", current['result'])
      writeValueInMemory(current['result'], value)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.GreaterThan:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left > right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.GreaterEqual:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left >= right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.LessThan:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left < right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.LessEqual:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left <= right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Equal:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left == right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.NotEqual:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left != right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.And:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left and right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Or:
      # Get values and get boolean value
      left = extractValue(current['left'])
      right = extractValue(current['right'])
      result = left or right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Not:
      # Get values and get boolean value
      value = extractValue(current['left'])
      result = not value
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Print:
      # Get value and print
      value = extractValue(current['result'])
      print(value)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Read:
      # Get input
      value = input("")
      # Assign to variable
      writeValueInMemory(current['result'], value)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Goto:
      # Get number of quad to jump to
      nextQuad = int(current['result'])
      # Move to that quad
      currentPointer = nextQuad
    elif current['operation'] == Operations.GotoF:
      # Evaluate expression
      value = extractValue(current['left'])
      if not value:
        # Move to specified quad
        nextQuad = int(current['result'])
        currentPointer = nextQuad
      else:
        currentPointer += 1
    elif current['operation'] == Operations.GlobalEra:
      # Get second (temporal) era
      secondEra = quadruples[currentPointer+1]
      # Activate Global and TempGlobal memory
      activateGlobalMem(current, secondEra)
      # Move two quads
      currentPointer += 2
    elif current['operation'] == Operations.Era:
      # Get second (temporal) era
      secondEra = quadruples[currentPointer+1]
      # Activate local mem
      activateLocalMem(current, secondEra)
      # Add to function counter
      functionCount += 1
      # Move pointer 2 quads
      currentPointer += 2
    elif current['operation'] == Operations.Param:
      argument = extractValue(current['left'])
      argumentType = current['right']
      writeArgInMemory(argumentType, current['result'], argument)
      currentPointer += 1
    elif current['operation'] == Operations.GoSub:
      pointerStack.append(currentPointer+1)
      scopeStack.append(currentScope)
      nextQuad = current['result']
      currentPointer = nextQuad
      currentScope = str(functionCount-1)
    elif current['operation'] == Operations.EndProc:
      currentPointer = pointerStack.pop()
      clearMemory(currentScope)
      currentScope = scopeStack.pop()
    elif current['operation'] == Operations.Return:
      value = extractValue(current['left'])
      # scope = currentScope
      # currentScope = 'global'
      writeValueInMemory(current['result'], value)
      # Do assign to temp
      # secondQuad = quadruples[currentPointer+1]
      # value = extractValue(secondQuad['left'])
      # writeValueInMemory(secondQuad['result'], value)
      # Return scope to normal
      # currentScope = scope
      currentPointer += 1
    elif current['operation'] == Operations.End:
      # End the program
      exit(1)
    else:
      pass
    
