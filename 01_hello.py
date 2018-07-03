import os
import numpy as np
import pyopencl as cl

def main():
    GLOBAL_GROUP = 6
    LOCAL_GROUP = 2

    CL_CODE = '''
    kernel void hello(void) {
      int gid = get_global_id(0);
      int lid = get_local_id(0);
      printf("Hello World! [%d:%d]\\n", gid, lid);
    }
    '''

    os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=cl.device_type.GPU, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    prg.hello(queue, (GLOBAL_GROUP,), (LOCAL_GROUP,))
    queue.finish()

if __name__ == '__main__':
    main()
