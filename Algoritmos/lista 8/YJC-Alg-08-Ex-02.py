def fibonnaci(number):
    if number == 1:
        return 0
    if number == 2:
        return 1
    return fibonnaci(number-1)+fibonnaci(number-2)


number = int(input("Digite:"))
result = fibonnaci(number)
print(result)