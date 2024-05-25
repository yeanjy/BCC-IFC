#include <stdio.h>

int mult(int n, int m)
{
  if (n<0 && m <0)
    return mult(-n, -m);

  if (m < 0)
    return -mult(n, -m);

  if (m > 0)
    return n + mult(n, m-1); 

  return m;
}

double multi(double n, double m)
{
  if (n<0 && m <0)
    return multi(-n, -m);

  if (m < 0)
    return -multi(n, -m);

  if (m > 0)
    return n + multi(n, m-1); 

  return m;
}

int quantidade(int n)
{
  if (n<0)
    n = -n;
  
  if (n>=10)
    return 1 + quantidade(n/10);

  return 1;
}

int main()
{
  printf("%d\n", mult(9, 0)); 

  return 0;
}
