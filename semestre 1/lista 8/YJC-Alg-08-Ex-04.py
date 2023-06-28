def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result

number = int(input("Digite:"))
result = fibonacci(number)
print(result)