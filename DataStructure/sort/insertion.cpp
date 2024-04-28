#include <iostream>

template <typename T>
void insertion(T *arr,int n)
{
  for (int i = 1; i < n; i++) 
  {
    auto key = arr[i];
    int j = i-1;

    while (j >= 0 && arr[j] > key)
    {
      arr[j+1] = arr[j];
      j--;
    }
    arr[j+1] = key;
  }
} 

template <typename T>
void insertionSort(T *arr,int n)
{
  for (int i = 1; i < n; i++) 
  {
    int j = i;

    while (j > 0 && arr[j] < arr[j-1])
    {
      auto temp = arr[j-1];
      arr[j-1] = arr[j];
      arr[j] = temp;
      j--;
    }
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
  const int n = 8;
  int arr[8] = {3, 1, 5, 2, 6, 8, 7, 4};
  printArray(arr, n);
  insertionSort(arr, n);
  printArray(arr, n);
  return 0;
}
