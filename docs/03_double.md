[Home](../../../#overview)

# About 03_double.py

## Known Issue

### Intel HD Graphics 3rd gen doesn't have cl_khr_fp64 extension.

Intel HD Graphics 3rd ~ 5h gen doesn't have cl_khr_fp64 extension, so type **double** isn't available.

(driver 10.18.10.4885 2017-12-11)

Intel HD Graphics 7th gen has this extension, however 6th was not tested.

## Output

### Win10 / Intel Core i5 7200U + HD Graphics 620

```
Increase each items in array: [1. 2. 3.]
 ... Python\Python37\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
Results of CPU: [2. 3. 4.]
Results of GPU: [2. 3. 4.]
```

### Win10 / Intel Core i5 3470 + HD Graphics 2500

```
... Python\Python36\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
Results of CPU: [2. 3. 4.]
Cannot use double.
Results of GPU: [0. 0. 0.]
```

### macOS 10.13.3 / Intel Core i7-3667U + HD Graphics 4000

```
Increase each items in array: [1. 2. 3.]
Results of CPU: [2. 3. 4.]
Cannot use double.
Results of GPU: [0. 0. 0.]
```

### macOS 10.13.3 / Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz + Intel(R) Iris(TM) Graphics 6100

```
Cannot use double.
Increase each item in array: [1. 2. 3.]
Results of CPU: [2. 3. 4.]
Results of GPU: [0. 0. 0.]
```
