def f(x):
    return x * x

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 8])