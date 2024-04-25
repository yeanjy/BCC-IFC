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

class vendedor : public pessoa {
public:
  vendedor();

private:
  double comissao;
  string AreaDeVenda;
};

class motorista : public pessoa {
public:
  motorista();

private:
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

class carro : public veiculo {
public:
  carro();

private:
  int numeroDeLugares;
  string renavam;
};

class moto : public veiculo {
public:
  moto();

private:
  string cilindradas;
};
