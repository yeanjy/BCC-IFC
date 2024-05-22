#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int isPrime(int n)
{
  if (n <= 1)
    return 0;

  for(int i = 2; i <= n/2; i++)
  {
    if (n % i == 0)
      return 0;
  }
  return 1;
}

void drawPrimes(int arr[], int size)
{
  srand(time(0));
  int count = 0;

  while(count < size)
  {
    int r = rand()%101;
    if(isPrime(r))
    {
      arr[count] = r;
      count++;
    }
  }
}

void drawDiferentPrimes(int arr[], int size)
{
  srand(time(0)); 
  int count = 0;

outerloop:
  while (count < size)
  {
    int r = rand()%101;
    if (isPrime(r))
    { 
      for(int i = 0; i < count; i++)
      {
        if (r == arr[i])
          goto outerloop;
      }

      arr[count] = r;
      count++;
    }
  }
}

void printArray(int arr[], int size)
{
  for (int i = 0; i < size; i++)
  {
    printf("%d\n", arr[i]);
  }
}

int main()
{
  int arr[25]; 
  drawPrimes(arr, 25);
  printArray(arr, 25);

  return 0;
}
