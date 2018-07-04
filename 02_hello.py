import numpy as np
import pyopencl as cl

def main():
    GLOBAL_WORK_SIZE = 5

    CL_CODE = '''
    kernel void hello(void) {
      int gid = get_global_id(0);
      printf("Hello! I'm work item #%d.\\n", gid);
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=cl.device_type.GPU, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    prg.hello(queue, (GLOBAL_WORK_SIZE,), None)
    queue.finish()

if __name__ == '__main__':
    main()
