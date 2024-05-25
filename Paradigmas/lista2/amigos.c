#include <stdio.h>

int isFriendNumber(int n, int m)
{
  if (n <=0 || m <= 0)
    return 0;

  int sn = 1;
  int sm = 1;

  for (int i = 2; i < n; i++)
  {
    if(n%i==0)
      sn += i;
  }
  for (int i = 2; i < m; i++)
  {
      if(m%i==0)
        sm += i;
  }

  return (sn == m) && (sm == n);
}

int main()
{
  printf("%d\n", isFriendNumber(1210, 1184)); 

  return 0;
}
