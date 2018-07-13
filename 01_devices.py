import numpy as np
import pyopencl as cl

def main():
    # List platforms.
    for pi, p in enumerate(cl.get_platforms()):
        p_name = p.get_info(cl.platform_info.NAME)
        p_ver = p.get_info(cl.platform_info.VERSION)
        print('[{}] {} / {}'.format(pi, p_name, p_ver))

        # List devices.
        for di, d in enumerate(p.get_devices()):
            # CPU name of Intel Core 3th gen may appear redundant spaces on Windows.
            d_name = d.get_info(cl.device_info.NAME).strip()
            d_type = cl.device_type.to_string(d.get_info(cl.device_info.TYPE))
            print('|- [{}:{}] {} / {}'.format(pi, di, d_type, d_name))

            # Show primary informations.
            d_cu   = d.get_info(cl.device_info.MAX_COMPUTE_UNITS)
            print('   |- Max Compute Units: {}'.format(d_cu))
            d_wgsz = d.get_info(cl.device_info.MAX_WORK_GROUP_SIZE)
            print('   |- Max Work Group Size: {}'.format(d_wgsz))
            d_widm = d.get_info(cl.device_info.MAX_WORK_ITEM_DIMENSIONS)
            print('   |- Max Work Item Dimensions: {}'.format(d_widm))
            d_wisz = d.get_info(cl.device_info.MAX_WORK_ITEM_SIZES)
            print('   |- Max Work Item Size: {}'.format(d_wisz))
            d_lmsz = d.get_info(cl.device_info.LOCAL_MEM_SIZE)
            print('   |- Max Local Memory Size: {}KB'.format(d_lmsz >> 10))
            d_gmsz = d.get_info(cl.device_info.GLOBAL_MEM_SIZE)
            print('   |- Max Global Memory Size: {}MB'.format(d_gmsz >> 20))
            d_freq = d.get_info(cl.device_info.MAX_CLOCK_FREQUENCY)
            print('   |- Max Clock Frequency: {}MHz'.format(d_freq))

            # List extensions.
            print('   |- Extensions: ')
            d_exts = d.get_info(cl.device_info.EXTENSIONS).strip().split(' ')
            for ext in d_exts:
                print('      |- {}'.format(ext))

if __name__ == '__main__':
    main()
