[Home](../../../#overview)

# About 04_group.py

## Known Issues

### clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE

Work size doesn't run as expected on macOS 10.13.3 + i7 3667U.

While global work size is 6, local work size accept 1 or None (NULL) only.

If any other reasonable value (e.g. 2, 3, 6) is given for local work size, INVALID_WORK_GROUP_SIZE is returned.

### default local work size

While global work size is 6 and local work size is None (NULL), the results between CPU and GPU are different.

* 6 local work size were created on Intel HD Graphics.
* 1 local work size was created on Intel CPU.

It means kernels cannot run in the same work group on Intel CPU while None (NULL) is given for local work size.

So that barrier() would not work as expected.

Therefore it is better to assign a specific value for local work size.

## Output

### Win10 / Intel Core i5 7200U + HD Graphics 620

```
===== (device: GPU, global work size: 6, local work size: undefined) =====
... Python\Python37\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: undefined) =====
global_id=0, local_id=0, group_id=0
global_id=2, local_id=0, group_id=2
global_id=1, local_id=0, group_id=1
global_id=3, local_id=0, group_id=3
global_id=4, local_id=0, group_id=4
global_id=5, local_id=0, group_id=5
===== (device: GPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=3, local_id=0, group_id=3
global_id=1, local_id=0, group_id=1
global_id=4, local_id=0, group_id=4
global_id=2, local_id=0, group_id=2
global_id=5, local_id=0, group_id=5
===== (device: CPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=2, local_id=0, group_id=2
global_id=5, local_id=0, group_id=5
global_id=4, local_id=0, group_id=4
global_id=3, local_id=0, group_id=3
global_id=1, local_id=0, group_id=1
===== (device: GPU, global work size: 6, local work size: 2) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
===== (device: CPU, global work size: 6, local work size: 2) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
===== (device: GPU, global work size: 6, local work size: 6) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: 6) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
```

### Win10 / Intel Core i5 3470 + HD Graphics 2500

```
===== (device: GPU, global work size: 6, local work size: undefined) =====
... Python\Python36\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: undefined) =====
global_id=0, local_id=0, group_id=0
global_id=4, local_id=0, group_id=4
global_id=5, local_id=0, group_id=5
global_id=3, local_id=0, group_id=3
global_id=2, local_id=0, group_id=2
global_id=1, local_id=0, group_id=1
===== (device: GPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=0, group_id=1
global_id=3, local_id=0, group_id=3
global_id=2, local_id=0, group_id=2
global_id=5, local_id=0, group_id=5
global_id=4, local_id=0, group_id=4
===== (device: CPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=4, local_id=0, group_id=4
global_id=5, local_id=0, group_id=5
global_id=2, local_id=0, group_id=2
global_id=3, local_id=0, group_id=3
global_id=1, local_id=0, group_id=1
===== (device: GPU, global work size: 6, local work size: 2) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
===== (device: CPU, global work size: 6, local work size: 2) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
===== (device: GPU, global work size: 6, local work size: 6) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: 6) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
```

### macOS 10.13.3 / Intel Core i7-3667U + HD Graphics 4000

```
===== (device: GPU, global work size: 6, local work size: undefined) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: undefined) =====
global_id=0, local_id=0, group_id=0
global_id=4, local_id=0, group_id=4
global_id=5, local_id=0, group_id=5
global_id=1, local_id=0, group_id=1
global_id=2, local_id=0, group_id=2
global_id=3, local_id=0, group_id=3
===== (device: GPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=2, local_id=0, group_id=2
global_id=1, local_id=0, group_id=1
global_id=4, local_id=0, group_id=4
global_id=3, local_id=0, group_id=3
global_id=5, local_id=0, group_id=5
===== (device: CPU, global work size: 6, local work size: 1) =====
global_id=0, local_id=0, group_id=0
global_id=3, local_id=0, group_id=3
global_id=5, local_id=0, group_id=5
global_id=4, local_id=0, group_id=4
global_id=2, local_id=0, group_id=2
global_id=1, local_id=0, group_id=1
===== (device: GPU, global work size: 6, local work size: 2) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
===== (device: CPU, global work size: 6, local work size: 2) =====
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
===== (device: GPU, global work size: 6, local work size: 6) =====
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: CPU, global work size: 6, local work size: 6) =====
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```
### macOS 10.13.3 / Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz + Intel(R) Iris(TM) Graphics 6100

```
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
global_id=0, local_id=0, group_id=0
global_id=2, local_id=0, group_id=2
global_id=3, local_id=0, group_id=3
global_id=1, local_id=0, group_id=1
global_id=4, local_id=0, group_id=4
global_id=5, local_id=0, group_id=5
global_id=5, local_id=0, group_id=5
global_id=3, local_id=0, group_id=3
global_id=4, local_id=0, group_id=4
global_id=1, local_id=0, group_id=1
global_id=0, local_id=0, group_id=0
global_id=2, local_id=0, group_id=2
global_id=1, local_id=0, group_id=1
global_id=3, local_id=0, group_id=3
global_id=4, local_id=0, group_id=4
global_id=0, local_id=0, group_id=0
global_id=5, local_id=0, group_id=5
global_id=2, local_id=0, group_id=2
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=0, group_id=1
global_id=3, local_id=1, group_id=1
global_id=4, local_id=0, group_id=2
global_id=5, local_id=1, group_id=2
global_id=0, local_id=0, group_id=0
global_id=1, local_id=1, group_id=0
global_id=2, local_id=2, group_id=0
global_id=3, local_id=3, group_id=0
global_id=4, local_id=4, group_id=0
global_id=5, local_id=5, group_id=0
===== (device: GPU, global work size: 6, local work size: undefined) =====
===== (device: CPU, global work size: 6, local work size: undefined) =====
===== (device: GPU, global work size: 6, local work size: 1) =====
===== (device: CPU, global work size: 6, local work size: 1) =====
===== (device: GPU, global work size: 6, local work size: 2) =====
===== (device: CPU, global work size: 6, local work size: 2) =====
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
===== (device: GPU, global work size: 6, local work size: 6) =====
===== (device: CPU, global work size: 6, local work size: 6) =====
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```
