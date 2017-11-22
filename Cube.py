import numpy as numpy
from Constants import *

# Semantic Cube

Cube = numpy.zeros((13, 4, 4))

# CUBE
# x = operator, y = operand1, z = operand2

def InitializeCube():
    # PLUS
    Cube[Operations.Plus, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Plus, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Plus, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Plus, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Plus, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Plus, Types.String, Types.String] = Errors.TypeMismatch

    # MINUS
    Cube[Operations.Minus, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Minus, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Minus, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Minus, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Minus, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Minus, Types.String, Types.String] = Errors.TypeMismatch
    
    # TIMES
    Cube[Operations.Times, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Times, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Times, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Times, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Times, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Times, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Times, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Times, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Times, Types.String, Types.String] = Errors.TypeMismatch

    # DIVIDE
    Cube[Operations.Divide, Types.Int, Types.Int] = Types.Decimal
    Cube[Operations.Divide, Types.Int, Types.Decimal] = Types.Decimal
    Cube[Operations.Divide, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Divide, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Divide, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Divide, Types.String, Types.String] = Errors.TypeMismatch

    # GREATERTHAN
    Cube[Operations.GreaterThan, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.GreaterThan, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterThan, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.GreaterThan, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterThan, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterThan, Types.String, Types.String] = Errors.TypeMismatch

    # GREATEREQUAL
    Cube[Operations.GreaterEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.GreaterEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.GreaterEqual, Types.String, Types.String] = Errors.TypeMismatch

    # LESSTHAN
    Cube[Operations.LessThan, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.LessThan, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.LessThan, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.LessThan, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.LessThan, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessThan, Types.String, Types.String] = Errors.TypeMismatch

    # LESSEQUAL
    Cube[Operations.LessEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.LessEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.LessEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.LessEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.LessEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.LessEqual, Types.String, Types.String] = Errors.TypeMismatch

    # EQUAL
    Cube[Operations.Equal, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.Equal, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.Equal, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.Equal, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.Equal, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.Bool, Types.Bool] = Types.Bool
    Cube[Operations.Equal, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Equal, Types.String, Types.String] = Errors.TypeMismatch

    # NOTEQUAL
    Cube[Operations.NotEqual, Types.Int, Types.Int] = Types.Bool
    Cube[Operations.NotEqual, Types.Int, Types.Decimal] = Types.Bool
    Cube[Operations.NotEqual, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Decimal, Types.Int] = Types.Bool
    Cube[Operations.NotEqual, Types.Decimal, Types.Decimal] = Types.Bool
    Cube[Operations.NotEqual, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.Bool, Types.Bool] = Types.Bool
    Cube[Operations.NotEqual, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.NotEqual, Types.String, Types.String] = Errors.TypeMismatch

    # AND
    Cube[Operations.And, Types.Int, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.And, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.And, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.Bool, Types.Bool] = Types.Bool
    Cube[Operations.And, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.And, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.And, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.And, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.And, Types.String, Types.String] = Errors.TypeMismatch

    # OR
    Cube[Operations.Or, Types.Int, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.Bool, Types.Bool] = Types.Bool
    Cube[Operations.Or, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Or, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Or, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Or, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Or, Types.String, Types.String] = Errors.TypeMismatch

    # ASSIGN
    Cube[Operations.Assign, Types.Int, Types.Int] = Types.Int
    Cube[Operations.Assign, Types.Int, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Int, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Int, Types.String] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Decimal, Types.Int] = Types.Decimal
    Cube[Operations.Assign, Types.Decimal, Types.Decimal] = Types.Decimal
    Cube[Operations.Assign, Types.Decimal, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Decimal, Types.String] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.Bool, Types.Bool] = Types.Bool
    Cube[Operations.Assign, Types.Bool, Types.String] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.String, Types.Int] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.String, Types.Decimal] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.String, Types.Bool] = Errors.TypeMismatch
    Cube[Operations.Assign, Types.String, Types.String] = Errors.TypeMismatch

InitializeCube()