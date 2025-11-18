#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#
import enum

class Operation(enum.Enum):
    SUM = 1
    DIFFERENCE = 2
    MULTIPLICATION = 3
    DIVISION = 4

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
def operation(a, b, op: Operation):
    if op == Operation.SUM:
        return sum(a, b)
    elif op == Operation.DIFFERENCE:
        return difference(a, b)
    elif op == Operation.MULTIPLICATION:
        return multiplication(a, b)
    elif op == Operation.DIVISION:
        return division(a, b)
    else:
        raise ValueError("Invalid operation")
    
if __name__ == "__main__":
    num1 = float(input("Insert first number: "))
    num2 = float(input("Insert second number: "))
    
    print(f"SUM: {operation(num1, num2, Operation.SUM)}")
    print(f"Difference: {operation(num1, num2, Operation.DIFFERENCE)}")
    print(f"Multiplication: {operation(num1, num2, Operation.MULTIPLICATION)}")
    print(f"Division: {operation(num1, num2, Operation.DIVISION)}")