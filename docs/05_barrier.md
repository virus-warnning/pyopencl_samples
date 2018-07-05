[Home](../../../#overview)

# About 05_barrier.py

## Output

### Win10 / Intel Core i5 7200U + HD Graphics 620

```
... Python\Python37\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
===== Run without barrier =====
sum[0..100]=120
===== Run with barrier =====
sum[0..100]=4950
```

### Win10 / Intel Core i5 3470 + HD Graphics 2500

The same as i5 7200U.

### macOS 10.13.3 / Intel Core i7-3667U + HD Graphics 4000

```
=== Test GPU ===
* Run without barrier:
sum[0..100]=496
* Run with barrier:
sum[0..100]=4950
=== Test CPU ===
* Run without barrier:
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
* Run with barrier:
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```
