#include <stdio.h>

int fibonacci(int n)
{
  if (n == 0 || n == 1)
    return n;
  return fibonacci(n-1) + fibonacci(n-2);
}

int loopfibonacci(int n)
{
  int f = 1;
  int f1 = 1;
  int result = 0;

  if (n == 1 || n == 2)
    return f;

  for(int i = 3; i <= n; i++)
  {
    result = f + f1; 
    f = f1;
    f1 = result;
  }

  return result; 
}

int main()
{
  int a = loopfibonacci(7);
  printf("%d\n", a);
  return 0;
}
