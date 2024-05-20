#include <stdio.h>

int fatorial(int n)
{
  int result = 1;

  if (n < 2)
    return result;

  while (n > 0)
  {
    result *= n;
    n--;
  }

  return result;
}

int rfatorial(int n)
{
  if (n < 2)
    return 1;
  return n*rfatorial(n-1);
}

int main()
{
  int a = fatorial(5);
  int b = rfatorial(5);
  printf("%d\n", a);
  printf("%d\n", b);
  return 0;
}
