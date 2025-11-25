"""
13) memoryview() --> memory data type me convert krne k liye

Example: 
x=5
print(x)
5
type(x)
<class 'int'>

x= memoryview(5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x= memoryview(5)
TypeError: memoryview: a bytes-like object is required, not 'int'

x = memoryview(bytes(5))
x
<memory at 0x0000013B3167B580>
type(x)
<class 'memoryview'>

"""