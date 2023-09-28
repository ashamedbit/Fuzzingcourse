# Continuous Fuzzing for C/C++ Example (Heartbleed example)

This is an example of how to integrate your [libfuzzer](https://llvm.org/docs/LibFuzzer.html) targets into GitLab CI/CD.

This tutorial will show how to find the "fameous" [heartbleed](https://en.wikipedia.org/wiki/Heartbleed) security bug with libfuzzer and GitLab CI/CD.

This example will show the following steps:
* [Building and running a simple libFuzzer target locally](#building-libfuzzer-target)
* [Running the libFuzzer target via GitLab CI/CD](#integrating-with-fuzzit-from-ci)

Result:
* The libFuzzer targets will run continuously on the master branch .
* The libFuzzer targets will run regression tests on every pull-request (and every other branch)
 with the generated corpus and crashes to catch bugs early on.

Fuzzing for C/C++ can help find both various complex and critical security. C/C++ are both memory unsafe languages were 
memory corruption bugs can lead to serious security vulnerabilities. Heartbleed bugs affected almost any well known web service and was explitable
for almost two years before discovery and patching. 

This tutorial focuses less on how to build libFuzzer targets and more on how to integrate the targets with GitLab. A lot of 
great information is available at the [libFuzzer](https://llvm.org/docs/LibFuzzer.html) tutorial.

## Building libFuzzer Target

### Prerequisite

This tutorial tested on Ubuntu 18, though it should work on any Unix environment.

The required packages are cmake and clang > 6.0

```bash
apt update && apt install -y git clang cmake 
```

### Getting the code

```bash
git clone https://gitlab.com/gitlab-org/security-products/demos/coverage-fuzzing/heartbleed-fuzzing-example
```

### Compiling

```bash
# you might need to export CXX=<path_to_clang++> CC=<path_to_clang>
cd heartbleed-example
ln -s /usr/bin/llvm-symbolizer-6.0 /usr/bin/llvm-symbolizer
export CC=`which clang`
export CXX=`which clang++`
export ASAN_SYMBOLIER_PATH=`which llvm-symbolizer`
cd openssl-1.0.1f && ./config && make CC="$CC -g -fsanitize=address,fuzzer-no-link" && cd ..
$CXX -g handshake-fuzzer.cc -fsanitize=address,fuzzer openssl-1.0.1f/libssl.a openssl-1.0.1f/libcrypto.a -std=c++17 -Iopenssl-1.0.1f/include/ -lstdc++fs  -ldl -lstdc++ -o handshake-fuzzer
```

### Understanding the bug
The fuzzer code exists in `handhsare-fuzzer.cc`. You can see it's a pretty short code and will discover the heartbleed vulnerability in a few seconds.

It might look a bit unclear for developers that are not familiar with openssl but usually the developers themself write fuzz tests just like
they are responsible for writing unit-tests.

For developer who is familiar with openssl code-base this should be pretty stndard and look very similar to a standard unit-test but instead of 
creating the testcase using the testcases that are created by libfuzzer and passed to `const unit8_t *Data`.

## Fuzzing
```bash
./handshake-fuzzer
```
 The output should look something like this:
 ```text
#150255 REDUCE cov: 485 ft: 756 corp: 38/15713b exec/s: 25042 rss: 402Mb L: 2891/2891 MS: 1 EraseBytes-
=================================================================
==6098==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x629000009748 at pc 0x0000005133a2 bp 0x7fffe29233c0 sp 0x7fffe2922b70
READ of size 48830 at 0x629000009748 thread T0
    #0 0x5133a1 in __asan_memcpy (/app/handshake-fuzzer+0x5133a1)
    #1 0x5630c8 in tls1_process_heartbeat /app/openssl-1.0.1f/ssl/t1_lib.c:2586:3
    #2 0x5cfa9d in ssl3_read_bytes /app/openssl-1.0.1f/ssl/s3_pkt.c:1092:4
    #3 0x5d42da in ssl3_get_message /app/openssl-1.0.1f/ssl/s3_both.c:457:7
    #4 0x59f537 in ssl3_get_client_hello /app/openssl-1.0.1f/ssl/s3_srvr.c:941:4
    #5 0x59b5a9 in ssl3_accept /app/openssl-1.0.1f/ssl/s3_srvr.c:357:9
    #6 0x551335 in LLVMFuzzerTestOneInput /app/handshake-fuzzer.cc:66:3
    #7 0x430df7 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/app/handshake-fuzzer+0x430df7)
    #8 0x43b664 in fuzzer::Fuzzer::MutateAndTestOne() (/app/handshake-fuzzer+0x43b664)
    #9 0x43cccf in fuzzer::Fuzzer::Loop(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, fuzzer::fuzzer_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) (/app/handshake-fuzzer+0x43cccf)
    #10 0x42c08c in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/app/handshake-fuzzer+0x42c08c)
    #11 0x41ee72 in main (/app/handshake-fuzzer+0x41ee72)
    #12 0x7f638efe8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #13 0x41efc9 in _start (/app/handshake-fuzzer+0x41efc9)

0x629000009748 is located 0 bytes to the right of 17736-byte region [0x629000005200,0x629000009748)
allocated by thread T0 here:
    #0 0x5144e0 in __interceptor_malloc (/app/handshake-fuzzer+0x5144e0)
    #1 0x60437b in CRYPTO_malloc /app/openssl-1.0.1f/crypto/mem.c:308:8
    #2 0x5d5809 in freelist_extract /app/openssl-1.0.1f/ssl/s3_both.c:708:12
    #3 0x5d5809 in ssl3_setup_read_buffer /app/openssl-1.0.1f/ssl/s3_both.c:770
    #4 0x5d5dec in ssl3_setup_buffers /app/openssl-1.0.1f/ssl/s3_both.c:827:7
    #5 0x59c174 in ssl3_accept /app/openssl-1.0.1f/ssl/s3_srvr.c:292:9
    #6 0x551335 in LLVMFuzzerTestOneInput /app/handshake-fuzzer.cc:66:3
    #7 0x430df7 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/app/handshake-fuzzer+0x430df7)
    #8 0x43aa3b in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, fuzzer::fuzzer_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) (/app/handshake-fuzzer+0x43aa3b)
    #9 0x43cba2 in fuzzer::Fuzzer::Loop(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, fuzzer::fuzzer_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) (/app/handshake-fuzzer+0x43cba2)
    #10 0x42c08c in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/app/handshake-fuzzer+0x42c08c)
    #11 0x41ee72 in main (/app/handshake-fuzzer+0x41ee72)
    #12 0x7f638efe8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow (/app/handshake-fuzzer+0x5133a1) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c527fff9290: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff92a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff92b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff92c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff92d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c527fff92e0: 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa fa fa
  0x0c527fff92f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff9300: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff9310: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff9320: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff9330: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==6098==ABORTING
MS: 1 CopyPart-; base unit: bf5161803df66fc3a5bc1e300e58188d45dc1366
0x0,0x3,0x0,0x0,0x0,0x18,0x3,0x0,0x0,0x1,0x1,
\x00\x03\x00\x00\x00\x18\x03\x00\x00\x01\x01
artifact_prefix='./'; Test unit written to ./crash-c86f3ae03bc52ace3a009278ef73d9d5ed61a4d7
Base64: AAMAAAAYAwAAAQE=
 ```

 
We can see clearly the heap-buffer-overflow READ bug at `tls1_process_heartbeat /app/openssl-1.0.1f/ssl/t1_lib.c:2586:3` (This is why it called heartbleed:)). And even for complex libraries we can see that libfuzzer find this serious vulnerability in a few seconds.

 ## Running libFuzzer from  CI
 
The best way to integrate go-fuzz fuzzing with Gitlab CI/CD is by adding additional stage & step to your `.gitlab-ci.yml`.

