#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "slipsort.h"

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void merge(int left[], int nL, int right[], int nR, int arr[]) {
    int i = 0, j = 0, k = 0;

    while (i < nL && j < nR) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < nL) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < nR) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

void splitSort(int arr[], int n) {
    if (n <= 1) return;

    int splitPoint = (n > 1) ? max(1, n / 3) : 1;
    int nL = splitPoint;
    int nR = n - splitPoint;

    int *left = (int *)malloc(nL * sizeof(int));
    int *right = (int *)malloc(nR * sizeof(int));

    for (int i = 0; i < nL; i++)
        left[i] = arr[i];
    for (int i = 0; i < nR; i++)
        right[i] = arr[i + splitPoint];

    insertionSort(left, nL);
    splitSort(right, nR);
    merge(left, nL, right, nR, arr);

    free(left);
    free(right);
}

int main() {
    int n = 10; // Size of the array
    int *arr = malloc(n * sizeof(int)); // Dynamically allocate memory for the array

    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Seed for random number generation
    srand(time(NULL));

    // Filling the array with random numbers
    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100; // Random numbers between 0 and 99
        printf("%d ", arr[i]);
    }
    printf("\n");

    splitSort(arr, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");

    free(arr); // Free the dynamically allocated memory

    return 0;
}