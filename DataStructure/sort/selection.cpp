#include <iostream>

template <typename T>
void selectionSort(T *a, int n)
{
  for(int i = 0; i < n-1; i++)
  {
    int min = i;
    for (int j = i+1; j < n; j++)
    {
      if (a[min] > a[j]) 
      {
        min = j;
      }
    }

    int temp = a[min];
    a[min] = a[i];
    a[i] = temp; 
  }
}

template <typename T>
void printArray(T *a, int n)
{
  for (int i = 0; i < n; i++)
    printf("%d\t", a[i]);

  printf("\n");
}

int main()
{
  const int n = 5;
  int arr[n] = {3, 2, 1, 8, 7};
  printArray(arr, n);
  selectionSort(arr, n);
  printArray(arr, n);

  return 0;
} 
