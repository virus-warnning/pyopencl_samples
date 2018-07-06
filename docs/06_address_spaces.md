[Home](../../../#overview)

# About 06_address_spaces.py

## Output

### Win10 / Intel Core i5 3470 + HD Graphics 2500

```
======== Test address spaces on CPU ========
... Python\Python36\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
 private: i = 1
   local: i = [0, 0, 0]
  global: i = [2, 3, 4]
constant: i = [2, 3, 4]
======== Test address spaces on GPU ========
 private: i = 1
   local: i = [0, 0, 0]
  global: i = [2, 3, 4]
constant: i = [2, 3, 4]
```

### macOS 10.13.3 / Intel Core i7 3667U + HD Graphics 4000

```
======== Test address spaces on CPU ========
 private: i = 1
   local: i = [195949888, 28672, 211209229]
  global: i = [2, 3, 4]
constant: i = [2, 3, 4]
======== Test address spaces on GPU ========
 private: i = 1
   local: i = [0, 0, 0]
  global: i = [2, 3, 4]
constant: i = [2, 3, 4]
```
