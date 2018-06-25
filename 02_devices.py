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
            d_name = d.get_info(cl.device_info.NAME)
            d_type = cl.device_type.to_string(d.get_info(cl.device_info.TYPE))
            d_ver = d.get_info(cl.device_info.VERSION).strip()
            print('  |- [{}:{}] {} / {} / {}'.format(pi, di, d_type, d_ver, d_name))

if __name__ == '__main__':
    main()
