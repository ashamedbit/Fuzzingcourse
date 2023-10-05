#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int foo(const char* str, int size) {
  if (size < 4) return 0;
  char buf[4];
  memcpy(buf, str, 4);
  if (buf[0] == 'F' && buf[1] == 'U' && buf[2] == 'Z' && buf[3] == 'Z') {
    buf[5] = '!';      // Overflow!!!
    return 1;
  }
  return 0;
}

int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    foo((char *)(data), size);
    return 0;
}