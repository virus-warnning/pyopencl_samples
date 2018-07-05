# PyOpenCL Samples

## Overview

 N | Description | Detail
---- | ---- | ----
1 | List OpenCL devices. | [View](docs/01_devices.md)
2 | Print "Hello World!" in CL language. | [View](docs/02_hello.md)
3 | Examine whether the device support double precision. | [View](docs/03_double.md)
4 | Work group. | [View](docs/04_group.md)
5 | Synchronize work items in a work group. | [View](docs/05_barrier.md)
6 | Do a merge sort and print it's progress. |
7 | Compare merge sort by CPU, merge sort by GPU and Python built-in sorted(). |
8 | Convert a PNG to gray level. |

## Requirements

### Windows

* Make sure CPU or GPU driver installed.
* Download [Python 3.7 x86-64 executable installer](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe).
* Download **pyopencl‑2018.1.1+cl12‑cp37‑cp37m‑win_amd64.whl** from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl).
* Run Python 3.7 Installer.
* Check **Add Python 3.7 to PATH**.
* Install Python 3.7.
* python -m pip install numpy pillow
* python -m pip install **pyopencl‑2018.1.1+cl12‑cp37‑cp37m‑win_amd64.whl**

If your CPU is Intel Core 6th gen or newer, use **pyopencl‑2018.1.1+cl21‑cp37‑cp37m‑win_amd64.whl** instead.

### macOS

* brew install python3
* pip3 install pyopencl pillow

## Tested Environments

OS | OpenCL | Device
---- | ---- | ----
Windows 10 | 2.1 | Intel Core i5 7200U + HD Graphics 620
Windows 10 | 1.2 | Intel Core i5 3470 + HD Graphics 2500
macOS 10.13.3 | 1.2 | Intel Core i7 3667U + HD Graphics 4000

If you'd like to share test result on device not listed here, just edit *.md files and give me a PR.

# References

* [List of Intel graphics processing units - Seventh generation](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Seventh_generation)
* [List of AMD graphics processing units - API Overview](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units#API_Overview)
* [List of NVIDIA graphics processing units - GeForce 10 Series](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units#GeForce_10_series)
* [Mac computers that use OpenCL and OpenGL graphics](https://support.apple.com/en-us/HT202823)
* [OpenCL™ Drivers and Runtimes for Intel® Architecture](https://software.intel.com/en-us/articles/opencl-drivers)
* [AMD OpenCL™ 2.0 Driver](https://support.amd.com/en-us/kb-articles/Pages/OpenCL2-Driver.aspx)
* [Apple Deprecates Support for OpenGL & OpenCL Libraries at Mojave Announcement](https://appuals.com/apple-deprecates-support-for-opengl-opencl-libraries-at-mojave-announcement/)
