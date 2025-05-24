# def f(x):
    # return x * 2
    # x * 2

# print(type(f(3)))

# def f(x=2):
#     return x ** x
#
# print(f())
# print(f(3))
#
# def add_it(x,y=10):
#     return x + y
#
# result = add_it(2)
# print(result)

# def f():
#     x = 10
#
# print(x)

# x = 100
#
# def f():
#     global x
#     x += 1
#     print(x)
#
# f()

a = input("type a number: ")
b = input("type a number: ")
try:
    a = int(a)
    b = int(b)
    print(a /b)
# except ValueError:
#     print("a and b must be integers")
# except ZeroDivisionError:
#     print("b cannot be zero")
except (ValueError, ZeroDivisionError):
    print("Invalid input")

