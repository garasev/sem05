#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define SUCCESS 0
#define FAILED -1
#define INCORRECT_INPUT -2
#define INVALID_POINTER -3
#define INCORRECT_OUTPUT -4
#define FILE_ER -5
#define OVERFLOW -6
#define EPS 0.00001
#define N 100
#define ITERATIONS 1000000

typedef struct
{
    char name[31];
    long int pop;
    char cap[31];
    char cont[31];
    char tour[31];
    union  {
        struct {
            int cnt_plc;
            char view[31];
        } excurs;
        struct {
            int month;
            double tmp_w;
            double tmp_a;
            double trvl_time;
        } beach;
        struct {
            char kind[31];
            long int min_cost;
        } sport;
    } tours;
} Country_t;

typedef struct
{
    int id;
    char name[31];
} key_t;
//cdio

void shuffle(Country_t *countries, key_t *key, int n)
{
    srand(time(NULL));
    for (int i = n - 1; i >= 0; i--)
    {
        int j = rand() % (i + 1);
        Country_t tmp_c = countries[j];
        countries[j] = countries[i];
        countries[i] = tmp_c;
        key_t tmp_k = key[j];
        key[j] = key[i];
        key[i] = tmp_k;
    }
}

void input_struct(char *str, Country_t *countries, key_t *key)
{
    char *p_str = strtok(str, " ");
    strcpy((*countries).name, p_str);
    strcpy((*key).name, p_str);
    p_str = strtok(NULL, " ");
    (*countries).pop = atol(p_str);
    p_str = strtok(NULL, " ");
    strcpy((*countries).cap, p_str);
    p_str = strtok(NULL, " ");
    strcpy((*countries).cont, p_str);
    p_str = strtok(NULL, " ");
    strcpy((*countries).tour, p_str);
    if (strcmp((*countries).tour, "excurs") == 0)
    {
        p_str = strtok(NULL, " ");
        (*countries).tours.excurs.cnt_plc = atoi(p_str);
        p_str = strtok(NULL, "\n");
        strcpy((*countries).tours.excurs.view, p_str);
    }
    else
    {
        if (strcmp((*countries).tour, "beach") == 0)
        {
            p_str = strtok(NULL, " ");
            (*countries).tours.beach.month = atoi(p_str);
            p_str = strtok(NULL, " ");
            (*countries).tours.beach.tmp_a = atof(p_str);
            p_str = strtok(NULL, " ");
            (*countries).tours.beach.tmp_w = atof(p_str);
            p_str = strtok(NULL, "\n");
            (*countries).tours.beach.trvl_time = atof(p_str);
        }
        else
            if (strcmp((*countries).tour, "sport") == 0)
            {
                p_str = strtok(NULL, " ");
                strcpy((*countries).tours.sport.kind, p_str);
                p_str = strtok(NULL, "\n");
                (*countries).tours.sport.min_cost = atol(p_str);
            }
    }
}

int read_file(Country_t *countries, key_t *key, int *n)
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
    *n = 0;
    char str[256];
    while (1)
    {
        fgets(str, 256, f);
        if (str[0] != '\n')
        {
            input_struct(str, &countries[(*n)], &key[(*n)]);
            key[*n].id = *n + 1;
        }
        else
            (*n)--;
        (*n)++;
        if ( feof(f) != 0)
            break;
    }
    fclose(f);
    return SUCCESS;
}

