import numpy as np
import pyopencl as cl

def cl_inc_doubles(dev_type, data):
    CL_CODE = '''
    #ifdef cl_khr_fp64
    kernel void inc_doubles(global const double* data, global double* results) {
      int gid = get_global_id(0);
      results[gid] = data[gid] + 1.0;
    }
    #else
    kernel void inc_doubles(global const void* data, global void* results) {
      int gid = get_global_id(0);
      if (gid==0) {
        printf("Cannot use double.\\n");
      }
    }
    #endif
    '''

    # Build kernel on CPU or GPU
    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=dev_type, properties=plf)
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
    print('Increase each item in array:', data, flush=True)
    print('Results of CPU:', cl_inc_doubles(cl.device_type.CPU, data), flush=True)
    print('Results of GPU:', cl_inc_doubles(cl.device_type.GPU, data), flush=True)

if __name__ == '__main__':
    main()
