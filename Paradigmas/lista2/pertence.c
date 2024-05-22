#include <stdio.h>

int pertence(int arr[], int size, int n)
{
  for (int i = 0; i < size; i++)
  {
    if(arr[i] == n)
      return 1;
  }
  return 0; 
}

int main()
{
  int arr[] = {2, 3,4 ,5,6 ,7};
  printf("%d\n", pertence(arr, 6, 7));

  return 0;
}
