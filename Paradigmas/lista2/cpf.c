#include <ctype.h>
#include <stdio.h>
#include <string.h>

int isValidCPF(const char cpf[])
{
  if (strlen(cpf) != 11 || cpf == "11111111111" || cpf == "00000000000")
    return 0;

  int digitoverificador1 = 0;
  for(int i = 0; i < 9; i++)
  {
    digitoverificador1 += (cpf[i] - '0')*(i+1);
  }
  digitoverificador1 %= 11;

  if(digitoverificador1 == 10)
    digitoverificador1 = 0;
  
  if ((cpf[9] - '0') != digitoverificador1)
    return 0;

  int digitoverificador2 = 0;
  for(int i = 0; i <= 9; i++)
  {
    digitoverificador2 += (cpf[i] - '0')*i;
  }
  digitoverificador2 %= 11;

  if(digitoverificador2 == 10)
    digitoverificador2 = 0;

  if ((cpf[10] - '0') != digitoverificador2)
      return 0;

  return 1;
}

int main()
{
  printf("%d\n", isValidCPF("18516868000"));
  printf("%d\n", isValidCPF("61058697020"));
  printf("%d\n", isValidCPF("30212886012"));
  printf("%d\n", isValidCPF("80087176050"));
  printf("%d\n", isValidCPF("50958108041"));
  printf("%d\n", isValidCPF("46774249025"));

  return 0;
}
