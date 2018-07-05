import numpy as np
import pyopencl as cl

def barrier_test(dev_type):
    CL_CODE = '''
    kernel void barrier_test(local int* temp, int with_barrier) {
        int lid = get_local_id(0);
        size_t lsz = get_local_size(0);

        if (lid % 2 == 1) {
            int loop = lid * lid;
            for (int n = 0; n < loop; n++) {
                printf("\\r");
            }
        }

        temp[lid] = lid;
        if (with_barrier == 1) {
            barrier(CLK_LOCAL_MEM_FENCE);
        }

        if (lid == 0) {
            int sum = 0;
            for (size_t i=0; i<lsz; i++) {
                sum += temp[i];
            }
            printf("sum[0..%d]=%d\\n", lsz, sum);
        }
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=dev_type, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    ITEM_COUNT = 100
    temp = cl.LocalMemory(ITEM_COUNT * 4)
    print('* Run without barrier:', flush=True)
    try:
        prg.barrier_test(queue, (ITEM_COUNT,), (ITEM_COUNT,), temp, np.int32(0))
    except cl.cffi_cl.LogicError as ex:
        print(ex, flush=True)
    finally:
        queue.finish()
    print('* Run with barrier:', flush=True)
    try:
        prg.barrier_test(queue, (ITEM_COUNT,), (ITEM_COUNT,), temp, np.int32(1))
    except cl.cffi_cl.LogicError as ex:
        print(ex, flush=True)
    finally:
        queue.finish()

def main():
    print('=== Test GPU ===', flush=True)
    barrier_test(cl.device_type.GPU)
    print('=== Test CPU ===', flush=True)
    barrier_test(cl.device_type.CPU)

if __name__ == '__main__':
    main()
