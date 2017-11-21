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
memory['global']['list'] = {}
memory['global']['node'] = {}
memory['global']['var']['int'] = []
memory['global']['var']['decimal'] = []
memory['global']['var']['bool'] = []
memory['global']['temp']['int'] = []
memory['global']['temp']['decimal'] = []
memory['global']['temp']['bool'] = []
memory['global']['list']['int'] = []
memory['global']['list']['decimal'] = []
memory['global']['list']['bool'] = []
memory['global']['node']['int'] = []
memory['global']['node']['decimal'] = []
memory['global']['node']['bool'] = []
memory['local'] = {}



# PROGRAM

def activateGlobalMem(varQuad, tempQuad, listQuad):
  varInt = varQuad['left']
  varDec = varQuad['right']
  varBool = varQuad['result']
  tempInt = tempQuad['left']
  tempDec = tempQuad['right']
  tempBool = tempQuad['result']
  listInt = listQuad['left']
  listDec = listQuad['right']
  listBool = listQuad['result']
  
  for x in range(0, int(varInt)):
    memory['global']['var']['int'].append(0)
  
  for x in range(0, int(tempInt)):
    memory['global']['temp']['int'].append(0)
  
  for x in range(0, int(listInt)):
    memory['global']['list']['int'].append({'head' : None, 'tail' : None})

  for x in range(0, int(varDec)):
    memory['global']['var']['decimal'].append(0)

  for x in range(0, int(tempDec)):
    memory['global']['temp']['decimal'].append(0)
  
  for x in range(0, int(listDec)):
    memory['global']['list']['decimal'].append({'value' : 0, 'next' : None, 'prev' : None})

  for x in range(0, int(varBool)):
    memory['global']['var']['bool'].append(False)
  
  for x in range(0, int(tempBool)):
    memory['global']['temp']['bool'].append(False)
  
  for x in range(0, int(listBool)):
    memory['global']['list']['bool'].append({'value' : False, 'next' : None, 'prev' : None})
  
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

# Gets the value inside an address
def extractValueFromAddress(address):
  if isinstance(address, str):
    if address.startswith("#"):
      # Convert constant
      convertedValue = fast_real(address[1:])
      if convertedValue == "false":
        return False
      elif convertedValue == "true":
        return True
      return convertedValue
    elif address.startswith("&"):
      # Get value from pointer
      address = address[1:]
      listAddress, index = address.split(',')
      scope, kind, datatype, realListAddress = deconstructAddress(listAddress)
      listItem = retrieve(currentScope, currentScope, kind, datatype, realListAddress)
      indexValue = extractValueFromAddress(index)
      node = retrieveFromList(listItem['head'], indexValue, datatype)
      return node['value']
    else:
      address = int(address)
      scope, kind, datatype, realAddress = deconstructAddress(address)
      value = retrieve(scope, currentScope, kind, datatype, realAddress)
      return value
  else:
    scope, kind, datatype, realAddress = deconstructAddress(address)
    value = retrieve(scope, currentScope, kind, datatype, realAddress)
    return value

