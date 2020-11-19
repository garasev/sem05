#include "var.h"
#include "cdio.h"
#include <stdlib.h>

int create_fill_arr(ptr_t *arr, ptr_t *arr_end, long long int n)
{
    printf("Input elem of array: \n");
    *arr = (ptr_t)malloc(n * sizeof(double));
    *arr_end = *arr + n;
    if (! arr)
    {
        free(*arr);
        return EXIT_INVALID_POINTER;
    }
    for (ptr_t i = *arr; i < *arr_end; i++)
    {
        if (scanf("%lf", i) != 1)
        {
            free(*arr);
            return EXIT_INCORRECT_INPUT;
        }
    }
    return EXIT_SUCCESS;
}

void output_arr(ptr_t arr, ptr_t arr_end)
{
    printf("Array: \n");
    for (ptr_t i = arr; i < arr_end; i++)
        printf("%lf ", *i);
    printf("\n");
}

void delete_arr(ptr_t *arr, ptr_t *arr_end)
{
    free(*arr);
    *arr_end = NULL;
}

void resize(ptr_t *arr, long long int *n, long long int newn)
{
    double *buf = (double*)realloc(*arr, newn * sizeof(double));
    (*arr) = buf;
    buf = NULL;
    *n = newn;
}
