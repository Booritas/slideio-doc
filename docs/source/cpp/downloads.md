# Downloads

Prebuilt packages of the C++ library carry the headers, the shared libraries,
the CMake package configuration, and the
[command line tools](../tools/index.md). The link points at the current
release, so it stays correct as new versions appear.

[Download the SlideIO library](https://github.com/Booritas/slideio/releases/latest)

| Platform | Package |
|---|---|
| Windows x86-64 | `.zip` with headers, import libraries and DLLs, built with MSVC 2022. A matching `-pdb.zip` carries the debug symbols. |
| macOS (Apple Silicon) | `.tar.gz` with headers and dylibs, built against a macOS 12 deployment target. |
| Linux x86-64 | `.tar.gz` built in a `manylinux_2_28` image, so it runs anywhere with glibc 2.28 or newer. |
| Debian 12+ / Ubuntu 22.04+ | Three packages: `libslideio<version>` (the runtime, named so that two minor releases can be installed side by side), `libslideio-dev` (headers and the CMake package config), and `slideio-tools` (the two command line tools). Install the first two for development. |

How to install each package is described under
[Installation](index.md#installation).

## Source code

The library is developed in
[github.com/Booritas/slideio](https://github.com/Booritas/slideio). To build it
yourself, see
[Building the library from the source](index.md#building-the-library-from-the-source).
