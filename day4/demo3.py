def getnum_gen(n):
    for i in range(n):
        yield i

a = getnum_gen(5)

print(next(a))
print(next(a))
print(next(a))

