#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CORRECT_ENDING 0
#define INCORRECT_INPUT -1

typedef char str_t[60];
typedef int array_t[60];


// Проверка строки на наличие нескольких букв E или '.'/','
// на сторонние символы и лишнии пробелы
// а так же удаление пробелов
int check_str(str_t str)
{
    int i = 0, cp = 0, pe = -1, ce = 0, fp = 0, f = 0, len = strlen(str);
    while(str[i] != '\0')
    {
        if(str[i] == ' ')
        {
            fp = 1;
            int j = i--;
            --len;
            while (++j != len + 1)
                str[j - 1] = str[j];
            str[len] = '\0';
            if(f == 0)
                fp = 0;
            i += 1;
        }
        else
        {
            if((str[i] >= '0' && str[i] <= '9') || str[i] == '.' || str[i] == ',')
            {
                f = 1;
                if(fp == 1)
                    return INCORRECT_INPUT;
            }
            if((str[i] == '-' || str[i] == '+') && i != 0 && i != pe + 1)
                return INCORRECT_INPUT;
            if(str[i] == 'E' && f == 0)
                return INCORRECT_INPUT;
            if(str[i] == '.' || str[i] == ',')
                cp += 1;
            else
            {
                if(str[i] == 'E')
                {
                    f = 0;
                    fp = 0;
                }
                if(str[i] == 'E' && ce == 0)
                {
                    pe = i;
                    ce += 1;
                }
                else
                    if(str[i] == 'E')
                        return INCORRECT_INPUT;
                if(str[i] != '-' && str[i] != '+' && (str[i] < '0' || str[i] > '9') && str[i] != 'E')
                    return INCORRECT_INPUT;
            }
            i += 1;
        }
    }
    if(cp > 1 || ce > 1)
        return INCORRECT_INPUT;
    return CORRECT_ENDING;
}


// Разбиение строки на мантису и порядок, а так же удаление "."
void format_in(str_t in, str_t str, long int *o1)
{
    if(strchr(in, 'E'))
    {
        char *pstr = strchr(in, 'E');
        pstr++;
        *o1 = atol(pstr);
    }
    else
        *o1 = 0;
    int i = 0;
    while(in[++i] != 'E' && i < 32);
    i = i <= 32 ? i - 1: i;
    strncpy(str, in, i + 1);
    i = 0;
    while(str[i] != ',' && str[i] != '\0')
        i += 1;
    if(str[i] != '\0')
        str[i] = '.';
    if(strchr(str, '.'))
    {
        char *ostr = strchr(str, '.');
        int len = strlen(ostr);
        i = 0;
        int j = i--;
        --len;
        while (++j != len + 1)
            ostr[j - 1] = ostr[j];
        ostr[len] = '\0';
        i = 0;
        while(ostr[++i] != '\0');
        i -= 1;
        *o1 -= i;
    }
    int len = strlen(str);
    i = 0;
    while(str[i] == '0')
    {
        int j = i--;
        --len;
        while (++j != len + 1)
            str[j - 1] = str[j];
    }
    str[len] = '\0';
    //printf("%s", str);
}


// Проверка втрого числа на стронние символы, лишнии пробелы
int check_str2(str_t str)
{
    int i = 0, cp = 0, f = 0, fp = 0, len = strlen(str);
    while(str[i] != '\0')
    {
        if(str[i] == ' ')
        {
            fp = 1;
            int j = i--;
            --len;
            while (++j != len + 1)
                str[j - 1] = str[j];
            str[len] = '\0';
            if(f == 0)
                fp = 0;
            i += 1;
        }
        else
        {
            if(str[i] > '0' && str[i] < '9')
            {
                f = 1;
                if(fp == 1)
                    return INCORRECT_INPUT;
            }
            if((str[i] == '-' || str[i] == '+') && i >= 1 )
                return INCORRECT_INPUT;
            if(str[i] == '.' || str[i] == ',')
                cp += 1;
            else
                if(str[i] != '-' && str[i] != '+' && (str[i] < '0' || str[i] > '9'))
                    return INCORRECT_INPUT;
            i += 1;
        }
    }
    if(cp > 0)
        return INCORRECT_INPUT;
    return CORRECT_ENDING;
}


