#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, const char *argv[]) {
    char *s = malloc(13);
    strcpy(s, "Hello world!");
    printf("string is: %s\n", s);
    // forgot to deallocate memory
    return 0;
}