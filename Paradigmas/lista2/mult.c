#include <stdio.h>

int mult(int n, int m)
{
  if (m > 0)
    return n + mult(n, m-1); 

  return m;
}

int quantidade(int n)
{
  if (n>=10)
    return 1 + quantidade(n/10);

  return 1;
}

int main()
{
  printf("%d\n", mult(4, 12)); 

  return 0;
}
