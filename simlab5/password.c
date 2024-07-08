#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

// function to check if a password is valid
int is_valid_password(const char *password) {
    if (strlen(password) < 8) {
        return FALSE; // ivalid
    }

    int has_upper = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (isupper(password[i])) {
            has_upper = 1;
            break;
        }
    }

    int has_lower = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (islower(password[i])) {
            has_lower = 1;
            break;
        }
    }

    int has_digit = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (isdigit(password[i])) {
            has_digit = 1;
            break;
        }
    }

    int has_special = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (!isalnum(password[i])) {
            has_special = 1;
            break;
        }
    }

    if (has_upper && has_lower && has_digit && has_special) {
        return TRUE; // valid
    } else {
        return FALSE; // invalid
    }
}
