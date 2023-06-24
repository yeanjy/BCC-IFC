def fibonnaci(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonnaci(number-1)+fibonnaci(number-2)


number = int(input("Digite:"))
result = fibonnaci(number)
print(result)