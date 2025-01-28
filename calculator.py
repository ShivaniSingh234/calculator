import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is undefined."
    return a % b

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide", "power", "modulus"],
                        help="Choose an operation to perform")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")

    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "modulus": modulus,
    }

    operation_function = operations[args.operation]
    result = operation_function(args.a, args.b)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()


