#include <stdio.h>

int main() {
    
    int i,k;
    int num;
    printf("Enter an integer: ");
    printf("\n");
    scanf("%d", &num);
    if(num % 2 == 0)
        printf("%d is even.", num);
    else
    for(k=1; k<=i ; k++){        
        for(i=1;i<=num-1;i++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}