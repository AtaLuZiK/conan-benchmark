# conan-benchmark

Conan package for [benchmark](https://github.com/google/benchmark)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/benchmark%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/benchmark%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-benchmark.svg?branch=release%2F1.4.1)](https://travis-ci.org/AtaLuZiK/conan-benchmark)|[![Build status](https://ci.appveyor.com/api/projects/status/2ug5ff66jjfq5fgf/branch/release/1.4.1?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-benchmark/branch/release/1.4.1)|

## Reuse the packages

### Basic setup

```
conan install benchmark/1.4.1@zimmerk/stable
```

### Project setup

```
[requires]
benchmark/1.4.1@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