// Функция умножения числа с мантисой m и порядком o на число in,
// считает знак произведения, удаляет незначащие нули
// а так же выводит результат в указанном формате
int main_math(str_t m, long int o, str_t in)
{
    array_t out;
    //printf("\n m = %s\n", m);
    int sign = 0, rem, len1 = strlen(m) - 1, len2 = strlen(in) - 1, a, b, e = 60, count = 0, j;
    sign = m[0] == '-' ? -1: 1;

    if(m[0] == '-' || m[0] == '+')
    {
        m++;
        len1 -= 1;
    }
    if(in[0] == '-' || in[0] == '+')
    {
        if(in[0] == '-')
            sign *= -1;
        in++;
        len2 -= 1;
    }
    //printf("\n len = %d %d\n", len1, len2);
    for(int i = 0; i < 60; i++)
        out[i] = 0;
    for(int i = len1; i >= 0; i--)
    {
        rem = 0;
        a = m[i] - '0';
        for(int j = len2; j >= 0; j--)
        {
            b = in[j] - '0';
            out[i + j + 1] += rem + a * b;
            rem = out[i + j + 1] / 10;
            out[i + j + 1] %= 10;
            count += 1;
        }
        out[i] += rem;
    }
    printf("\n Array:\n");
    for(int i = 0; i < 60; i++)
        printf("%d ", out[i]);
    int i = 0;
    while(out[i] == 0 && i < 60)
        i += 1;
    i = 61 < i ? 0:i;
    while(out[--e] == 0 && e > 0);
    if(e <= 0)
        printf(" Result: 0");
    else
    {
        //printf("e = %d i = %d c = %d o = %ld \n", e, i, count, o);
        if((e - i) >= 30)
        {
            printf("out = %d", out[30]);
            if(out[30] > 4)
            {
                j = 29;
                while(1)
                {
                    if(out[j] == 9)
                        out[j] = 0;
                    else
                    {
                        out[j] += 1;
                        break;
                    }
                    j -= 1;
                }
            }
            e = j;

        }
        //printf("\n Array:\n");
        //for(int i = 0; i < 60; i++)
            //printf("%d ", out[i]);
        o = o - i + len1 + len2 + 2;
        if(o > 99999 || o < -99999)
            return INCORRECT_INPUT;
        //printf("e = %d i = %d c = %d o = %ld \n", e, i, count, o);
        printf("          |    5    |    5    |    5    | \n");
        while(out[e] == 0 && e > 0)
            e -= 1;
        printf("e = %d i = %d c = %d o = %ld \n", e, i, count, o);
        if(sign == -1)
            printf(" Result: -0.");
        else
            printf(" Result: 0.");
        for(int j = i; j < e + 1; j++)
            printf("%d", out[j]);
        if(e == 0)
        {
            o += 1;
            //printf("%d", out[0]);
        }
        if(e == -1)
        {
            o += 1;
            printf("1");
        }
        printf(" E %ld", o);
    }
    return CORRECT_ENDING;
}


int main()
{
    str_t in, m;
    long int o;
    printf("Input real number in format: +-_._ E+-_ \n");
    printf("Use right SLASH with sign. Left - without sign. \n");
    printf("|sign here 30 characters here||  \n");
    gets(in);
    if(check_str(in) != 0)
    {
        printf("incorrect input");
        return INCORRECT_INPUT;
    }
    format_in(in, m, &o);
    if(strlen(m) > 30)
    {
        printf("incorrect input");
        return INCORRECT_INPUT;
    }
    printf("Input integer number: \n");
    printf("|sign here 30 characters here||  \n");
    gets(in);
    if(check_str2(in) != 0 || strlen(in) > 31)
    {
        printf("incorrect input");
        return INCORRECT_INPUT;
    }
    //printf(" %sE%ld x %s ", m, o, in);
    if(main_math(m, o, in))
    {
        printf("incorrect input");
        return INCORRECT_INPUT;
    }
    return CORRECT_ENDING;
}
