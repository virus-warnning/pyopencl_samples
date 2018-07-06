import numpy as np
import pyopencl as cl

def test_printf(dev_type):
    CL_CODE = '''
    kernel void test_format(void) {
        int i = 5;
        long l = 5;
        float f = 5.5;
        char c = 'A';
        constant char* s = "ABC";
        size_t sz = 10;

        printf("         int: %4d\\n", i);
        printf("        long: %4d\\n", l);
        printf("       float: %1.2f\\n", f);
        printf("        char: %4c\\n", c);
        printf("      string: %4s\\n", s);
        printf("      size_t: %4d\\n", sz);
        printf("   int + int: %4d %4d\\n", i, i);
        printf("  long + int: %4d %4d\\n", l, i);
        printf("size_t + int: %4u %4d\\n", sz, i);
    }

    kernel void test_host_chars(constant char* host_str) {
        for (int n=0; n<8; n++) {
            printf("host char[%d]: '%c' %02x\\n", n, host_str[n], host_str[n]);
        }
    }

    kernel void test_host_string(constant char* host_str) {
        printf(" host string: %s\\n", host_str);
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=dev_type, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)

    mf = cl.mem_flags
    host_s = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b'HOST STR\x00')
    prg.test_format(queue, (1,), None)

    try:
        prg.test_host_chars(queue, (1,), None, host_s);
    except ex:
        print("Something went wrong in kernel test_host_chars(...)")

    try:
        prg.test_host_string(queue, (1,), None, host_s);
    except ex:
        print("Something went wrong in kernel test_host_string(...)")

    queue.finish()

def main():
    print('===== Print by CPU =====')
    test_printf(cl.device_type.CPU)
    print('===== Print by GPU =====')
    test_printf(cl.device_type.GPU)

if __name__ == '__main__':
    main()
