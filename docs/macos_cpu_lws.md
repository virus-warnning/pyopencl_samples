# Issues of Local Work Size on macOS + CPU

## Device Info

```
[0] Apple / OpenCL 1.2 (Oct 31 2017 18:30:00)
|- [0:0] CPU / Intel(R) Core(TM) i7-3667U CPU @ 2.00GHz
   |- Max Compute Units: 4
   |- Max Global Memory Size: 8192MB
   |- Max Local Memory Size: 32KB
   |- Max Work Group Size: 1024
   |- Max Work Item Dimensions: 3
   |- Max Work Item Size: [1024, 1, 1]
   ...
```

## Code to test this issue.

```python
import numpy as np
import pyopencl as cl

def main():
    GLOBAL_WORK_SIZE = (1024, 1, 1)
    LOCAL_WORK_SIZE = (1024, 1, 1)
    CL_CODE = '''
    kernel void test(void) {
        printf("");
    }
    '''

    ctx = cl.Context(dev_type=cl.device_type.CPU)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    try:
        prg.test(queue, GLOBAL_WORK_SIZE, LOCAL_WORK_SIZE)
        print('It works!')
    except cl.cffi_cl.LogicError as ex:
        print(ex)
    finally:
        queue.finish()

if __name__ == '__main__':
    main()
```

According to **Max Work Item Size: [1024, 1, 1]**, LOCAL_WORK_SIZE is reasonable, but an exception is thrown.

```
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```

Change LOCAL_WORK_SIZE to (2, 1, 1), then ...

```
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```

At this time, remove **printf("");** in CL_CODE, then ...

```
It works!
```

It seems local work size cannot > 1 with **printf("");**.

Without **printf("");**, change LOCAL_WORK_SIZE to (128, 1, 1), then ...

```
It works!
```

Change LOCAL_WORK_SIZE to (256, 1, 1), then ...

```
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```

Change GLOBAL_WORK_SIZE and LOCAL_WORK_SIZE to (129, 1, 1), then ...

```
clEnqueueNDRangeKernel failed: INVALID_WORK_GROUP_SIZE
```

CL_DEVICE_MAX_WORK_GROUP_SIZE of device info is 1024, but it is 128 actually.

### Summary

To use OpenCL on macOS + CPU.

* Do not use **printf()** while local work size > 1.
* The maximum local work size is (128, 1, 1).
* The 2nd and 3rd dimentions of local work size are useless.
