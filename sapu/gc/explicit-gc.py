# explicit 明示的な
import tracemalloc
import gc


tracemalloc.start()

def foo():
    x = [0] * (10**6)
    ss = tracemalloc.take_snapshot()
    for s in ss.statistics("filename"):
        print("関数内でx解放前", s)

    del x
    gc.collect()

    ss = tracemalloc.take_snapshot()
    for s in ss.statistics("filename"):
        print("関数内でx解放後", s)
    y = [1] * (10 ** 6)

foo()
ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print("関数外", s)

tracemalloc.stop()
