[Home](../../../#overview)

# About 07_printf.py

## Output

### Win10 / Intel Core i5 3470 + HD Graphics 2500

```
===== Print by CPU =====
... Python\Python36\lib\site-packages\pyopencl\cffi_cl.py:1521: CompilerWarning: Non-empty compiler output encountered. Set the environment variable PYOPENCL_COMPILER_OUTPUT=1 to see more.
  "to see more.", CompilerWarning)
         int:    5
        long:    5
       float: 5.50
        char:    A
      string:  ABC
      size_t:   10
   int + int:    5    5
  long + int:    5    0
size_t + int:   10    0
host char[0]: 'H' 48
host char[1]: 'O' 4f
host char[2]: 'S' 53
host char[3]: 'T' 54
host char[4]: ' ' 20
host char[5]: 'S' 53
host char[6]: 'T' 54
host char[7]: 'R' 52
 host string: (null)
===== Print by GPU =====
         int:    5
        long:    5
       float: 5.50
        char:    A
      string:  ABC
      size_t:   10
   int + int:    5    5
  long + int:    5    5
size_t + int:   10    5
host char[0]: 'H' 48
host char[1]: 'O' 4f
host char[2]: 'S' 53
host char[3]: 'T' 54
host char[4]: ' ' 20
host char[5]: 'S' 53
host char[6]: 'T' 54
host char[7]: 'R' 52
ERROR: printf has thrown an exception
```

### macOS 10.13.3 / Intel Core i7 3667U + HD Graphics 4000

```
===== Print by CPU =====
         int:    5
        long:    5
       float: 5.50
        char:    A
      string:  ABC
      size_t:   10
   int + int:    5    5
  long + int:    5    5
size_t + int:   10    5
host char[0]: 'H' 48
host char[1]: 'O' 4f
host char[2]: 'S' 53
host char[3]: 'T' 54
host char[4]: ' ' 20
host char[5]: 'S' 53
host char[6]: 'T' 54
host char[7]: 'R' 52
 host string: HOST STR
===== Print by GPU =====
         int:    5
        long:    5
       float: 5.50
        char:    A
      string:  ABC
      size_t:   10
   int + int:    5    5
  long + int:    5    5
size_t + int:   10    5
host char[0]: 'H' 48
host char[1]: 'O' 4f
host char[2]: 'S' 53
host char[3]: 'T' 54
host char[4]: ' ' 20
host char[5]: 'S' 53
host char[6]: 'T' 54
host char[7]: 'R' 52
Segmentation fault: 11
```
