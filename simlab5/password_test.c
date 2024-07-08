#include <assert.h>
#include "password.h"

#define TRUE 1
#define FALSE 0

int main() {
    // this test checks if short passwords are not accepted
    assert(is_valid_password("s3cURe?") == FALSE);
    // add more assertion-based tests here
}