int add_country(Country_t *countries, key_t *key, int *n)
{
    if (*n == 100)
        return OVERFLOW;
    FILE *f = fopen("Country.txt", "a+");
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
    char str[256], result[256];
    double check_d;
    long int check_li;
    int check_i;
    memset(result, '\0', 256);
    printf("  Input country NAME: ");
    if (scanf("%s", str) != 1)
        return INCORRECT_INPUT;
    if (strlen(str) > 31)
        return INCORRECT_INPUT;
    strcat(result, str);
    strcat(result, " ");
    printf("  Input country POPULATION: ");
    if (scanf("%lf", &check_d) != 1)
        return INCORRECT_INPUT;
    check_li = check_d;
    if (check_li - check_d != 0)
        return INCORRECT_INPUT;
    if (strlen(str) > 31)
        return INCORRECT_INPUT;
    itoa(check_d, str, 10);
    strcat(result, str);
    strcat(result, " ");
    printf("  Input country CAPITAL: ");
    if (scanf("%s", str) != 1)
        return INCORRECT_INPUT;
    if (strlen(str) > 31)
        return INCORRECT_INPUT;
    strcat(result, str);
    strcat(result, " ");
    printf("  Input country MAINLAND: ");
    if (scanf("%s", str) != 1)
        return INCORRECT_INPUT;
    if (strlen(str) > 31)
        return INCORRECT_INPUT;
    strcat(result, str);
    strcat(result, " ");
    printf("   1 - excursion \n");
    printf("   2 - beach \n");
    printf("   3 - sport \n");
    printf("  Choise country KIND OF TOURISM: ");
    if (scanf("%lf", &check_d) != 1)
        return INCORRECT_INPUT;
    check_i = check_d;
    if (check_i - check_d != 0)
        return INCORRECT_INPUT;
    if (check_i == 1)
    {
        strcat(result, "excurs ");
        printf("  Input country NUMBER OF OBJECTS: ");
        if (scanf("%lf", &check_d) != 1)
            return INCORRECT_INPUT;
        check_i = check_d;
        if (check_i - check_d != 0 || check_i < 0)
            return INCORRECT_INPUT;
        itoa(check_d, str, 10);
        strcat(result, str);
        strcat(result, " ");
        printf("   1 - natural \n");
        printf("   2 - history \n");
        printf("   3 - art \n");
        printf("  Choise country MAIN TYPE: ");
        if (scanf("%lf", &check_d) != 1)
            return INCORRECT_INPUT;
        check_i = check_d;
        if (check_i - check_d != 0)
            return INCORRECT_INPUT;
        switch (check_i) {
            case 1:
                strcat(result, "natural");
                break;
            case 2:
                strcat(result, "history");
                break;
            case 3:
                strcat(result, "art");
                break;
            default:
                return INCORRECT_INPUT;
        }
    }
    else
    {
        if (check_i == 2)
        {
            strcat(result, "beach ");
            printf("  Input country main month: ");
            if (scanf("%lf", &check_d) != 1)
                return INCORRECT_INPUT;
            check_li = check_d;
            if (check_li - check_d != 0)
                return INCORRECT_INPUT;
            itoa(check_d, str, 10);
            strcat(result, str);
            strcat(result, " ");
            printf("  Input country temperature water: ");
            if (scanf("%lf", &check_d) != 1)
                return INCORRECT_INPUT;
            itoa(check_d, str, 10);
            strcat(result, str);
            strcat(result, " ");
            printf("  Input country temperature air: ");
            if (scanf("%lf", &check_d) != 1)
                return INCORRECT_INPUT;
            itoa(check_d, str, 10);
            strcat(result, str);
            strcat(result, " ");
            printf("  Input country time of flight: ");
            if (scanf("%lf", &check_d) != 1)
                return INCORRECT_INPUT;
            itoa(check_d, str, 10);
            strcat(result, str);
        }
        else
        {
            if (check_i == 3)
            {
                strcat(result, "sport ");
                printf("   1 - alpine skiing\n");
                printf("   2 - surfing \n");
                printf("   3 - ascent \n");
                printf("  Choise country MAIN TYPE: ");
                if (scanf("%lf", &check_d) != 1)
                    return INCORRECT_INPUT;
                check_i = check_d;
                if (check_i - check_d != 0)
                    return INCORRECT_INPUT;
                switch (check_i) {
                    case 1:
                        strcat(result, "alpine_skiing ");
                        break;
                    case 2:
                        strcat(result, "surfing ");
                        break;
                    case 3:
                        strcat(result, "ascent ");
                        break;
                    default:
                        return INCORRECT_INPUT;
                }
                printf("  Input country MIN COST: ");
                if (scanf("%lf", &check_d) != 1 || check_d < 0)
                    return INCORRECT_INPUT;
                itoa(check_d, str, 10);
                strcat(result, str);
            }
            else
                return INCORRECT_INPUT;
        }
    }
    fprintf(f, "\n%s", result);
    input_struct(result, &countries[(*n)], &key[(*n)]);
    key[*n].id = *n + 1;
    (*n)++;
    fclose(f);
    return SUCCESS;
}

