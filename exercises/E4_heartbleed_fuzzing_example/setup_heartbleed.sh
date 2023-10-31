# you might need to export CXX=<path_to_clang++> CC=<path_to_clang>
ln -s /usr/bin/llvm-symbolizer-6.0 /usr/bin/llvm-symbolizer
export CC=`which clang`
export CXX=`which clang++`
export ASAN_SYMBOLIER_PATH=`which llvm-symbolizer`
cd openssl-1.0.1f && ./config && make CC="$CC -g -fsanitize=address,fuzzer-no-link" && cd ..
clang -g handshake-fuzzer.cc -fsanitize=address,fuzzer openssl-1.0.1f/libssl.a openssl-1.0.1f/libcrypto.a -std=c++17 -Iopenssl-1.0.1f/include/ -lstdc++fs  -ldl -lstdc++ -o handshake-fuzzer
