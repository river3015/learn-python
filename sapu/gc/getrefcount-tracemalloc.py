import sys
import tracemalloc


tracemalloc.start()

def foo():
    x = [0] * (10**6)
    print(f"xの参照カウント: {sys.getrefcount(x) - 1}")
    y = x
    print(f"xの参照カウント: {sys.getrefcount(x) - 1}")
    ss = tracemalloc.take_snapshot()
    for s in ss.statistics("filename"):
        print("関数内部", s)

foo()
ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print("関数外部", s)
