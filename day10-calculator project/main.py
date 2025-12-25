from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1 , n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
print(logo)
num1 = float(input("enter the first number  : "))
for symbol in operations:
    print(symbol)
operation_symbol = input("pick an operation : ")
num2= float(input("enter the second number : "))

result = operations[operation_symbol] (num1 , num2)
print(result)
go = input("do you want to continue with last result? enter y or for new operation n")
while True:
    user_input = input()
    if user_input.lower() == 'q':
        break
    if go == "y":
        num1 = result
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation : ")
        num2 = float(input("enter the second number : "))
        result = operations[operation_symbol](result, num2)
        print(result)
    elif go == "n":
        num1 = float(input("enter the first number  : "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation : ")
        num2 = float(input("enter the second number : "))

        result = operations[operation_symbol](num1, num2)
        print(result)
