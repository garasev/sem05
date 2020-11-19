#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EXIT_SUCCESS 0
#define EXIT_FAILED -1
#define EXIT_INCORRECT_INPUT -2
#define EXIT_INVALID_POINTER -3
#define EPS 0.00001

typedef double * ptr_t;

int len(ptr_t ast, ptr_t afn)
{
    return (afn - ast);
}

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

void resize(ptr_t *arr,long long int *n, long long int newn)
{
    double * buf = (double*)realloc(*arr, newn * sizeof(double));
    (*arr) = buf;
    buf = NULL;
    *n = newn;
}

double aver_geom(ptr_t arr, ptr_t arr_end)
{
    double multi = 1, result, count = 0;
    for (ptr_t i = arr; i < arr_end; i++)
    {
        multi *= *i;
        count += 1;
    }
    result = pow(multi, (1 / count));
    return result;
}

void delete_nearest_elem(ptr_t *arr, ptr_t *arr_end, double u)
{
    double diff;
    diff = fabs(**arr - u);
    for (ptr_t i = *arr; i < *arr_end; i++)
        if(diff > fabs(*i - u))
            diff = fabs(*i - u);
    printf("diff = %lf \n", diff);
    ptr_t i = *arr;
    while(1)
    {
        if (fabs(fabs(*i - u) - diff) < EPS)
        {
            for (ptr_t j = i; j < *arr_end; j++)
                *j = *(j + 1);
            arr_end --;
            break;
        }
        i++;
    }
}

double calculate_u2(ptr_t arr, ptr_t arr_end)
{
    double u, max_a = *arr, min_a = *arr;
    for (ptr_t i = (arr + 1); i < arr_end; i++)
    {
        if (max_a < *i)
            max_a = *i;
        if (min_a > *i)
            min_a = *i;
    }
    u = min_a * max_a / (1 + abs(min_a) + abs(max_a));
    return u;
}

int create_new_arr(ptr_t arr, ptr_t arr_end, long long int n, long long int p, double u)
{
    for (ptr_t i = arr_end - 3; i > arr + p; i--)
        *i = *(i - 1);
    *(arr + p) = u;
    for (ptr_t i = arr_end - 2; i > arr; i--)
        *i = *(i - 1);
    *arr = u;
    *(arr_end - 1) = u;
    return EXIT_SUCCESS;
}

int main()
{
    long long int check_int, n, p;
    float check_float;
    printf("Input size of array: ");
    if (scanf("%f", &check_float) != 1)
    {
        printf(" Incorrect input size of array1");
        return EXIT_INCORRECT_INPUT;
    }
    check_int = check_float;
    if ((check_int - check_float) != 0)
    {
        printf(" Incorrect input size of array2");
        return EXIT_INCORRECT_INPUT;
    }
    n = check_int;
    ptr_t arr = NULL, arr_end = NULL;
    arr_end = arr + n;
    if (create_fill_arr(&arr, &arr_end, n) != 0)
    {
        printf("Error of create or fill array");
        return EXIT_FAILED;
    }
    double u = aver_geom(arr, arr_end);
    printf("u = %lf \n", u);
    if (n == 1 || n == 2)
    {
        printf("Delete all elem.");
        return EXIT_INCORRECT_INPUT;
    }
    output_arr(arr, arr_end);
    delete_nearest_elem(&arr, &arr_end, u);
    output_arr(arr, arr_end);
    resize(&arr, &n, (n - 1));
    arr_end = arr + n;
    delete_nearest_elem(&arr, &arr_end, u);
    output_arr(arr, arr_end);
    resize(&arr, &n, (n - 1));
    arr_end = arr + n;
    u = calculate_u2(arr, arr_end);
    printf("Input p: ");
    if (scanf("%f", &check_float) != 1 || check_float > (n - 1) || check_float < 0)
    {
        printf(" Incorrect input p");
        return EXIT_INCORRECT_INPUT;
    }
    check_int = check_float;
    if ((check_int - check_float) != 0)
    {
        printf(" Incorrect input p");
        return EXIT_INCORRECT_INPUT;
    }
    p = check_int;
    resize(&arr, &n, (n + 3));
    arr_end = arr + n;
    if (create_new_arr(arr, arr_end, n, p, u) != 0)
    {
        printf("Fail creating second array");
        return EXIT_FAILED;
    }
    output_arr(arr, arr_end);

    return EXIT_SUCCESS;
}
