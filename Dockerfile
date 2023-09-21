FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# note that we need to install a newer version of cmake through a pass
RUN apt-get update --fix-missing
RUN apt-get install -y --no-install-recommends llvm-11* clang-11* gdb git curl zsh tmux wget libxml2 libarchive13 autoconf vim

RUN cp /usr/bin/llvm-profdata-11 /usr/bin/llvm-profdata && cp /usr/bin/llvm-cov-11 /usr/bin/llvm-cov && cp /usr/bin/clang-11 /usr/bin/clang

# GIT STUFF
RUN git config --global core.fileMode false && \
    git config --global diff.ignoreSubmodules dirty && \
    git config --global core.autocrlf input && \
    git config --global --add oh-my-zsh.hide-status 1 && \
    git config --global --add oh-my-zsh.hide-dirty 1