void output_country(Country_t countries)
{
    printf("Country: %s \n", countries.name);
    printf("  population: %ld \n", countries.pop);
    printf("  capital: %s \n", countries.cap);
    printf("  mainland: %s \n", countries.cont);
    printf("  kind of tourism: %s \n", countries.tour);
    if (strcmp(countries.tour, "excurs") == 0)
    {
        printf("    number of objects: %d \n", countries.tours.excurs.cnt_plc);
        printf("    main type: %s \n", countries.tours.excurs.view);
    }
    else
    {
        if (strcmp(countries.tour, "beach") == 0)
        {
            printf("    month: %d \n", countries.tours.beach.month);
            printf("    air temperature: %f \n", countries.tours.beach.tmp_a);
            printf("    water temperature: %f \n", countries.tours.beach.tmp_w);
            printf("    time of flight: %f \n", countries.tours.beach.trvl_time);
        }
        else
            if (strcmp(countries.tour, "sport") == 0)
            {
                printf("    kind: %s \n", countries.tours.sport.kind);
                printf("    min_cost: %ld \n", countries.tours.sport.min_cost);
            }
    }
}

void output_key(key_t key)
{
    printf("  id: %d name: %s \n", key.id, key.name);
}

void output_table(key_t *key, int n)
{
    for (int i = 0; i < n; i++)
        output_key(key[i]);
}

void output_struct(Country_t *countries, int n)
{
    for(int i = 0; i < n; i++)
    {
        output_country(countries[i]);
        printf("\n");
    }
}

int reset_file(void)
{
    FILE *f = fopen("Country.txt", "w");
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
    fclose(f);
    return SUCCESS;
}

int record_file(Country_t countries)
{
    FILE *f = fopen("Country.txt", "a+");
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
    char result[256], str[31];
    memset(result, '\0', 256);
    strcat(result, countries.name);
    strcat(result, " ");
    itoa(countries.pop, str, 10);
    strcat(result, str);
    strcat(result, " ");
    strcat(result, countries.cap);
    strcat(result, " ");
    strcat(result, countries.cont);
    strcat(result, " ");
    strcat(result, countries.tour);
    strcat(result, " ");
    if (strcmp(countries.tour, "excurs") == 0)
    {
        itoa(countries.tours.excurs.cnt_plc, str, 10);
        strcat(result, str);
        strcat(result, " ");
        strcat(result, countries.tours.excurs.view);
    }
    if (strcmp(countries.tour, "beach") == 0)
    {
        itoa(countries.tours.beach.month, str, 10);
        strcat(result, str);
        strcat(result, " ");
        itoa(countries.tours.beach.tmp_w, str, 10);
        strcat(result, str);
        strcat(result, " ");
        itoa(countries.tours.beach.tmp_a, str, 10);
        strcat(result, str);
        strcat(result, " ");
        itoa(countries.tours.beach.trvl_time, str, 10);
        strcat(result, str);
    }
    if (strcmp(countries.tour, "sport") == 0)
        {
        strcat(result, countries.tours.sport.kind);
        strcat(result, " ");
        itoa(countries.tours.sport.min_cost, str, 10);
        strcat(result, str);
        }
    fprintf(f, "\n%s", result);
    fclose(f);
    return SUCCESS;
}

