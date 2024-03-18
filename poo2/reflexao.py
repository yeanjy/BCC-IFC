import sys


class Pessoa:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def print_info(self):
        print(self.__dict__)


class Padeiro(Pessoa):
    def __init__(self, nome, email, cpf, especialidade):
        super().__init__(nome, email, cpf)
        self.especialidade = especialidade


def discover(x):
    # Tipo da variável
    print(type(x).__name__)

    # Tamanho da variável em bytes
    print(sys.getsizeof(x))

    # Mostra o atributo 'nome' do objeto
    if hasattr(x, "email"):
        print(x.email)


def main():

    p = Pessoa("Jairo", "jairo@jairo.com", "000000000000")
    discover(p)

    print()

    pad = Padeiro("Carlos", "carlos@email.com", "22222222222", "Pães")
    discover(pad)


if __name__ == "__main__":
    main()
