import numpy as np
import pyopencl as cl

def main():
    CL_CODE = '''
    kernel void hello(void) {
      int i = 5;
      long l = 5;
      float f = 5.5;
      char c = 'A';
      constant char* s = "ABC";
      size_t sz = 10;

      printf("int %d\\n", i);
      printf("long %d\\n", l);
      printf("float %f\\n", f);
      printf("char %c\\n", c);
      printf("string %s\\n", s);
      printf("size_t %d\\n", sz);
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=cl.device_type.CPU, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    mf = cl.mem_flags
    host_s = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=bytearray(b'ABC\x00'))
    prg.hello(queue, (1,), None)
    queue.finish()

if __name__ == '__main__':
    main()