int delete(Country_t *countries, int *n)
{
    float check_f;
    int i, j, check_i;
    char str[31];
    puts(" Choose field:");
    puts("  1 - Country name");
    puts("  2 - Population");
    puts("  3 - Capital");
    puts("  4 - Mainland");
    puts("  5 - excurs");
    puts("  6 - beach");
    puts("  7 - sport");
    printf(" Choose field:");
    if (scanf("%f", &check_f) != 1)
        return INCORRECT_INPUT;
    i = check_f;
    if (i - check_f != 0)
        return INCORRECT_INPUT;
    switch (i) {
    case 1:
        printf(" input country name: ");
        if (scanf("%s", str) != 1)
            return INCORRECT_INPUT;
        if (reset_file())
            return FILE_ER;
        for (j = 0; j < *n; j++)
            if (strcmp(countries[j].name, str) != 0)
                record_file(countries[j]);
        break;
    case 2:
        printf(" input country population: ");
        if (scanf("%f", &check_f) != 1)
            return INCORRECT_INPUT;
        check_i = check_f;
        if (check_i - check_f != 0)
            return INCORRECT_INPUT;
        if (reset_file())
            return FILE_ER;
        for (j = 0; j < *n; j++)
            if (countries[j].pop != check_i)
                record_file(countries[j]);
        break;
    case 3:
        printf(" input country capital: ");
        if (scanf("%s", str) != 1)
            return INCORRECT_INPUT;
        if (reset_file())
            return FILE_ER;
        for (j = 0; j < *n; j++)
            if (strcmp(countries[j].cap, str) != 0)
                record_file(countries[j]);
        break;
    case 4:
        printf(" input country mainland: ");
        if (scanf("%s", str) != 1)
            return INCORRECT_INPUT;
        if (reset_file())
            return FILE_ER;
        for (j = 0; j < *n; j++)
            if (strcmp(countries[j].cont, str) != 0)
                record_file(countries[j]);
        break;
    case 5:
        puts("    1 - number of objects");
        puts("    2 - main type - natural");
        puts("    3 - main type - history");
        puts("    4 - main type - art");
        puts("    5 - excurs");
        printf(" input country type: ");
        if (scanf("%f", &check_f) != 1)
            return INCORRECT_INPUT;
        check_i = check_f;
        if (check_i - check_f != 0)
            return INCORRECT_INPUT;
        if (check_i == 1)
        {
            printf(" input number of objects: ");
            if (scanf("%f", &check_f) != 1)
                return INCORRECT_INPUT;
            check_i = check_f;
            if (check_i - check_f != 0)
                return INCORRECT_INPUT;
            if (reset_file())
                return FILE_ER;
            for (j = 0; j < *n; j++)
                if (countries[j].tours.excurs.cnt_plc != check_i)
                    record_file(countries[j]);
        }
        else
        {
            if (check_i == 2)
            {
                if (reset_file())
                    return FILE_ER;
                for (j = 0; j < *n; j++)
                    if (strcmp(countries[j].tours.excurs.view, "natural") != 0)
                        record_file(countries[j]);
            }
            else
            {
                if (check_i == 3)
                {
                    if (reset_file())
                        return FILE_ER;
                    for (j = 0; j < *n; j++)
                        if (strcmp(countries[j].tours.excurs.view, "history") != 0)
                            record_file(countries[j]);
                }
                else
                {
                    if (check_i == 4)
                    {
                        if (reset_file())
                            return FILE_ER;
                        for (j = 0; j < *n; j++)
                            if (strcmp(countries[j].tours.excurs.view, "art") != 0)
                                record_file(countries[j]);
                    }
                    else
                    {
                        if (check_i == 5)
                        {
                            if (reset_file())
                                return FILE_ER;
                            for (j = 0; j < *n; j++)
                                if (strcmp(countries[j].tour, "excurs") != 0)
                                    record_file(countries[j]);
                        }
                        else
                            return INCORRECT_INPUT;
                    }
                }
            }
        }
        break;
    case 6:
        puts("    1 - month number");
        puts("    2 - temperature water");
        puts("    3 - temperature air");
        puts("    4 - time of flight");
        puts("    5 - beach");
        printf(" input country type: ");
        if (scanf("%f", &check_f) != 1)
            return INCORRECT_INPUT;
        check_i = check_f;
        if (check_i - check_f != 0)
            return INCORRECT_INPUT;
        if (check_i == 1)
        {
            printf(" input month number: ");
            if (scanf("%f", &check_f) != 1)
                return INCORRECT_INPUT;
            check_i = check_f;
            if (check_i - check_f != 0 || check_i < 0 || check_i > 12)
                return INCORRECT_INPUT;
            if (reset_file())
                return FILE_ER;
            for (j = 0; j < *n; j++)
                if (countries[j].tours.beach.month != check_i)
                    record_file(countries[j]);
        }
        else
        {
            if (check_i == 2)
            {
                printf(" input temperature water: ");
                if (scanf("%f", &check_f) != 1)
                    return INCORRECT_INPUT;
                if (reset_file())
                    return FILE_ER;
                for (j = 0; j < *n; j++)
                    if (fabs(countries[j].tours.beach.tmp_w - check_f) > EPS)
                        record_file(countries[j]);
            }
            else
            {
                if (check_i == 3)
                {
                    printf(" input temperature air: ");
                    if (scanf("%f", &check_f) != 1)
                        return INCORRECT_INPUT;
                    if (reset_file())
                        return FILE_ER;
                    for (j = 0; j < *n; j++)
                        if (fabs(countries[j].tours.beach.tmp_a - check_f) > EPS)
                            record_file(countries[j]);
                }
                else
                {
                    if (check_i == 4)
                    {
                        printf(" input time of flight: ");
                        if (scanf("%f", &check_f) != 1)
                            return INCORRECT_INPUT;
                        if (reset_file())
                            return FILE_ER;
                        for (j = 0; j < *n; j++)
                            if (fabs(countries[j].tours.beach.trvl_time - check_f) > EPS)
                                record_file(countries[j]);
                    }
                    else
                    {
                        if (check_i == 5)
                        {
                            if (reset_file())
                                return FILE_ER;
                            for (j = 0; j < *n; j++)
                                if (strcmp(countries[j].tour, "beach") != 0)
                                    record_file(countries[j]);
                        }
                        else
                            return INCORRECT_INPUT;
                    }
                }
            }
        }
        break;
    case 7:
        puts("    1 - kind of sport - alpine_skiing");
        puts("    2 - kind of sport - surfing");
        puts("    3 - kind of sport - ascent");
        puts("    4 - min. cost");
        puts("    5 - sport");
        printf(" input country type: ");
        if (scanf("%f", &check_f) != 1)
            return INCORRECT_INPUT;
        check_i = check_f;
        if (check_i - check_f != 0)
            return INCORRECT_INPUT;
        if (check_i == 4)
        {
            printf(" input min. cost: ");
            if (scanf("%f", &check_f) != 1)
                return INCORRECT_INPUT;
            check_i = check_f;
            if (check_i - check_f != 0)
                return INCORRECT_INPUT;
            if (reset_file())
                return FILE_ER;
            for (j = 0; j < *n; j++)
                if (countries[j].tours.excurs.cnt_plc != check_i)
                    record_file(countries[j]);
        }
        else
        {
            if (check_i == 2)
            {
                if (reset_file())
                    return FILE_ER;
                for (j = 0; j < *n; j++)
                    if (strcmp(countries[j].tours.excurs.view, "surfing") != 0)
                        record_file(countries[j]);
            }
            else
            {
                if (check_i == 3)
                {
                    if (reset_file())
                        return FILE_ER;
                    for (j = 0; j < *n; j++)
                        if (strcmp(countries[j].tours.excurs.view, "ascent") != 0)
                            record_file(countries[j]);
                }
                else
                {
                    if (check_i == 1)
                    {
                        if (reset_file())
                            return FILE_ER;
                        for (j = 0; j < *n; j++)
                            if (strcmp(countries[j].tours.excurs.view, "alpine_skiing") != 0)
                                record_file(countries[j]);
                    }
                    else
                    {
                        if (check_i == 5)
                        {
                            if (reset_file())
                                return FILE_ER;
                            for (j = 0; j < *n; j++)
                                if (strcmp(countries[j].tour, "sport") != 0)
                                    record_file(countries[j]);
                        }
                        else
                            return INCORRECT_INPUT;
                    }
                }
            }
        }
        break;
    default:
        return INCORRECT_INPUT;
    }
    return SUCCESS;
}

