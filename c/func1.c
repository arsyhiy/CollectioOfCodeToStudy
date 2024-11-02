#include <stdio.h>

int power(int m, int n );

/* тестирование power - функции возведения в степень */
main()
{
    int i;

    for (i = 0; i < 10; ++i)
        printf("&d &d &d\n", i, power(2,i), power(-3,i));
    return 0;
}

/* power: возводит base в n-ю степень; n >= 0 */
int power(int base, int n)
{
    int i, p;

    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}

