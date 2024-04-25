#include <iostream>
using namespace std;

class pessoa {
public:
  pessoa();

protected:
  string cpf;
  string nome;
  string email;
  string telefone;
};

class vendedor {
public:
  vendedor();

private:
  pessoa p;
  double comissao;
  string AreaDeVenda;
};

class motorista {
public:
  motorista();

private:
  pessoa p;
  int numeroCNH;
  string dataDeVencimentoCNH;
};

class veiculo {
public:
  veiculo();

protected:
  string placa;
  string cor;
  string modelo;
  vendedor v;
  motorista m;
};

class carro {
public:
  carro();

private:
  veiculo v;
  int numeroDeLugares;
  string renavam;
};

class moto {
public:
  moto();

private:
  veiculo v;
  string cilindradas;
};
