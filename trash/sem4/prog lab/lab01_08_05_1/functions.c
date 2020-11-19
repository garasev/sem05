#include "var.h"
#include "functions.h"
#include <math.h>

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
        if (diff > fabs(*i - u))
            diff = fabs(*i - u);
    ptr_t i = *arr;
    while (1)
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