int output_list_mainland_sport(Country_t *countries, int n)
{
    char ml[64];
    double check_d;
    int check_i;
    printf("Input mainland: ");
    if (scanf("%s", ml) != 1)
        return INCORRECT_INPUT;
    if (strlen(ml) > 31)
        return INCORRECT_INPUT;
    puts(" Choise kind of rest: ");
    printf("  1 - excurs\n");
    printf("  2 - beach \n");
    printf("  3 - sport \n");
    printf("   Choise kind of rest: ");
    if (scanf("%lf", &check_d) != 1)
        return INCORRECT_INPUT;
    check_i = check_d;
    if (check_i - check_d != 0)
        return INCORRECT_INPUT;
    for (int i = 0; i < n; i++)
        if (strcmp(countries[i].cont, ml) == 0)
        {
            if (strcmp(countries[i].tour, "excurs") == 0 && check_i == 1)
            {
                puts("");
                output_country(countries[i]);
            }
            if (strcmp(countries[i].tour, "beach") == 0 && check_i == 2)
            {
                puts("");
                output_country(countries[i]);
            }
            if (strcmp(countries[i].tour, "sport") == 0 && check_i == 3)
            {
                puts("");
                output_country(countries[i]);
            }
        }
    return SUCCESS;
}

int err(int err)
{
    switch (err) {
    case -1:
        puts("FAILED");
        break;
    case -2:
        puts("INCORRECT_INPUT");
        break;
    case -3:
        puts("INVALID_POINTER");
        break;
    case -4:
        puts("INCORRECT_OUTPUT");
        break;
    case -5:
        puts("FILE_ERROR");
        break;
    case -6:
        puts("OVERFLOW");
        break;
    }
    return err;
}

