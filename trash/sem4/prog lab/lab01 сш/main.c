#include <stdio.h>

#define CORRECT_ENDING 0
#define FILE_ER -1
#define SIZE_ER -2
#define ELEM_ER -3

int create_arr(FILE *f, int n, int *arr)
{
    float a;
    for(int i = 0; i < n; i++)
    {
        if(fscanf(f, "%f", &a) != 1)
            return ELEM_ER;
        int b = a;
        if (a - b != 0)
            return ELEM_ER;
        arr[i] = b;
    }
    return CORRECT_ENDING;
}

void copy_arr(int *arr, int *cop, int n)
{
    for(int i = 0; i < n; i++)
        cop[i] = arr[i];
}

void z1(int *arr, int n)
{
    int s1 = 0, s2 = 0;
    for(int i = 0; i < n; i++)
    {
        if(arr[i] % 10 == 3)
            s2 += arr[i];
        if(arr[i] % 3 == 0)
            s1 += arr[i];
    }
    printf("\nZadanie #1 \n");
    if(s1 > s2)
        printf(" multiple 3 = %d > %d = ending 3", s1, s2);
    else
        if (s1 < s2)
            printf(" multiple 3 = %d < %d = ending 3", s1, s2);
        else
            printf(" multiple 3 = %d == %d = ending 3", s1, s2);
}

void z2(int *arr, int n)
{
    int even = -1, odd = -1;
    for(int i = 0; i < n; i++)
    {
        if(arr[i] % 2 == 0 && even == -1)
            even = i;
        if(arr[i] % 2 == 1 || arr[i] % 2 == -1)
            odd = i;
    }
    int swap;
    printf("\nZadanie #2 \n");
    if(even != -1 && odd != -1)
    {
        swap = arr[even];
        arr[even] = arr[odd];
        arr[odd] = swap;
        for(int i = 0; i < n; i++)
        {
            printf(" %d", arr[i]);
        }
    }
    else
        printf(" Don't have one of even or odd element.");
}

void z3(int *arr, int n)
{
    int m = -1;
    for(int i = 0; i < n; i++)
        if(arr[i] > 0 && arr[i] > m)
            m = arr[i];
    printf("\nZadanie #3 \n");
    if(m == -1)
        printf(" Don't have positive elements.");
    else
        printf(" Max positive elem: %d", m);
}

void z4(int *arr, int n)
{
    int d = 0;
    for(int i = 0; i < n - d; i++)

        if(arr[i] < 0)
        {
            for(int j = i; j < n - d - 1; j++)
                arr[j] = arr[j + 1];
            d += 1;
            i -= 1;
        }
    printf("\nZadanie #4 \n");
    for(int i = 0; i < n - d; i++)
        printf(" %d", arr[i]);
    if(d == n)
        printf(" DELETED all elements.");
}

int main(int argc, char **argv)
{
    float proverka;
    int arr[10], cop[10];
    FILE *f = fopen(argv[1], "rt");
    if (f == NULL)
    {
        printf("FILE error");
        return FILE_ER;
    }
    if (feof(f))
    {
        printf("FILE is empty");
        return SIZE_ER;
    }
    if (fscanf(f, "%f", &proverka) != 1 || proverka < 1 || proverka >10)
    {
        printf("Size of array error");
        return SIZE_ER;
    }
    int n = proverka;
    if (n - proverka != 0)
    {
        printf("Size of array error");
        return SIZE_ER;
    }
    if (create_arr(f, n, arr) != 0)
        return ELEM_ER;
    printf("Start array: \n");
    for(int i = 0; i < n; i++)
        printf(" %d ", arr[i]);
    z1(arr, n);
    copy_arr(arr, cop, n);
    z2(cop, n);
    z3(arr, n);
    copy_arr(arr, cop, n);
    z4(cop, n);
    fclose(f);
    return CORRECT_ENDING;
}
