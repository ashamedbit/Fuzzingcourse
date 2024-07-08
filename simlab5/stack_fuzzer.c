#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// prints a valid sequence of at most max_number_of_commands
// into standard output stream
void stack_fuzzer(int max_number_of_commands) {
    return;
}

int main() {
    // use current time as a seed for the pseudorandom
    // number generator
    srand(time(NULL));
    stack_fuzzer(10);
}