void sort_key_buble(key_t *key, int n)
{
    int f;
    key_t tmp;
    for (int j = 0; j < n - 1; j++)
    {
        f = 0;
        for (int i = 0; i < n - j - 1; i++)
            if (strcmp(key[i].name, key[i + 1].name) > 0)
            {
                tmp = key[i];
                key[i] = key[i + 1];
                key[i + 1] = tmp;
                f = 1;
            }
        if (f == 0)
            break;
    }
}

void sort_key_insert(key_t *key, int n)
{
    key_t f;
    int j;
    for (int i = 1; i < n; i++)
    {
        j = i - 1;
        f = key[i];
        while(strcmp(key[j].name, f.name) > 0 && j >= 0)
        {
            key[j + 1] = key[j];
            j -= 1;
        }
        key[j + 1] = f;
    }
}

void sort_struct_buble(Country_t *key, int n)
{
    int f;
    Country_t tmp;
    for (int j = 0; j < n - 1; j++)
    {
        f = 0;
        for (int i = 0; i < n - j - 1; i++)
            if (strcmp(key[i].name, key[i + 1].name) > 0)
            {
                tmp = key[i];
                key[i] = key[i + 1];
                key[i + 1] = tmp;
                f = 1;
            }
        if (f == 0)
            break;
    }
}

void sort_struct_insert(Country_t *key, int n)
{
    Country_t f;
    int j;
    for (int i = 1; i < n; i++)
    {
        j = i - 1;
        f = key[i];
        while(strcmp(key[j].name, f.name) > 0 && j >= 0)
        {
            key[j + 1] = key[j];
            j -= 1;
        }
        key[j + 1] = f;
    }
}

