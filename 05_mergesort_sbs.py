import io
import random
import numpy as np
import pyopencl as cl

def dump_step(data, chunk_size):
    msg = io.StringIO('')
    div = io.StringIO('')
    for idx, item in enumerate(data):
        if idx % chunk_size == 0:
            if idx > 0:
                msg.write(' ||')
                div.write('   ')
            div.write(' --')
        else:
            msg.write('   ')
            div.write('------')
        msg.write(' {:2d}'.format(item))

    out = msg.getvalue()
    if chunk_size == 1: print(' ' + '-' * (len(out) - 1))
    print(out)
    print(div.getvalue())
    msg.close()
    div.close()

def cl_merge_sort_sbs(data_in):
    CL_CODE = '''
    kernel void merge(int chunk_size, int size, global long* data, global long* buff) {
        const int gid = get_global_id(0);
        const int offset = gid * chunk_size;
        const int real_size = min(offset + chunk_size, size) - offset;

        global long* data_part = data + offset;
        global long* buff_part = buff + offset;

        int r_beg = chunk_size >> 1;
        int b_ptr = 0;
        int l_ptr = 0;
        int r_ptr = r_beg;

        while (b_ptr < real_size) {
            if (r_ptr >= real_size) {
                buff_part[b_ptr] = data_part[l_ptr++];
            } else if (l_ptr == r_beg) {
                buff_part[b_ptr] = data_part[r_ptr++];
            } else {
                if (data_part[l_ptr] < data_part[r_ptr]) {
                    buff_part[b_ptr] = data_part[l_ptr++];
                } else {
                    buff_part[b_ptr] = data_part[r_ptr++];
                }
            }
            b_ptr++;
        }
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=cl.device_type.GPU, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    mf = cl.mem_flags

    data_np = np.int64(data_in)
    buff_np = np.empty_like(data_np)

    data = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data_np)
    buff = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=buff_np)
    data_len = np.int32(len(data_np))
    chunk_size = np.int32(1)
    dump_step(data_np, chunk_size)

    while chunk_size < data_len:
        chunk_size <<= 1
        group_size = ((data_len - 1) // chunk_size) + 1
        prg.merge(queue, (group_size,), (1,), chunk_size, data_len, data, buff)
        temp = data
        data = buff
        buff = temp
        cl.enqueue_copy(queue, data_np, data)
        dump_step(data_np, chunk_size)

    queue.finish()
    data.release()
    buff.release()

def main():
    n = random.randint(5, 16)
    data = []
    for i in range(n):
        data.append(random.randint(1, 99))
    cl_merge_sort_sbs(data)

if __name__ == '__main__':
    main()
