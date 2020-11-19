#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SUCCESS 0
#define FAILED -1
#define INCORRECT_INPUT -2
#define INVALID_POINTER -3
#define INCORRECT_OUTPUT -4
#define FILE_ER -5
#define EPS 0.00001
#define N 100

typedef struct
{
    char *name;
    long int pop;
    char *cap;
    char *cont;
    char *tour;
    union  {
        struct {
            int cnt_plc;
            char *view;
        } excurs;
        struct {
            int month;
            double tmp_w;
            double tmp_a;
            double trvl_time;
        } beach;
        struct {
            char *kind;
            long int min_cost;
        } sport;
    } tours;
} Country;

typedef Country countries[N];

//cdio
int read_file(countries *countries, int *n)
{
    FILE *f = fopen("Country.txt", "r");
    if (f == NULL)
    {
        printf("FILE error");
        return FILE_ER;
    }
    if (feof(f))
    {
        printf("FILE is empty");
        return FILE_ER;
    }
    int i = 0;
    char str[64];
    while (1)
    {
        fscanf(f, "%s", &countries[i]->name);
        //fgets(str, sizeof(str), f);
        printf("str = %s \n", str);
        strncpy(countries[i]->name, str, 32);
        //countries[i].name = str;
        printf("str = %s \n", str);
        fgets(str, sizeof(str), f);
        countries[i]->pop = atol(str);
        printf("str = %s \n", str);
        fgets(str, sizeof(str), f);
        countries[i]->cap = str;
        printf("str = %s \n", str);
        fgets(str, sizeof(str), f);
        countries[i]->cont = str;
        printf("str = %s \n", str);
        fgets(str, sizeof(str), f);
        countries[i]->tour = str;
        printf("str = %s \n", str);
        if (strcmp(countries[i]->tour, "excurs\n") == 0)
        {
            printf("i = %d \n", i);
            fgets(str, sizeof(str), f);
            countries[i]->tours.excurs.cnt_plc = atoi(str);
            printf("str = %s \n", str);
            fgets(str, sizeof(str), f);
            countries[i]->tours.excurs.view = str;
            printf("str = %s \n", str);
        }
        else
        {
            if (strcmp(countries[i]->tour, "beach\n") == 0)
            {
                fgets(str, sizeof(str), f);
                countries[i]->tours.beach.month = atoi(str);
                printf("str = %s \n", str);
                fgets(str, sizeof(str), f);
                countries[i]->tours.beach.tmp_a = atof(str);
                printf("str = %s \n", str);
                fgets(str, sizeof(str), f);
                countries[i]->tours.beach.tmp_w = atof(str);
                printf("str = %s \n", str);
                fgets(str, sizeof(str), f);
                countries[i]->tours.beach.trvl_time = atof(str);
                printf("str = %s \n", str);
            }
            else
                if (strcmp(countries[i]->tour, "sport\n") == 0)
                {
                    fgets(str, sizeof(str), f);
                    countries[i]->tours.sport.kind = str;
                    printf("str = %s \n", str);
                    fgets(str, sizeof(str), f);
                    countries[i]->tours.sport.min_cost = atol(str);
                    printf("str = %s \n", str);
                }
        }
        i++;
        if ( feof(f) != 0)
            break;
    }
    *n = i;
    fclose(f);
    return SUCCESS;
}
//int add_country(struct *countries)


void output_struct(countries countries, int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("County: %s \n", countries[i].name);
        printf("  population: %ld \n", countries[i].pop);
        printf("  capital: %s \n", countries[i].cap);
        printf("  mainland: %s \n", countries[i].cont);
        printf("  kind of tourism: %s \n", countries[i].tour);
        if (strcmp(countries[i].tour, "excurs\n") == 0)
        {
            printf("    number of objects: %d \n", countries[i].tours.excurs.cnt_plc);
            printf("    main type: %s \n", countries[i].tours.excurs.view);
        }
        else
        {
            if (strcmp(countries[i].tour, "beach\n") == 0)
            {
                printf("    month: %d \n", countries[i].tours.beach.month);
                printf("    air temperature: %f \n", countries[i].tours.beach.tmp_a);
                printf("    water temperature: %f \n", countries[i].tours.beach.tmp_w);
                printf("    time of flight: %f \n", countries[i].tours.beach.trvl_time);
            }
            else
                if (strcmp(countries[i].tour, "sport\n") == 0)
                {
                    printf("    kind: %s \n", countries[i].tours.sport.kind);
                    printf("    min_cost: %ld \n", countries[i].tours.sport.min_cost);
                }
        }
    }

}

int main()
{
    countries countries;
    int n;
    read_file(&countries, &n);
    printf("n = %d \n", n);
    output_struct(countries, n);
    return SUCCESS;
}
