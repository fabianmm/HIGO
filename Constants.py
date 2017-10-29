class Types:
  Int = 0
  Decimal = 1
  Bool = 2
  String = 4
  Void = 5

class Errors:
  TypeMismatch = -1

class Operations:
  Null = -1
  Plus = 0
  Minus = 1
  Times = 2
  Divide = 3
  GreaterThan = 4
  GreaterEqual = 5
  LessThan = 6
  LessEqual = 7
  Equal = 8
  NotEqual = 9
  And = 10
  Or = 11
  Assign = 12
  Not = 13
  Parenthesis = 14
  Print = 15
  Goto = 20
  GotoF = 21
  GotoT = 22
  GoSub = 23
