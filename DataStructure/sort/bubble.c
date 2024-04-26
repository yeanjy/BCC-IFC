#include <stdio.h>

void bubble(int arr[],int n)
{
  for(int i = 0; i < n; i++)
  {
    for(int j = 0; j < n-1; j++)
    {
      if(arr[j] > arr[j+1])
      {
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
} 

void printArray(int arr[], int n)
{
  for (int i = 0; i < n; i++)
    printf("%d\t", arr[i]);

  printf("\n");
}

int main()
{
  int arr[5] = {3, 1, 2, 7, 8};
  printArray(arr, 5);
  bubble(arr, 5);
  printArray(arr, 5);
  return 0;
}
