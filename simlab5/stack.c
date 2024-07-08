#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the maximum size of the stack
#define MAX_SIZE 5
#define CMD_LENGTH 16 

// Structure to represent the stack
struct Stack {
    int items[MAX_SIZE];
    int top;
};

// Function to initialize an empty stack
void initializeStack(struct Stack *stack) {
    stack->top = -1;
}

// Function to check if the stack is empty
int isEmpty(struct Stack *stack) {
    return stack->top == -1;
}

// Function to check if the stack is full
int isFull(struct Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

// Function to push an element onto the stack
void push(struct Stack *stack, int value) {
    stack->top++;
    stack->items[stack->top] = value;
}

// Function to pop an element from the stack
int pop(struct Stack *stack) {
    int poppedItem = stack->items[stack->top];
    stack->top--;
    return poppedItem;
}

// Function to get the top element of the stack without popping
int peek(struct Stack *stack) {
    return stack->items[stack->top];
}

int main() {
    struct Stack myStack;
    initializeStack(&myStack);

    // Commands: ISEMPTY, ISFULL, PUSH, POP, PEEK, EXIT
    printf("Commands: ISEMPTY, ISFULL, PUSH [value], POP, PEEK.\n");
    printf("Type in EXIT to terminate the program.\n");

    char command[CMD_LENGTH];
    
    // Ask the user to input the first command
    char *status = fgets(command, CMD_LENGTH, stdin);
    int value = 0;

    while (status != NULL) {
        if (strcmp(command, "ISEMPTY\n") == 0) {
            if (isEmpty(&myStack))
                printf("Stack is empty\n");
            else
                printf("Stack is not empty\n");
        } else if (strcmp(command, "ISFULL\n") == 0) {
            if (isFull(&myStack))
                printf("Stack is full\n");
            else
                printf("Stack is not full\n");
        } else if (strcmp(command, "PUSH\n") == 0) {
            status = fgets(command, CMD_LENGTH, stdin);
            if (status != NULL) {
                value = atoi(command);
                push(&myStack, value); // if the value was invalid pushes 0
                printf("Pushed element: %d\n", value);
            }
        } else if (strcmp(command, "POP\n") == 0) {
            printf("Popped element: %d\n", pop(&myStack));
        } else if (strcmp(command, "PEEK\n") == 0) {
            printf("Top element: %d\n", peek(&myStack));
        } else if (strcmp(command, "EXIT\n") == 0) {
            break;
        } else {
            printf("Invalid command\n");
        }

        // Ask the user to input the next command
        status = fgets(command, CMD_LENGTH, stdin);
    }

    return 0;
}
