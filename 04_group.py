import numpy as np
import pyopencl as cl

def group_test(dev_type, gw_size, lw_size):
    CL_CODE = '''
    kernel void group_test(void) {
        int glb = get_global_id(0);
        int loc = get_local_id(0);
        int grp = get_group_id(0);
        printf("global_id=%d, local_id=%d, group_id=%d\\n", glb, loc, grp);
    }
    '''

    type_name = cl.device_type.to_string(dev_type)
    lw_name = 'undefined' if lw_size == 0 else lw_size
    print('===== (device: {}, global work size: {}, local work size: {}) ====='.format(type_name, gw_size, lw_name))

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=dev_type, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    GLOBAL_SIZE = (gw_size,)
    if lw_size > 0:
        LOCAL_SIZE = (lw_size, )
    else:
        LOCAL_SIZE = None

    try:
        prg.group_test(queue, GLOBAL_SIZE, LOCAL_SIZE)
    except cl.cffi_cl.LogicError as ex:
        print(ex)
    finally:
        queue.finish()

def main():
    group_test(cl.device_type.GPU, 6, 0)
    group_test(cl.device_type.CPU, 6, 0)

    group_test(cl.device_type.GPU, 6, 1)
    group_test(cl.device_type.CPU, 6, 1)

    group_test(cl.device_type.GPU, 6, 2)
    group_test(cl.device_type.CPU, 6, 2)

    group_test(cl.device_type.GPU, 6, 6)
    group_test(cl.device_type.CPU, 6, 6)

if __name__ == '__main__':
    main()
