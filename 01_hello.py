import numpy as np
import pyopencl as cl

def main():
    GLOBAL_GROUP = 6
    LOCAL_GROUP = 2

    CL_CODE = '''
    kernel void foo(void) {
      int gid = get_global_id(0);
      int lid = get_local_id(0);
      printf("Hello World! [%d:%d]\\n", gid, lid);
    }
    '''

    ctx = cl.Context(dev_type=cl.device_type.GPU)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    prg.foo(queue, (GLOBAL_GROUP,), (LOCAL_GROUP,))
    queue.finish()

if __name__ == '__main__':
    main()
