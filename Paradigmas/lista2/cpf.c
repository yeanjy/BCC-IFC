#include <ctype.h>
#include <stdio.h>
#include <string.h>

int isValidCPF(const char cpf[])
{
  if (strlen(cpf) != 11)
    return 0;

  int count = 0;

  for (int i = 0; i < 11; i++)
  {
    if (!isdigit(cpf[i]))
    {
      return 0;
    }
    else 
    {
      int num = cpf[i] - '0';
      count += num;
    }
  }

  if ((count % 11) != 0)
    return 0;

  return 1;
}

int main()
{
  printf("%d\n", isValidCPF("01136462910"));

  return 0;
}
