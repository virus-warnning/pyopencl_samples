import numpy as np
import pyopencl as cl

def test_address_space(dev_type):
    CL_CODE = '''
    kernel void pass_private(private int i) {
        printf(" private: i = %d\\n", i);
    }

    kernel void pass_local(local int* i) {
        printf("   local: i = [%d", i[0]);
        for (int n=1; n<3; n++) {
            printf(", %d", i[n]);
        }
        printf("]\\n");
    }

    kernel void pass_global(global int* i) {
        i[0]++;
        printf("  global: i = [%d", i[0]);
        for (int n=1; n<3; n++) {
            i[n]++;
            printf(", %d", i[n]);
        }
        printf("]\\n");
    }

    kernel void pass_constant(constant int* i) {
        printf("constant: i = [%d", i[0]);
        for (int n=1; n<3; n++) {
            printf(", %d", i[n]);
        }
        printf("]\\n");
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=dev_type, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    mf = cl.mem_flags
    local_mem = cl.LocalMemory(3 * 4)
    global_mem = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=np.int32([1, 2, 3]))
    prg.pass_private(queue, (1,), None, np.int32(1))
    prg.pass_local(queue, (1,), None, local_mem)
    prg.pass_global(queue, (1,), None, global_mem)
    prg.pass_constant(queue, (1,), None, global_mem)
    queue.finish()

def main():
    print("======== Test address spaces on CPU ========", flush=True)
    test_address_space(cl.device_type.CPU)
    print("======== Test address spaces on GPU ========", flush=True)
    test_address_space(cl.device_type.GPU)

if __name__ == '__main__':
    main()
