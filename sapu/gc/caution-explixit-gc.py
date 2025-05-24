import tracemalloc
import gc
import sys


tracemalloc.start()

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.data = [0] * (10**6)
user_1 = User("鈴木")
user_2 = User("田中")
print(f"user_1の参照カウント: {sys.getrefcount(user_1) - 1}")
ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print("user_1のappend前", s)
user_2.friends.append(user_1)
ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print("user_1のappend後", s)
print(f"user_1の参照カウント: {sys.getrefcount(user_1) - 1}")

del user_1
gc.collect()

ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print("gc後", s)




tracemalloc.stop()