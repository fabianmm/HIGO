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
  
def activateLocalMem(varQuad, tempQuad, listQuad):
  #print(varQuad, tempQuad)
  varInt = varQuad['left']
  varDec = varQuad['right']
  varBool = varQuad['result']
  tempInt = tempQuad['left']
  tempDec = tempQuad['right']
  tempBool = tempQuad['result']
  listInt = listQuad['left']
  listDec = listQuad['right']
  listBool = listQuad['result']

  # Create memory 
  memory['local'][str(functionCount)] = {}
  memory['local'][str(functionCount)]['var'] = {}
  memory['local'][str(functionCount)]['temp'] = {}
  memory['local'][str(functionCount)]['list'] = {}
  memory['local'][str(functionCount)]['node'] = {}
  memory['local'][str(functionCount)]['var']['int'] = []
  memory['local'][str(functionCount)]['var']['decimal'] = []
  memory['local'][str(functionCount)]['var']['bool'] = []
  memory['local'][str(functionCount)]['temp']['int'] = []
  memory['local'][str(functionCount)]['temp']['decimal'] = []
  memory['local'][str(functionCount)]['temp']['bool'] = []
  memory['local'][str(functionCount)]['list']['int'] = []
  memory['local'][str(functionCount)]['list']['decimal'] = []
  memory['local'][str(functionCount)]['list']['bool'] = []
  memory['local'][str(functionCount)]['node']['int'] = []
  memory['local'][str(functionCount)]['node']['decimal'] = []
  memory['local'][str(functionCount)]['node']['bool'] = []

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
  
  for x in range(0, int(listInt)):
    memory['local'][str(functionCount)]['list']['int'].append({'head' : None, 'tail' : None})
  for x in range(0, int(listDec)):
    memory['local'][str(functionCount)]['list']['decimal'].append({'head' : None, 'tail' : None})
  for x in range(0, int(listBool)):
    memory['local'][str(functionCount)]['list']['bool'].append({'head' : None, 'tail' : None})

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
      # Get list Item
      listItem = retrieve(scope, currentScope, kind, datatype, realListAddress)
      # Gets the index
      indexValue = extractValueFromAddress(index)
      # Retrieve from nodes
      node = retrieveFromList(listItem['head'], indexValue, datatype)
      return node['value']
    else:
      # In case the address got stringified
      address = int(address)
      scope, kind, datatype, realAddress = deconstructAddress(address)
      value = retrieve(scope, currentScope, kind, datatype, realAddress)
      return value
  else:
    # Normal address
    scope, kind, datatype, realAddress = deconstructAddress(address)
    value = retrieve(scope, currentScope, kind, datatype, realAddress)
    return value

def printValue(address):
  if isinstance(address, str):
    if address.startswith("#"):
      # Convert constant
      convertedValue = fast_real(address[1:])
      if convertedValue == "false":
        print(False)
        return
      elif convertedValue == "true":
        print(True)
        return
      print(convertedValue)
      return
    elif address.startswith("&"):
      # Get value from pointer
      address = address[1:]
      listAddress, index = address.split(',')
      scope, kind, datatype, realListAddress = deconstructAddress(listAddress)
      listItem = retrieve(scope, currentScope, kind, datatype, realListAddress)
      indexValue = extractValueFromAddress(index)
      node = retrieveFromList(listItem['head'], indexValue, datatype)
      print(node['value'])
      return
    else:
      address = int(address)
      scope, kind, datatype, realAddress = deconstructAddress(address)
      if kind == 'list':
        printList(datatype, realAddress)
        return
      else:
        value = retrieve(scope, currentScope, kind, datatype, realAddress)
        print(value)
        return
  else:
    scope, kind, datatype, realAddress = deconstructAddress(address)
    if kind == 'list':
        printList(datatype, realAddress)
        return
    else:
        value = retrieve(scope, currentScope, kind, datatype, realAddress)
        print(value)
        return

def retrieveFromList(head, index, datatype):
  if head != None:
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
    else:
      current = memory['local'][currentScope]['node'][datatype][head]
      i = index
      while i > 0:
        nextNode = current['next']
        if not nextNode:
          print("Index {} out of bounds".format(index))
          exit(1)
        else:
          current = memory['local'][currentScope]['node'][datatype][nextNode]
          i -= 1
      return current
  else:
    print("Out of bounds.")
    exit(1)

# def getValueFromMemory(address):
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

  realAddress = numAddress - AddressStart.Local.ListBool
  if realAddress >= 0:
    return currentScope, 'list', 'bool', realAddress
  
  realAddress = numAddress - AddressStart.Local.ListDec
  if realAddress >= 0:
    return currentScope, 'list', 'decimal', realAddress

  realAddress = numAddress - AddressStart.Local.ListInt
  if realAddress >= 0:
    return currentScope, 'list', 'int', realAddress

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
    listItem = retrieve(scope, currentScope, kind, datatype, realListAddress)
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
  else:
    listItem = memory['local'][currentScope]['list'][datatype][listAddress]
    if listItem['head'] == None:
      # list is empty, update head
      newNode = {'value' : value, 'next' : None, 'prev' : None}
      memory['local'][currentScope]['node'][datatype].append(newNode)
      memory['local'][currentScope]['list'][datatype][listAddress]['head'] = len(memory['local'][currentScope]['node'][datatype]) - 1
    else:
      last = memory['local'][currentScope]['list'][datatype][listAddress]['tail']
      newNode = {'value' : value, 'next' : None, 'prev' : last}
      memory['local'][currentScope]['node'][datatype].append(newNode)
      # Update previous node and tail
      memory['local'][currentScope]['node'][datatype][last]['next'] = len(memory['local'][currentScope]['node'][datatype]) - 1
    memory['local'][currentScope]['list'][datatype][listAddress]['tail'] = len(memory['local'][currentScope]['node'][datatype]) - 1

