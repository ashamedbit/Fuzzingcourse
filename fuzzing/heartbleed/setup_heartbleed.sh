# Download and unpack a vulnerable version of OpenSSL:
curl -O https://ftp.openssl.org/source/old/1.0.1/openssl-1.0.1f.tar.gz
tar xf openssl-1.0.1f.tar.gz

# Build OpenSSL with ASan and fuzzer instrumentation:
cd openssl-1.0.1f/
./config

# $CC must be pointing to clang binary, see the "compiler section" link above.
make CC="clang -g -fsanitize=address,fuzzer"
cd ..