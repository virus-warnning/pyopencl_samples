import os
import numpy as np
import pyopencl as cl
from PIL import Image

def main():
    CL_CODE = '''
    constant float R_weight = 0.6;
    constant float G_weight = 0.4;
    constant float B_weight = 0.8;
    constant float ALL_weight = 1.8;
    constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE |
                                 CLK_ADDRESS_CLAMP |
                                 CLK_FILTER_NEAREST;

    kernel void gray(__read_only image2d_t src_img, __write_only image2d_t dst_img) {
        int x = get_global_id(0);
        int y = get_global_id(1);

        int2 coord = (int2)(x, y);
        uint4 pixel = read_imageui(src_img, sampler, coord);
        uint g = (uint)((pixel[0] * R_weight + pixel[1] * G_weight + pixel[2] * B_weight) / ALL_weight);
        pixel = g;
        pixel[3] = 255;
        write_imageui(dst_img, coord, pixel);
    }
    '''

    plf = [(cl.context_properties.PLATFORM, cl.get_platforms()[0])]
    ctx = cl.Context(dev_type=cl.device_type.GPU, properties=plf)
    prg = cl.Program(ctx, CL_CODE).build()
    queue = cl.CommandQueue(ctx)
    mf = cl.mem_flags

    src_raw = np.asarray(Image.open('res/tile-z16.png').convert("RGBA"))
    src_img = cl.image_from_array(ctx, src_raw, 4)
    (w, h, _) = src_raw.shape
    image_size = (w, h)

    fmt = cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.UNSIGNED_INT8)
    dst_img = cl.Image(ctx, mf.WRITE_ONLY, fmt, shape=image_size)
    dst_raw = np.empty_like(src_raw)

    prg.gray(queue, image_size, (1, 1), src_img, dst_img)
    cl.enqueue_copy(queue, dst_raw, dst_img, origin=(0, 0), region=image_size)
    Image.fromarray(dst_raw).show()

if __name__ == '__main__':
    main()
