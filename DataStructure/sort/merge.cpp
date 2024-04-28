
#include <iostream>

template <typename T>
void merge(T *arr, int inicio, int medio, int final) {
    int n1 = medio - inicio + 1;
    int n2 = final - medio;

    T l[n1];
    T r[n2];

    for (int i = 0; i < n1; i++) {
        l[i] = arr[inicio + i];
    }
    for (int j = 0; j < n2; j++) {
        r[j] = arr[medio + 1 + j];  
    }

    int i = 0, j = 0, k = inicio;  

    while (i < n1 && j < n2) {
        if (l[i] <= r[j]) {
            arr[k] = l[i];
            i++;
        } else {
            arr[k] = r[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = l[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = r[j];
        j++;
        k++;
    }
}

template <typename T>
void mergeSort(T *arr, int inicio, int final) {
    if (inicio < final) {
        int m = inicio + (final - inicio) / 2;
        mergeSort(arr, inicio, m);
        mergeSort(arr, m + 1, final);

        merge(arr, inicio, m, final);
    }
}

template <typename T>
void printArray(T *a, int n) {
    for (int i = 0; i < n; i++)
        std::cout << a[i] << "\t";

    std::cout << std::endl;
}

int main() {
    const int n = 5;
    int arr[n] = {3, 1, 2, 7, 8};
    printArray(arr, n);
    mergeSort(arr, 0, n - 1);
    printArray(arr, n);
    return 0;
}