def sortList(address):
  scope, kind, datatype, listAddress = deconstructAddress(address)
  items = []
  if scope == 'global':
    listItem = memory['global']['list'][datatype][listAddress]
    if listItem['head'] != None:
      node = memory['global']['node'][datatype][listItem['head']]
      items.append(node['value'])
      nextNodeIndex = node['next']
      while nextNodeIndex != None:
        node = memory['global']['node'][datatype][nextNodeIndex]
        items.append(node['value'])
        nextNodeIndex = node['next']
      items.sort()
      # Replace values again
      node = memory['global']['node'][datatype][listItem['head']]
      node['value'] = items[0]
      nextNodeIndex = node['next']
      i = 1
      while nextNodeIndex != None:
        node = memory['global']['node'][datatype][nextNodeIndex]
        node['value'] = items[i]
        nextNodeIndex = node['next']
        i += 1
  else:
    listItem = memory['local'][scope]['list'][datatype][listAddress]
    if listItem['head'] != None:
      node = memory['local'][scope]['node'][datatype][listItem['head']]
      items.append(node['value'])
      nextNodeIndex = node['next']
      while nextNodeIndex != None:
        node = memory['local'][scope]['node'][datatype][nextNodeIndex]
        items.append(node['value'])
        nextNodeIndex = node['next']
      items.sort()
      # Replace values again
      node = memory['local'][scope]['node'][datatype][listItem['head']]
      node['value'] = items[0]
      nextNodeIndex = node['next']
      i = 1
      while nextNodeIndex != None:
        node = memory['local'][scope]['node'][datatype][nextNodeIndex]
        node['value'] = items[i]
        nextNodeIndex = node['next']
        i += 1

def findValueInList(value, address):
  scope, kind, datatype, listAddress = deconstructAddress(address)
  if scope == 'global':
    listItem = memory['global']['list'][datatype][listAddress]
    if listItem['head'] != None:
      i = 0
      node = memory['global']['node'][datatype][listItem['head']]
      if node['value'] == value:
        return i
      nextNodeIndex = node['next']
      i = 1
      while nextNodeIndex != None:
        node = memory['global']['node'][datatype][nextNodeIndex]
        if node['value'] == value:
          return i
        nextNodeIndex = node['next']
        i += 1
      return -1
  else:
    listItem = memory['local'][currentScope]['list'][datatype][listAddress]
    if listItem['head'] != None:
      i = 0
      node = memory['local'][currentScope]['node'][datatype][listItem['head']]
      if node['value'] == value:
        return i
      nextNodeIndex = node['next']
      i = 1
      while nextNodeIndex != None:
        node = memory['local'][currentScope]['node'][datatype][nextNodeIndex]
        if node['value'] == value:
          return i
        nextNodeIndex = node['next']
        i += 1
      return -1

def removeFromList(address):
  address = address[1:]
  listAddress, index = address.split(',')
  scope, kind, datatype, realListAddress = deconstructAddress(listAddress)
  listItem = retrieve(scope, currentScope, kind, datatype, realListAddress)
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
  else:
    if prevNode:
      memory['local'][currentScope]['node'][datatype][prevNode]['next'] = nextNode
    if nextNode:
      memory['local'][currentScope]['node'][datatype][nextNode]['prev'] = prevNode

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
    else:
      if datatype == 'int':
        return AddressStart.Local.ListInt
      if datatype == 'decimal':
        return AddressStart.Local.ListDec
      if datatype == 'bool':
        return AddressStart.Local.ListBool
  
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
  else:
    head = memory['local'][currentScope]['list'][datatype][address]['head']
    if head != None:
      node = memory['local'][currentScope]['node'][datatype][head]
      while True:
        items.append(node['value'])
        if not node['next']:
          break
        node = memory['local'][currentScope]['node'][datatype][node['next']]
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
      if right == 0:
        print("Cannot divide by 0")
        exit(1)
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
      address = current['result']
      printValue(address)
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
      thirdEra = quadruples[currentPointer+2]
      # Activate local mem
      activateLocalMem(current, secondEra, thirdEra)
      # Add to function counter
      functionCount += 1
      # Move pointer 2 quads
      currentPointer += 3
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
    elif current['operation'] == Operations.Add:
      value = extractValueFromAddress(current['left'])
      addToList(current['result'], value)
      currentPointer += 1
    elif current['operation'] == Operations.Remove:
      value = current['result']
      removeFromList(value)
      currentPointer += 1
    elif current['operation'] == Operations.Sort:
      address = current['result']
      sortList(address)
      currentPointer+=1
    elif current['operation'] == Operations.Find:
      value = extractValueFromAddress(current['left'])
      listAddress = current['right']
      foundIndex = findValueInList(value, listAddress)
      writeValueInMemory(current['result'], foundIndex)
      currentPointer += 1
    elif current['operation'] == Operations.End:
      # End the program
      memory.clear()
      exit(1)
    else:
      pass
    
