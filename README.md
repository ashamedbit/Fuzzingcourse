# Fuzzingcourse
This the Secure Coding module 4 content - Fuzzing, Profilers and Pen testing.

This contains the exercises, and examples used within the course. The docker setup contains all the exercises within exercise/ folder. The examples in this module are under fuzzing/ and runtime_checkers/ folders.

### Building docker image

First clone this repo, and enter the root directory of the project. Recursively fetch the submodules by running:
```bash
git clone https://github.com/ashamedbit/Fuzzingcourse
```

You can now build the environment required for the tool from using the Dockerfile included by running the following command:
```bash
docker build -t address . 
```

### Launching docker image with tool

The build command will both setup the environment and the 3 test repositories. To enter the container invoke:
```bash
docker run -it address
```
