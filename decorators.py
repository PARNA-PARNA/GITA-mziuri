from functools import wraps
from datetime import datetime


ALLOWED = ['admin', 'user']


def auth_permission(role: str):
    def decorator(func):
        @wraps(func)
        def wrapper():
            if role.lower() not in ALLOWED:
                return "You are not allowed to do this action!"
            else:
                return func()
        return wrapper
    return decorator


def repeat_decorator(n):
    def decorator(func):
        @wraps(func)
        def wrapper(a, b):
            print('start')
            for _ in range(n):
                print(func(a, b))
            print('end')
        return wrapper
    return decorator


def my_decorator(func):
    @wraps(func)
    def wrapper(a, b):
        print("დეკორატორი დაიწყო!")
        print(f"ფუნქცია {func.__name__}({a}, {b})")
        result = func(a, b)
        print(f"ფუნქციის შედეგი {result}")
        print('დეკორატორი დასრულდა!')
    return wrapper


def log_math_operations(func):
    @wraps(func)
    def wrapper(a, b):
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - {func.__name__}({a}, {b}) -> {func(a, b)}\n")
    return wrapper
