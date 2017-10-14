import numpy as numpy
from Constants import *

# Semantic Cube

Cube = numpy.zeros((13, 3, 3))

# CUBE
# x = operator, y = operand1, z = operand2

def InitializeCube():
    # PLUS
    Cube[Operations.Plus, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Plus, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Plus, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Plus, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Plus, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # MINUS
    Cube[Operations.Minus, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Minus, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Minus, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Minus, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Minus, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Bool] = Errors.TypeMismatch
    
    # TIMES
    Cube[Operations.Times, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Times, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Times, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Times, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Times, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # DIVIDE
    Cube[Operations.Divide, Types.Int, Types.Int] = Types.Decimal
    Cube[Operations.Divide, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Divide, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Divide, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Divide, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # GREATERTHAN
    Cube[Operations.GreaterThan, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.GreaterThan, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterThan, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.GreaterThan, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterThan, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # GREATEREQUAL
    Cube[Operations.GreaterEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # LESSTHAN
    Cube[Operations.LessThan, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.LessThan, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.LessThan, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.LessThan, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.LessThan, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # LESSEQUAL
    Cube[Operations.LessEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.LessEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.LessEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.LessEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.LessEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Bool] = Errors.TypeMismatch

    # EQUAL
    Cube[Operations.Equal, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.Equal, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.Equal, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.Equal, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.Equal, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Bool] = Types.Bool

    # NOTEQUAL
    Cube[Operations.NotEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.NotEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.NotEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.NotEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.NotEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Bool] = Types.Bool

    # AND
    Cube[Operations.And, Types.Int, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Bool] = Types.Bool

    # OR
    Cube[Operations.Or, Types.Int, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Bool] = Types.Bool

    # ASSIGN
    Cube[Operations.Assign, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Assign, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Assign, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Assign, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Bool] = Types.Bool

InitializeCube()