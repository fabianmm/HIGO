class Types:
  Int = 0
  Decimal = 1
  Bool = 2
  String = 3
  Void = 4

class AddressStart:
  class Global:
    Int = 10000
    Decimal = 11000
    Bool = 12000
    ListInt = 15000
    ListDec = 16000
    ListBool = 17000
  class Local:
    Int = 20000
    Decimal = 21000
    Bool = 22000
    ListInt = 25000
    ListDec = 26000
    ListBool = 27000
  class Temp:
    Int = 30000
    Decimal = 31000
    Bool = 32000

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
  Parenthesis = 15
  Print = 20
  Read = 21
  Goto = 30
  GotoF = 31
  GoSub = 32
  EndProc = 43
  Era = 40
  Param = 41
  Return = 42
  GlobalEra = 50
  End = 51
  Advance = 60
  Add = 60
  Remove = 61
  Sort = 62
  Find = 63
