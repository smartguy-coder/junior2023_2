some_data = [5, 6, 9, 10, 1, 11]

data = filter(lambda number: number > 5, some_data)

print(next(data))
print(next(data))
print(9999999999999999999999)
print(next(data))
print(next(data))
# print(next(data))

some_data2 = (item for item in some_data if item > 5)
print(next(some_data2))
print(next(some_data2))
some_data[5] = 800
print(99999999999988888888888)
print(next(some_data2))
print(next(some_data2))
#
# for i in data:
#     print(i)


def foo():
    yield 5




# print(next(foo()))