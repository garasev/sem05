#include "var.h"
#include "cdio.h"
#include "functions.h"


int main()
{
    long long int check_int, n, p;
    float check_float;
    printf("Input size of array: ");
    if (scanf("%f", &check_float) != 1)
    {
        printf(" Incorrect input size of array");
        return EXIT_INCORRECT_INPUT;
    }
    check_int = check_float;
    if ((check_int - check_float) != 0)
    {
        printf(" Incorrect input size of array");
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
    if (n == 1 || n == 2)
    {
        printf("Delete all elem.");
        return EXIT_INCORRECT_INPUT;
    }
    delete_nearest_elem(&arr, &arr_end, u);
    resize(&arr, &n, (n - 1));
    arr_end = arr + n;
    delete_nearest_elem(&arr, &arr_end, u);
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
    if (p >= n || p < 0)
    {
        printf(" Incorrect input p");
        return EXIT_INCORRECT_INPUT;
    }
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
