def isInteger(string):
    string = string.strip()
    if len(string) == 0:
        return False
    if string[0] == '+' or string[0] == '-':
        if all(char.isdigit() for char in string[1:]):
            return True

    if all(char.isdigit() for char in string):
        return True

    return False


string = input("Digite uma string: ")
if isInteger(string):
    print("A string representa um número inteiro.")
else:
    print("A string não representa um número inteiro.")
