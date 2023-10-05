#include <stdio.h>

int main(int argc, char** argv) {
  int* a = new int[10];
  if (a[5])
    printf("xx\n");
  return 0;
}