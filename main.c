#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    printf("\nEnter your password please:");
    scanf("%d",&x);

    int b=10000;


    if(x>b)
    {
         printf("\nYour password can not be %d",x);
         int i=0;
         for(i;i<=5;i++)
         {
             printf("\nInvalid password!\n");
         }

    }
    else
    {
        printf("\nYour password is valid.\n");
        printf("\nYour password is %d\n",x);

        int a=0;
        for(a;a<=5;a++)
        {
            printf("\nSuccessful entry.\n");
        }
    }




}
