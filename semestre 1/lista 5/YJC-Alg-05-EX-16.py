def convert_to_decimal(number, base):
    decimal = 0
    power = 0
    digits = "0123456789ABCDEF"

    for digit in reversed(number):
        decimal += digits.index(digit) * base**power
        power += 1

    return decimal

def convert_from_decimal(decimal, base):
    if decimal == 0:
        return '0'

    digits = []
    while decimal > 0:
        digit = decimal % base
        digits.append(str(digit))
        decimal //= base

    return ''.join(reversed(digits))

def main():
    input_number = input("Digite o número: ")
    input_base = int(input("Digite a base do número: "))
    output_base = int(input("Digite a base para conversão: "))

    decimal_number = convert_to_decimal(input_number, input_base)
    output_number = convert_from_decimal(decimal_number, output_base)

    print("Resultado:", output_number)

if __name__ == "__main__":
    main()
