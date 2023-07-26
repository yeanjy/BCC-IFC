def fat(number):
    return 1 if number == 1 else fat(number-1)*number

number = int(input("Digite:"))
result = fat(number)
print(result)