#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main(){
    int n;
    printf("Enter no. of testcases: ");
    scanf("%d", &n);
    // printf("Testcases: %d\n", n);

    while(n > 0){

        char s[8];
        printf("Enter the string: ");

        scanf("%s", s);
        int len = strlen(s);

        int i = 0;

        while (i < len && s[i] == 'a') {
            i++;
        }

        if (i < len - 1 && s[i] == 'b' && s[i + 1] == 'b' && i + 2 == len) {
            printf("String Accepted!!!\n");
        } else {
            printf("String rejected!!!\n");
        }

        n--;
    }
}