def fn(x):
    print(x)
    bomba(x - 1)


def bomba(n):
    print("Bommm") if n <= 0 else fn(n)
