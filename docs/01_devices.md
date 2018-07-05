[Home](../../../#overview)

# About 01_devices.py

## Known Issue

While get device name of Intel Core i5 3470 on Win10, 8 reduntant spaces appear at beginning of the string.

```python
d.get_info(cl.device_info.NAME)
```

```
"        Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz"
```

Do strip() for device name is better.

```python
d.get_info(cl.device_info.NAME).strip()
```

## Output

### Win10 / Intel Core i5 7200U + HD Graphics 620

```
[0] Intel(R) OpenCL / OpenCL 2.1
|- [0:0] GPU / Intel(R) HD Graphics 620
   |- Max Compute Units: 24
   |- Max Global Memory Size: 6512MB
   |- Max Local Memory Size: 64KB
   |- Extensions:
      |- cl_intel_accelerator
      |- cl_intel_advanced_motion_estimation
      |- cl_intel_d3d11_nv12_media_sharing
      |- cl_intel_device_side_avc_motion_estimation
      |- cl_intel_driver_diagnostics
      |- cl_intel_dx9_media_sharing
      |- cl_intel_media_block_io
      |- cl_intel_motion_estimation
      |- cl_intel_planar_yuv
      |- cl_intel_packed_yuv
      |- cl_intel_required_subgroup_size
      |- cl_intel_simultaneous_sharing
      |- cl_intel_subgroups
      |- cl_intel_subgroups_short
      |- cl_khr_3d_image_writes
      |- cl_khr_byte_addressable_store
      |- cl_khr_d3d10_sharing
      |- cl_khr_d3d11_sharing
      |- cl_khr_depth_images
      |- cl_khr_dx9_media_sharing
      |- cl_khr_fp16
      |- cl_khr_fp64
      |- cl_khr_gl_depth_images
      |- cl_khr_gl_event
      |- cl_khr_gl_msaa_sharing
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_gl_sharing
      |- cl_khr_icd
      |- cl_khr_image2d_from_buffer
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_mipmap_image
      |- cl_khr_mipmap_image_writes
      |- cl_khr_spir
      |- cl_khr_subgroups
      |- cl_khr_throttle_hints
|- [0:1] CPU / Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz
   |- Max Compute Units: 4
   |- Max Global Memory Size: 16302MB
   |- Max Local Memory Size: 32KB
   |- Extensions:
      |- cl_khr_icd
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_khr_depth_images
      |- cl_khr_3d_image_writes
      |- cl_intel_exec_by_local_thread
      |- cl_khr_spir
      |- cl_khr_dx9_media_sharing
      |- cl_intel_dx9_media_sharing
      |- cl_khr_d3d11_sharing
      |- cl_khr_gl_sharing
      |- cl_khr_fp64
      |- cl_khr_image2d_from_buffer
```

### Win10 / Intel Core i5 3470 + HD Graphics 2500

```
[0] Intel(R) OpenCL / OpenCL 1.2
|- [0:0] CPU / Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz
   |- Max Compute Units: 4
   |- Max Global Memory Size: 16064MB
   |- Max Local Memory Size: 32KB
   |- Extensions:
      |- cl_khr_fp64
      |- cl_khr_icd
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_intel_printf
      |- cl_ext_device_fission
      |- cl_intel_exec_by_local_thread
      |- cl_khr_gl_sharing
      |- cl_intel_dx9_media_sharing
      |- cl_khr_dx9_media_sharing
      |- cl_khr_d3d11_sharing
|- [0:1] GPU / Intel(R) HD Graphics 2500
   |- Max Compute Units: 6
   |- Max Global Memory Size: 1246MB
   |- Max Local Memory Size: 64KB
   |- Extensions:
      |- cl_intel_d3d11_nv12_media_sharing
      |- cl_intel_dx9_media_sharing
      |- cl_khr_3d_image_writes
      |- cl_khr_byte_addressable_store
      |- cl_khr_d3d10_sharing
      |- cl_khr_d3d11_sharing
      |- cl_khr_depth_images
      |- cl_khr_dx9_media_sharing
      |- cl_khr_gl_depth_images
      |- cl_khr_gl_event
      |- cl_khr_gl_msaa_sharing
      |- cl_khr_gl_sharing
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_icd
      |- cl_khr_image2d_from_buffer
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_intel_accelerator
      |- cl_intel_motion_estimation
```

### macOS 10.13.3 / Intel Core i7-3667U + HD Graphics 4000

```
[0] Apple / OpenCL 1.2 (Oct 31 2017 18:30:00)
|- [0:0] CPU / Intel(R) Core(TM) i7-3667U CPU @ 2.00GHz
   |- Max Compute Units: 4
   |- Max Global Memory Size: 8192MB
   |- Max Local Memory Size: 32KB
   |- Extensions: 
      |- cl_APPLE_SetMemObjectDestructor
      |- cl_APPLE_ContextLoggingFunctions
      |- cl_APPLE_clut
      |- cl_APPLE_query_kernel_names
      |- cl_APPLE_gl_sharing
      |- cl_khr_gl_event
      |- cl_khr_fp64
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_khr_int64_base_atomics
      |- cl_khr_int64_extended_atomics
      |- cl_khr_3d_image_writes
      |- cl_khr_image2d_from_buffer
      |- cl_APPLE_fp64_basic_ops
      |- cl_APPLE_fixed_alpha_channel_orders
      |- cl_APPLE_biased_fixed_point_image_formats
      |- cl_APPLE_command_queue_priority
|- [0:1] GPU / HD Graphics 4000
   |- Max Compute Units: 16
   |- Max Global Memory Size: 1536MB
   |- Max Local Memory Size: 64KB
   |- Extensions: 
      |- cl_APPLE_SetMemObjectDestructor
      |- cl_APPLE_ContextLoggingFunctions
      |- cl_APPLE_clut
      |- cl_APPLE_query_kernel_names
      |- cl_APPLE_gl_sharing
      |- cl_khr_gl_event
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_khr_image2d_from_buffer
      |- cl_khr_gl_depth_images
      |- cl_khr_depth_images
      |- cl_khr_3d_image_writes
```

### macOS 10.13.3 / Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz + Intel(R) Iris(TM) Graphics 6100

```
[0] Apple / OpenCL 1.2 (Oct 31 2017 18:30:00)
|- [0:0] CPU / Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz
   |- Max Compute Units: 4
   |- Max Global Memory Size: 8192MB
   |- Max Local Memory Size: 32KB
   |- Extensions:
      |- cl_APPLE_SetMemObjectDestructor
      |- cl_APPLE_ContextLoggingFunctions
      |- cl_APPLE_clut
      |- cl_APPLE_query_kernel_names
      |- cl_APPLE_gl_sharing
      |- cl_khr_gl_event
      |- cl_khr_fp64
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_khr_int64_base_atomics
      |- cl_khr_int64_extended_atomics
      |- cl_khr_3d_image_writes
      |- cl_khr_image2d_from_buffer
      |- cl_APPLE_fp64_basic_ops
      |- cl_APPLE_fixed_alpha_channel_orders
      |- cl_APPLE_biased_fixed_point_image_formats
      |- cl_APPLE_command_queue_priority
|- [0:1] GPU / Intel(R) Iris(TM) Graphics 6100
   |- Max Compute Units: 48
   |- Max Global Memory Size: 1536MB
   |- Max Local Memory Size: 64KB
   |- Extensions:
      |- cl_APPLE_SetMemObjectDestructor
      |- cl_APPLE_ContextLoggingFunctions
      |- cl_APPLE_clut
      |- cl_APPLE_query_kernel_names
      |- cl_APPLE_gl_sharing
      |- cl_khr_gl_event
      |- cl_khr_global_int32_base_atomics
      |- cl_khr_global_int32_extended_atomics
      |- cl_khr_local_int32_base_atomics
      |- cl_khr_local_int32_extended_atomics
      |- cl_khr_byte_addressable_store
      |- cl_khr_image2d_from_buffer
      |- cl_khr_gl_depth_images
      |- cl_khr_depth_images
      |- cl_khr_3d_image_writes
```

