#include <stdio.h>

int isPerfectNumber(int n)
{
  int sn = 1;

  for (int i = 2; i < n; i++)
    if (n%i == 0)
      sn += i;

  return n == sn;
}

int main()
{
  printf("%d\n", isPerfectNumber(6)); 

  return 0;
}
