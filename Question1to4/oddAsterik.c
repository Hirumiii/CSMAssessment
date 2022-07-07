#include <stdio.h>
int main()
{
    int i, n,k;
    n=5;
    printf("All odd numbers from 1 to %d are: \n", n);
for(i=1; i<=n; i+=2)
    {
        for (k=1; k<=i ;k++){
        printf("*");
    }
        printf("\n");
    }
    return 0;
}