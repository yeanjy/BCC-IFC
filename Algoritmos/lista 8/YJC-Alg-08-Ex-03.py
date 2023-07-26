import string
def palindromo(s):
    a = str.maketrans("", "", string.punctuation + " ")
    s = s.translate(a)
    if len(s) <= 1:
        return True

    return s[0] == s[-1] and palindromo(s[1:-1])

s = (input("Digite:"))
result = palindromo(s)
print(result)