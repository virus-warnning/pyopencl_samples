# A precision test for 64-bits floating point value.
#
# It's the output on Intel i7 3667U + HD Graphics 4000.
# The GPU doesn't support 64-bits floating point value.
#
#   Increase each items in array: [1. 2. 3.]
#   Results of CPU: [2. 3. 4.]
#   Results of GPU: [2.40000038e+001 5.26354425e-315 0.00000000e+000]
#
# See: https://stackoverflow.com/questions/11176990/opencl-floating-point-precision

import numpy as np
import pyopencl as cl

def cl_inc_doubles(dev_type, data):
    CL_CODE = '''
    #pragma OPENCL EXTENSION cl_khr_fp64 : enable
    kernel void inc_doubles(global const double* data, global double* results) {
      int gid = get_global_id(0);
      results[gid] = data[gid] + 1.0;
    }
    '''

    # Build kernel on CPU or GPU
    ctx = cl.Context(dev_type=dev_type)
    prg = cl.Program(ctx, CL_CODE).build()

    # Allocate memories.
    mf = cl.mem_flags
    buf_data = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=data)
    buf_result = cl.Buffer(ctx, mf.WRITE_ONLY, data.nbytes)

    # Run.
    queue = cl.CommandQueue(ctx)
    prg.inc_doubles(queue, data.shape, (1,), buf_data, buf_result)
    queue.finish()
    result = np.empty_like(data)
    cl.enqueue_copy(queue, result, buf_result)
    buf_data.release()
    buf_result.release()

    return result

def main():
    data = np.array([1.0, 2.0, 3.0])
    print('Increase each items in array:', data)
    print('Results of CPU:', cl_inc_doubles(cl.device_type.CPU, data))
    print('Results of GPU:', cl_inc_doubles(cl.device_type.GPU, data))

if __name__ == '__main__':
    main()