int main()
{
    Country_t countries[N];
    key_t key[N];
    clock_t start, end;
    double clock_k_b = -1, clock_k_i = -1;
    double clock_s_b = -1, clock_s_i = -1;
    int n, i, check_func;
    float check_f;
    check_func = read_file(countries, key, &n);
    if (check_func != SUCCESS)
        return err(check_func);
    while (1)
    {
        puts(" Available command:");
        puts("  1 - Output table");
        puts("  2 - Add record");
        puts("  3 - Delete record by value of field");
        puts("  4 - Output table of key");
        puts("  5 - Output country on SELECTED mainland and kind of rest");
        puts("  6 - Output sorted table");
        puts("  7 - Efficiency analysis");
        puts("  8 - Shuffle");
        puts("  9 - Sort table of keys");
        puts("  0 - Exit");
        printf(" Select next action:");
        if (scanf("%f", &check_f) != 1)
            return err(INCORRECT_INPUT);
        i = check_f;
        if (i - check_f != 0)
            return err(INCORRECT_INPUT);
        puts("-----------------------------------------------------");
        switch (i) {
        case 1:
            output_struct(countries, n);
            break;
        case 2:
            check_func = add_country(countries, key, &n);
            if (check_func != SUCCESS)
                return err(check_func);
            break;
        case 3:
            check_func = delete(countries, &n);
            if (check_func != SUCCESS)
                return err(check_func);
            check_func = read_file(countries, key, &n);
            if (check_func != SUCCESS)
                return err(check_func);
            break;
        case 4:
            output_table(key, n);
            break;
        case 5:
            output_list_mainland_sport(countries, n);
            break;
        case 6:
            sort_struct_insert(countries, n);
            reset_file();
            for (int j = 0; j < n; j++)
                record_file(countries[j]);
            check_func = read_file(countries, key, &n);
            if (check_func != SUCCESS)
                return err(check_func);
            output_struct(countries, n);
            break;
        case 7:
            puts("**Sort table. 1M iterations.");
            puts("  Buble sort.");
            start = clock();
            for (int j = 0; j < ITERATIONS; j++)
            {
                shuffle(countries, key, n);
                sort_struct_buble(countries, n);
            }
            end = clock();
            clock_s_b = ((double)(end - start) / CLOCKS_PER_SEC);
            printf("   Time on 1M iterations: %lf sec\n", clock_s_b);
            printf("   Average time: %.1lfE-7 sec\n", clock_s_b);
            puts("  Insert sort.");
            start = clock();
            for (int j = 0; j < ITERATIONS; j++)
            {
                shuffle(countries, key, n);
                sort_struct_insert(countries, n);
            }
            end = clock();
            clock_s_i = ((double)(end - start) / CLOCKS_PER_SEC);
            printf("   Time on 1M iterations: %lf sec\n", clock_s_i);
            printf("   Average time: %.1lfE-7 sec\n", clock_s_i);
            reset_file();
            for (int j = 0; j < n; j++)
                record_file(countries[j]);
            for (int j = 0; j < n; j++)
                key[j].id = j + 1;
            printf(" 1M sorting table with n = %d record:  %0.2lf %% \n", n, (fabs(clock_s_b - clock_s_i)) / fmax(clock_s_b,clock_s_i) * 100);
            puts("**Sort table WITH table of keys 10M iterations.");
            puts("  Buble sort.");
            start = clock();
            for (int j = 0; j < ITERATIONS; j++)
            {
                shuffle(countries, key, n);
                for (int j = 0; j < n; j++)
                    key[j].id = j + 1;
                sort_key_buble(key, n);
            }
            end = clock();
            clock_k_b = ((double)(end - start) / CLOCKS_PER_SEC);
            printf("   Time on 1M iterations: %lf sec\n", clock_k_b);
            printf("   Average time: %.1lfE-7 sec\n", clock_k_b);
            puts("  Insert sort.");
            start = clock();
            for (int j = 0; j < ITERATIONS; j++)
            {
                shuffle(countries, key, n);
                for (int j = 0; j < n; j++)
                    key[j].id = j + 1;
                sort_key_insert(key, n);
            }
            end = clock();
            clock_k_i = ((double)(end - start) / CLOCKS_PER_SEC);
            printf("   Time on 1M iterations: %lf sec\n", clock_k_i);
            printf("   Average time: %.1lfE-7 sec\n", clock_k_i);
            reset_file();
            for (int j = 0; j < n; j++)
                record_file(countries[key[j].id - 1]);
            check_func = read_file(countries, key, &n);
            if (check_func != SUCCESS)
                return err(check_func);
            printf(" 1M sorting table with n = %d record:  %0.2lf %% \n", n, (fabs(clock_k_b - clock_k_i)) / fmax(clock_k_b,clock_k_i) * 100);
            puts("**Memory**");
            printf("  Required space for one record (table Country): %I64d \n", sizeof(Country_t));
            printf("  Required space for one record (table key): %I64d \n", sizeof(key_t) + sizeof(Country_t));
            printf("  Space efficiency: %0.2lf %% \n", (double)(sizeof(key_t)) / (sizeof(Country_t) + sizeof(key_t)) *100   );
            break;
        case 8:
            shuffle(countries, key, n);
            reset_file();
            for (int j = 0; j < n; j++)
                record_file(countries[j]);
            for (int j = 0; j < n; j++)
                key[j].id = j + 1;
            puts("Table was shuffled");
            break;
        case 9:
            sort_key_buble(key, n);
            puts("Table of keys was sorted");
            break;
        case 0:
            return SUCCESS;
            break;
        default:
            return err(INCORRECT_INPUT);
        }
        puts("-----------------------------------------------------");
    }
    return SUCCESS;
}
