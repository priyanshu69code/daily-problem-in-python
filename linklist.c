#include <stdio.h>
#include <stdlib.h>

struct nodelist
{
    int data;
    struct nodelist *next;
};

struct nodelist *head;

void insertatpos(int data, int poss)
{
    int i = 0;
    struct nodelist *temp, *trv = head;
    temp = (struct nodelist *)(malloc(sizeof(struct nodelist)));
    temp->data = data;
    while (i == poss)
    {
        trv = trv->next;
        i++;
    }
    temp->next = trv->next;
    trv->next = temp;
    printf("Insert Success full\n");
}

void delete(int data)
{
    struct nodelist *temp = head;
    head = head->next;
    free(temp);
    printf("Delete succesfull\n");
}

void display()
{
    struct nodelist *trv = head;
    while (trv != NULL)
    {
        printf("%d --->", trv->data);
        trv = trv->next;
    }
    printf("NULL\n");
}

void linearSearch(int array[], int size, int data)
{
    int i = 0;
    while (i <= size)
    {
        if (array[i] == data)
        {
            printf("The data %d is at index %d", array[i], i);
            return;
        }
        else
        {
            printf("The data is Not in the array");
        }
    }
}

int main()
{
    struct nodelist *node2, *node3, node4;
    head = (struct nodelist *)(malloc(sizeof(struct nodelist)));
    head->data = 10;
    head->next = NULL;
    node2 = (struct nodelist *)(malloc(sizeof(struct nodelist)));
    node2->data = 20;
    node2->next = NULL;
    head->next = node2;
    insertatpos(30, 1);
    display();
    return 0;
}