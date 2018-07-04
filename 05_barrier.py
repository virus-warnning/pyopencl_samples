import os
import numpy as np
import pyopencl as cl

def main():
    CL_CODE = '''
    kernel void barrier_test(local int* temp, int with_barrier) {
        int lid = get_local_id(0);

        if (lid % 2 == 1) {
            for (int n = 0; n < 1000; n++) {
                printf("\\r");
            }
        }

        temp[lid] = lid;
        if (with_barrier == 1) {
            barrier(CLK_LOCAL_MEM_FENCE);
        }

        if (lid == 0) {
            int sum = 0;
            for (int i=4; i>=0; i--) {
                printf("temp[%d]=%d\\n", i, temp[i]);
                sum += temp[i];
            }
            printf("sum=%d\\n", sum);
        }
    }
    '''

    os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'

    ctx = cl.Context(dev_type=cl.device_type.GPU)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    temp = cl.LocalMemory(5 * 4)
    print('===== Run without barrier =====')
    prg.barrier_test(queue, (5,), (5,), temp, np.int32(0))
    queue.finish()
    print('===== Run with barrier =====')
    prg.barrier_test(queue, (5,), (5,), temp, np.int32(1))
    queue.finish()

if __name__ == '__main__':
    main()
