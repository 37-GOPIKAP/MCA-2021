/*queue using array*/
#include <stdio.h>
#include<stdlib.h>
int SIZE = 10;

void insert(int a[], int *front, int *rear)
{
    if(*rear > SIZE - 2)
    {
        printf("\n Queue is full\n");
        return;
    }
    else
    {
    int e;
    printf("\n Enter a value\n");
    scanf("%d",&e);
    if(*front == -1 && *rear == -1)
        *front = *rear = 0;
    else
        *rear += 1;
    a[*rear] = e;
    printf("\n Entered element %d is inserted\n", e);
    }
}
void delete(int a[], int *front, int *rear)
{
    int e;
    if(*front < 0)
    {
        printf("\n Queue is empty\n");
    }
     else
    {
    e = a[*front];
    printf("\n Element %d is deleted\n",e);
    *front += 1;
    }
}
void display(int a[], int *front, int *rear)
{
    int i;
    if(*front < 0)
    {
        printf("\n queue is empty\n");
        return;
    }
    else
    {
         printf("\n The queue elements are:\n");
    for(i = *front;i <= *rear;i++)
        printf("%d ",a[i]);
    }
}
int main()
{
    int arr[SIZE];
    int front, rear;
    int ch, e=1;
    front = rear = -1;

    while(e)
    {
    	printf("\n QUEUE USING ARRAY");
	    printf("\n...........MENU...........");
	    printf("\n 1.INSERT \n 2.DELETE \n 3.DISPLAY \n 4.EXIT");
	    printf("\n..........................");
	    printf("\n Enter your choice");
	    scanf("%d",&ch);
	    switch(ch)
	    {
		    case 1:
			    insert(arr, &front, &rear);
			    break;
		    case 2:
			    delete(arr, &front, &rear);
			    break;
		    case 3:
			    display(arr, &front, &rear);
			    break;
		    case 4:
			    e=0;
			      printf("\n exiting...");
			    break;
		    default: printf("\n please enter valid choice");
	    }
    }
    
    return 0;
}