def retrieveFromList(head, index, datatype):
  if currentScope == 'global':
    current = memory['global']['node'][datatype][head]
    i = index
    while i > 0:
      nextNode = current['next']
      if not nextNode:
        print("Index {} out of bounds".format(index))
        exit(1)
      else:
        current = memory['global']['node'][datatype][nextNode]
        i -= 1
    return current

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

  # Global Lists
  realAddress = numAddress - AddressStart.Global.ListBool
  if realAddress >= 0:
    value = memory['global']['list']['bool'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Global.ListDec
  if realAddress >= 0:
    value = memory['global']['list']['decimal'][realAddress]
    return value

  realAddress = numAddress - AddressStart.Global.ListInt
  if realAddress >= 0:
    value = memory['global']['list']['int'][realAddress]
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
  
def deconstructAddress(addressStr):
  numAddress = int(addressStr)
  realAddress = numAddress - AddressStart.Temp.Bool
  if realAddress >= 0:
    return currentScope, 'temp', 'bool', realAddress

  realAddress = numAddress - AddressStart.Temp.Decimal
  if realAddress >= 0:
    return currentScope, 'temp', 'decimal', realAddress

  realAddress = numAddress - AddressStart.Temp.Int
  if realAddress >= 0:
    return currentScope, 'temp', 'int', realAddress

  realAddress = numAddress - AddressStart.Local.Bool
  if realAddress >= 0:
    return currentScope, 'var', 'bool', realAddress
  
  realAddress = numAddress - AddressStart.Local.Decimal
  if realAddress >= 0:
    return currentScope, 'var', 'decimal', realAddress

  realAddress = numAddress - AddressStart.Local.Int
  if realAddress >= 0:
    return currentScope, 'var', 'int', realAddress

  realAddress = numAddress - AddressStart.Global.ListBool
  if realAddress >= 0:
    return 'global', 'list', 'bool', realAddress

  realAddress = numAddress - AddressStart.Global.ListDec
  if realAddress >= 0:
    return 'global', 'list', 'decimal', realAddress

  realAddress = numAddress - AddressStart.Global.ListInt
  if realAddress >= 0:
    return 'global', 'list', 'int', realAddress

  realAddress = numAddress - AddressStart.Global.Bool
  if realAddress >= 0:
    return 'global', 'var', 'bool', realAddress

  realAddress = numAddress - AddressStart.Global.Decimal
  if realAddress >= 0:
    return 'global', 'var', 'decimal', realAddress

  realAddress = numAddress - AddressStart.Global.Int
  if realAddress >= 0:
    return 'global', 'var', 'int', realAddress

def writeValueInMemory(address, value):
  if isinstance(address, str) and address.startswith("&"):
    # Address will be a list
    address = address[1:]
    listAddress, index = address.split(',')
    scope, kind, datatype, realListAddress = deconstructAddress(listAddress)
    listItem = retrieve(currentScope, currentScope, kind, datatype, realListAddress)
    indexValue = extractValueFromAddress(index)
    node = retrieveFromList(listItem['head'], indexValue, datatype)
    node['value'] = value
    return

  numAddress = int(address)
  scope, kind, datatype, realAddress = deconstructAddress(address)

  if scope == 'global':
    memory['global'][kind][datatype][realAddress] = value
  else:
    memory['local'][currentScope][kind][datatype][realAddress] = value

  # realAddress = numAddress - AddressStart.Temp.Bool
  # if realAddress >= 0:
  #   if currentScope == 'global':
  #     memory['global']['temp']['bool'][realAddress] = value
  #   else:
  #     memory['local'][currentScope]['temp']['bool'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Temp.Decimal
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   if currentScope == 'global':
  #     memory['global']['temp']['decimal'][realAddress] = value
  #   else:
  #     memory['local'][currentScope]['temp']['decimal'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Temp.Int
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   if currentScope == 'global':
  #     memory['global']['temp']['int'][realAddress] = value
  #   else:
  #     memory['local'][currentScope]['temp']['int'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Local.Bool
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['local'][currentScope]['var']['bool'][realAddress] = value
  #   return
  
  # realAddress = numAddress - AddressStart.Local.Decimal
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['local'][currentScope]['var']['decimal'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Local.Int
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['local'][currentScope]['var']['int'][realAddress] = value
  #   return
  
  # realAddress = numAddress - AddressStart.Global.ListBool
  # if realAddress >= 0:
  #   memory['global']['list']['bool'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Global.ListDec
  # if realAddress >= 0:
  #   memory['global']['list']['decimal'][realAddress] = value
  #   return 

  # realAddress = numAddress - AddressStart.Global.ListInt
  # if realAddress >= 0:
  #   memory['global']['list']['int'][realAddress] = value
  #   return 

  # realAddress = numAddress - AddressStart.Global.Bool
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['global']['var']['bool'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Global.Decimal
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['global']['var']['decimal'][realAddress] = value
  #   return

  # realAddress = numAddress - AddressStart.Global.Int
  # # print("Real address: ", realAddress)
  # if realAddress >= 0:
  #   memory['global']['var']['int'][realAddress] = value
  #   return

def writeArgInMemory(argType, argNum, value):
  numAddress = int(argNum)
  memory['local'][str(functionCount-1)]['var'][argType][numAddress] = value

def clearMemory(scope):
  memory['local'][scope].clear()

def addToList(address, value):
  scope, kind, datatype, listAddress = deconstructAddress(address)
  if currentScope == 'global':
    listItem = memory['global']['list'][datatype][listAddress]
    if listItem['head'] == None:
      # list is empty, update head
      newNode = {'value' : value, 'next' : None, 'prev' : None}
      memory['global']['node'][datatype].append(newNode)
      memory['global']['list'][datatype][listAddress]['head'] = len(memory['global']['node'][datatype]) - 1
    else:
      last = memory['global']['list'][datatype][listAddress]['tail']
      newNode = {'value' : value, 'next' : None, 'prev' : last}
      memory['global']['node'][datatype].append(newNode)
      # Update previous node and tail
      memory['global']['node'][datatype][last]['next'] = len(memory['global']['node'][datatype]) - 1
    memory['global']['list'][datatype][listAddress]['tail'] = len(memory['global']['node'][datatype]) - 1

    # # Advance to last element
    # while listItem and listItem['next']:
    #   realAddress = listItem['next']
    #   listItem = memory['global'][kind][datatype][realAddress]

    # # Add element and update last's next
    # memory['global'][kind][datatype].append({'value' : value, 'next' : None, 'prev' : realAddress})
    # memory['global'][kind][datatype][realAddress]['next'] = len(memory['global'][kind][datatype]) - 1

def removeFromList(address):
  address = address[1:]
  listAddress, index = address.split(',')
  scope, kind, datatype, realListAddress = deconstructAddress(listAddress)
  listItem = retrieve(currentScope, currentScope, kind, datatype, realListAddress)
  indexValue = extractValueFromAddress(index)
  node = retrieveFromList(listItem['head'], indexValue, datatype)
  prevNode = node['prev']
  nextNode = node['next']
  del node
  # Update prev and next, tail and head if necessary
  if prevNode == None:
    # Update head
    listItem['head'] = nextNode
  if nextNode == None:
    # Update tail
    listItem['tail'] = prevNode
  if currentScope == 'global':
    if prevNode:
      memory['global']['node'][datatype][prevNode]['next'] = nextNode
    if nextNode:
      memory['global']['node'][datatype][nextNode]['prev'] = prevNode

def retrieve(scope, functionName, kind, datatype, index):
  if scope == 'global':
    return memory[scope][kind][datatype][index]
  else:
    return memory['local'][str(functionName)][kind][datatype][index]

def getBaseAddress(scope, kind, datatype):
  if kind == 'temp':
    if datatype == 'int':
      return AddressStart.Temp.Int
    if datatype == 'decimal':
      return AddressStart.Temp.Decimal
    if datatype == 'bool':
      return AddressStart.Temp.Bool
  if kind == 'var':
    if scope == 'global':
      if datatype == 'int':
        return AddressStart.Global.Int
      if datatype == 'decimal':
        return AddressStart.Global.Decimal
      if datatype == 'bool':
        return AddressStart.Global.Bool
    else:
      if datatype == 'int':
        return AddressStart.Local.Int
      if datatype == 'decimal':
        return AddressStart.Local.Decimal
      if datatype == 'bool':
        return AddressStart.Local.Bool
  if kind == 'list':
    if scope == 'global':
      if datatype == 'int':
        return AddressStart.Global.ListInt
      if datatype == 'decimal':
        return AddressStart.Global.ListDec
      if datatype == 'bool':
        return AddressStart.Global.ListBool
  
def printList(datatype, address):
  items = []
  if currentScope == 'global':
    head = memory['global']['list'][datatype][address]['head']
    if head != None:
      node = memory['global']['node'][datatype][head]
      while True:
        items.append(node['value'])
        if not node['next']:
          break
        node = memory['global']['node'][datatype][node['next']]
  print(items)
      
    

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
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      # print(left, "+", right)
      result = left + right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Minus:
      # Get both values and subtract
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      # print(left, "-", right)
      result = left - right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Times:
      # Get both values and multiply
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      # print(left, "*", right)
      result = left * right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Divide:
      # Get both values and divide
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      # print(left, "/", right)
      result = left / right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Assign:
      # Get value
      value = extractValueFromAddress(current['left'])
      # Write in memory
      # print("Assigning: ", value, " to ", current['result'])
      writeValueInMemory(current['result'], value)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.GreaterThan:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left > right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.GreaterEqual:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left >= right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.LessThan:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left < right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.LessEqual:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left <= right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Equal:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left == right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.NotEqual:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left != right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.And:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left and right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Or:
      # Get values and get boolean value
      left = extractValueFromAddress(current['left'])
      right = extractValueFromAddress(current['right'])
      result = left or right
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Not:
      # Get values and get boolean value
      value = extractValueFromAddress(current['left'])
      result = not value
      # Write result in memory
      writeValueInMemory(current['result'], result)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Print:
      # Get value and print
      scope, kind, datatype, realAddress = deconstructAddress(current['result'])
      if kind == 'list':
        printList(datatype, realAddress)
      else:
        value = extractValueFromAddress(current['result'])
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
      value = extractValueFromAddress(current['left'])
      if not value:
        # Move to specified quad
        nextQuad = int(current['result'])
        currentPointer = nextQuad
      else:
        currentPointer += 1
    elif current['operation'] == Operations.GlobalEra:
      # Get second (temporal) era
      secondEra = quadruples[currentPointer+1]
      thirdEra = quadruples[currentPointer+2]
      # Activate Global and TempGlobal memory
      activateGlobalMem(current, secondEra, thirdEra)
      # Move two quads
      currentPointer += 3
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
      # Get argument
      argument = extractValueFromAddress(current['left'])
      argumentType = current['right']
      # Write argument in memory
      writeArgInMemory(argumentType, current['result'], argument)
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.GoSub:
      # Save current quad pointer and scope
      pointerStack.append(currentPointer+1)
      scopeStack.append(currentScope)
      nextQuad = current['result']
      # Change pointer and scope
      currentPointer = nextQuad
      currentScope = str(functionCount-1)
    elif current['operation'] == Operations.EndProc:
      # Return pointer and scope to previous
      currentPointer = pointerStack.pop()
      clearMemory(currentScope)
      currentScope = scopeStack.pop()
    elif current['operation'] == Operations.Return:
      # Get value and write it
      value = extractValueFromAddress(current['left'])
      saveScope = currentScope
      currentScope = 'global'
      writeValueInMemory(current['result'], value)
      currentScope = saveScope
      # Move to next quad
      currentPointer += 1
    elif current['operation'] == Operations.Advance:
      listItem = extractValueFromAddress(current['left'])
      num = extractValueFromAddress(current['right'])
      scope, kind, datatype, realAddress = deconstructAddress(current['left'])
      base = getBaseAddress(currentScope, kind, datatype)
      finalAddress = base
      # Move spaces
      while num > 0:
        finalAddress = base + listItem['next']
        listItem = extractValueFromAddress(finalAddress)
        num -= 1
      # Write address in memory
      writeValueInMemory(current['result'], finalAddress)
      currentPointer += 1
    elif current['operation'] == Operations.Add:
      value = extractValueFromAddress(current['left'])
      addToList(current['result'], value)
      currentPointer += 1
    elif current['operation'] == Operations.Remove:
      value = current['result']
      # address = value[1:]
      # kind, datatype, realAddress = deconstructAddress(address)
      # address = retrieve(currentScope, currentScope, kind, datatype, realAddress)
      removeFromList(value)
      currentPointer += 1
    elif current['operation'] == Operations.End:
      # End the program
      memory.clear()
      exit(1)
    else:
      pass
    
