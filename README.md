# PyOpenCL Samples

## Overview

 N | Description
---- | ----
1 | List OpenCL devices.
2 | Print "Hello World!" in CL language.
3 | Examine whether the device support double precision.
4 | Work group.
5 | Synchronize work items in a work group.
6 | Do a merge sort and print it's progress.
7 | Compare merge sort by GPU, by GPU and Python built-in sorted().
8 | Convert a PNG to gray level.

## Requirements

### Windows

* Download [Python 3.7 x86-64 executable installer](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe).
* Download [pyopencl‑2018.1.1+cl12‑cp37‑cp37m‑win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl).
* Install Python 3.7 x86-64.
* python -m pip install numpy pillow
* python -m pip install pyopencl‑2018.1.1+cl12‑cp37‑cp37m‑win_amd64.whl

If your CPU is Intel Core 6th gen or newer, use pyopencl‑2018.1.1+cl21‑cp37‑cp37m‑win_amd64.whl instead.

### macOS

* brew install python3
* pip3 install pyopencl pillow

## Tested Environments

OS | OpenCL | Device
---- | ---- | ----
Windows 10 | 1.2 | Core i5 3470
Windows 10 | 1.2 | HD Graphics 2500
macOS 10.13.3 | 1.2 | Core i7 3667U
macOS 10.13.3 | 1.2 | HD Graphics 4000

# References

* [Mac computers that use OpenCL and OpenGL graphics](https://support.apple.com/en-us/HT202823).
* [OpenCL™ Drivers and Runtimes for Intel® Architecture](https://software.intel.com/en-us/articles/opencl-drivers)
