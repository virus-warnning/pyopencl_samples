# Results on Macbook Air 2012 mid:
#
#   CPU: Intel(R) Core(TM) i7-3667U CPU @ 2.00GHz (OpenCL 1.2)
#   GPU: HD Graphics 4000 (OpenCL 1.2)
#   ------------------------------------------------------------
#   (N=10000)
#   Merge Sort OpenCL+CPU: 0.03s
#   Merge Sort OpenCL+GPU: 0.03s
#   built-in sorted():     0.00s
#   ------------------------------------------------------------
#   (N=100000)
#   Merge Sort OpenCL+CPU: 0.03s
#   Merge Sort OpenCL+GPU: 0.12s
#   built-in sorted():     0.05s
#   ------------------------------------------------------------
#   (N=1000000)
#   Merge Sort OpenCL+CPU: 0.22s
#   Merge Sort OpenCL+GPU: 0.98s
#   built-in sorted():     0.80s

import time
import random
import numpy as np
import pyopencl as cl

def cl_merge_sort(data_in, dev_type):
    CL_CODE = '''
    kernel void merge(global long* data, global long* buff, private int data_len, private int chunk_size) {
        const int gid = get_global_id(0);
        const int l_beg = gid * chunk_size;
        const int r_beg = l_beg + (chunk_size >> 1);
        const int r_end = min(l_beg + chunk_size, data_len);

        int b_ptr = l_beg;
        int l_ptr = l_beg;
        int r_ptr = r_beg;

        while (b_ptr < r_end) {
            if (l_ptr == r_beg) {
                buff[b_ptr] = data[r_ptr++];
            } else if (r_ptr >= r_end) {
                buff[b_ptr] = data[l_ptr++];
            } else {
                if (data[l_ptr] < data[r_ptr]) {
                    buff[b_ptr] = data[l_ptr++];
                } else {
                    buff[b_ptr] = data[r_ptr++];
                }
            }
            b_ptr++;
        }
    }
    '''

    ctx = cl.Context(dev_type=dev_type)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    mf = cl.mem_flags

    data_np = np.int64(data_in)
    buff_np = np.empty_like(data_np)

    data = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data_np)
    buff = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=buff_np)
    data_len = np.int32(len(data_np))
    chunk_size = np.int32(1)
    while chunk_size < data_len:
        chunk_size <<= 1
        group_size = ((data_len - 1) // chunk_size) + 1
        prg.merge(queue, (group_size,), (1,), data, buff, data_len, chunk_size)
        temp = data
        data = buff
        buff = temp

    queue.finish()
    cl.enqueue_copy(queue, data_np, data)
    data_sorted = data_np.tolist()

    data.release()
    buff.release()

    return data_sorted

def list_devices():
    for dev in cl.get_platforms()[0].get_devices():
        dev_name = dev.get_info(cl.device_info.NAME)
        dev_type = cl.device_type.to_string(dev.get_info(cl.device_info.TYPE))
        dev_ver = dev.get_info(cl.device_info.VERSION).strip()
        print('{}: {} ({})'.format(dev_type, dev_name, dev_ver))

def benchmark(data):
    print('(N={})'.format(len(data)))

    begin = time.time()
    result = cl_merge_sort(data, cl.device_type.CPU)
    elapsed = time.time() - begin
    print('Merge Sort OpenCL+CPU: {:.2f}s'.format(elapsed))

    begin = time.time()
    result = cl_merge_sort(data, cl.device_type.GPU)
    elapsed = time.time() - begin
    print('Merge Sort OpenCL+GPU: {:.2f}s'.format(elapsed))

    begin = time.time()
    result = sorted(data)
    elapsed = time.time() - begin
    print('built-in sorted():     {:.2f}s'.format(elapsed))

def main():
    data = [0] * 1000000
    for i in range(1000000):
        data[i] = random.randint(1, 2000000)

    list_devices()
    print('-' * 60)
    benchmark(data[0:10000])
    print('-' * 60)
    benchmark(data[0:100000])
    print('-' * 60)
    benchmark(data)

if __name__ == '__main__':
    main()
