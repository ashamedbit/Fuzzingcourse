#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 100

void initialize(int *a) {
    for (int i = 0; i < ARRAY_SIZE; i++) {
        a[i] = i;
    }
}

int main(int argc, char *argv[]) {

    // Ensure that the user supplied exactly one command line argument
    if (argc != 2) {
        fprintf(stderr, "Please provide at least one command line argument\n");
        return -1;
    }

    int *a = malloc(ARRAY_SIZE * sizeof(int));
    initialize(a);
    int index = atoi(argv[1]);
    free(a);
    printf("a[%d]=%d\n", index, a[index]); // if atoi fails to convert argv[1] to int, it returns the smallest valid index 0 
} 