# C++ library

## Overview

SlideIO is a cross-platform C++ library. It runs on Windows 10 and 11, on
macOS 12 and above, and on Linux distributions with glibc 2.28 or newer; the
Debian packages target Debian 12+ and Ubuntu 22.04+. Every release is built
and tested on all three before it is published.

The prebuilt macOS archive is for Apple Silicon. Intel Macs are supported by
the library itself -- build it from source, or use the Python module, whose
wheels cover both architectures.

The library is reached through the global functions `slideio::openSlide()` and
`slideio::getDriverIDs()`, and provides two main classes: `slideio::Slide`, a
slide container, and `slideio::Scene`, a single raster image within it.

## Installation

### Installing a release package

Prebuilt packages for Windows, macOS and Linux are on the
[Downloads page](downloads.md). They are self-contained:
no Conan, no CMake toolchain file and no build of SlideIO is needed to use
one. A package carries the headers, the shared libraries, the CMake package
configuration, and the `slideio-converter` and `slideio-tiffinspector`
command line tools.

Whichever platform you are on, a program then finds the library with:

```cmake
find_package(slideio REQUIRED)
target_link_libraries(myapp PRIVATE slideio::slideio)
```

The package publishes the components `slideio`, `core`, `imagetools`,
`converter` and `transformer`; linking `slideio::slideio` is enough for most
uses.

#### Debian and Ubuntu

Download the two packages from the release page and install them together.
The leading `./` matters -- without it `apt` looks for a package of that name
in your configured repositories rather than installing the file:

```
sudo apt install ./libslideio<version>_<version>_amd64.deb \
                 ./libslideio-dev_<version>_amd64.deb
```

`libslideio<version>` is the runtime and `libslideio-dev` adds the headers and
the CMake configuration; install both to build against the library. The
version is part of the runtime package name so that two minor releases can be
installed side by side. The command line tools are a third package,
`slideio-tools`, installed the same way.

Everything lands under `/usr`, which CMake and the dynamic loader already
search, so nothing further is needed:

```
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
```

#### macOS

Unpack the archive. Its layout is flat -- `bin`, `lib` and `include` sit at
the root with no enclosing directory -- so the directory you unpack into is
the prefix:

```
mkdir -p ~/slideio && tar -xzf slideio-<version>-macos-arm64.tar.gz -C ~/slideio
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=~/slideio
```

No `DYLD_LIBRARY_PATH` is required: the imported CMake target carries an
absolute location, and your executable gets an RPATH into the unpacked tree.
The tools in `bin` find the dylibs in `lib` the same way.

The archive is built for Apple Silicon against a macOS 12 deployment target.
It is not signed by a registered developer, so macOS may quarantine the
download; `xattr -d com.apple.quarantine <file>` clears it.

#### Windows

Unpack the zip. The layout is flat here too, so the directory you unpack into
is the prefix:

```
cmake -S . -B build -DCMAKE_PREFIX_PATH=C:/slideio
cmake --build build --config Release
```

Windows has no RPATH, so the DLLs are found on `PATH` at run time. Add the
package's `bin` directory to it, or copy the DLLs beside your executable:

```
set PATH=C:\slideio\bin;%PATH%
```

The separate `-pdb.zip` holds the matching MSVC debug symbols, should you need
to step into the library.

### Building the library from the source

Build instructions live with the code, where they are kept current:
see [Build instructions](https://github.com/Booritas/slideio#build-instructions)
in the SlideIO README for the prerequisites, the dependencies, and the
commands for Linux, macOS and Windows.

## Next steps

- [C++ API](api.md): the classes and a first example.
- [Command line tools](../tools/index.md) shipped with every package.
- [Image drivers](../drivers.md) and what each format exposes.
