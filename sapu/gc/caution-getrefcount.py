import sys

x = 0
print(f"xの参照カウント? {sys.getrefcount(x) - 1}")