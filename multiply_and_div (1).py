from my_math.decorators import log_math_operations


@log_math_operations
def multiply(a, b):
    return a * b


@log_math_operations
def division(a, b):
    if b == 0:
        return "Division By Zero"
    return a / b


if __name__ == '__main__':
    print(f"mutliply module : {multiply(5, 7)}")
    print(f"division : {division(5, 0)}")