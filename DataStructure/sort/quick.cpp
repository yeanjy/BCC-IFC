#include <iostream>
#include <utility>

template <typename T>
T partition(T *arr, T low, T high)
{
  int pivot = arr[high];

  int i = low;

  for (int j = low; j < high; j++)
  {
    if (arr[j]<pivot)
    {
      std::swap(arr[i], arr[j]);
      i++;
    }
  }
  std::swap(arr[i], arr[high]);
  return (i);
}

template <typename T>
void quick(T *arr,T low, T high)
{
  if (low < high)
  {
    int pivot = partition(arr, low, high);

    quick(arr, low, pivot-1);
    quick(arr, pivot+1, high);
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
  const int n = 12;
  int arr[n] = {3, 1, 5, 2, 6, 8, 7, 4, 19, 82, 32, 76};
  printArray(arr, n);
  quick(arr, 0, n-1);
  printArray(arr, n);
  return 0;
}
