# 1
def nijo(number: int):
    return number * number

# 2
def str_print(text: str):
    print(text)

# 3
def test_func(a,b,c,d="d",e="e"):
    print(a,b,c,d,e)

# 4
def return_divide_by_two(num: int):
    return num // 2

def return_multiply_by_four(num: int):
    print(num)
    return num * 4

x = return_divide_by_two(10)
return_multiply_by_four(x)

# 5
def convert_str_to_float(text: str):
    try:
        return float(text)
    except ValueError:
        print("Invalid input")

