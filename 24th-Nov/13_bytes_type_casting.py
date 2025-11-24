"""
11) bytes() --> bytes data type me conver krne k liye 

String are like below
=================================
x="Aman"
x
'Aman'
type(x)
<class 'str'>

x='Aman'
x
'Aman'
type(x)
<class 'str'>


Direct strings ko bytes() support nahi krega aur error de dega
===================================================================
x = bytes("Aman")
Traceback (most recent call last):
  File "<pyshell#342>", line 1, in <module>
    x = bytes("Aman")
TypeError: string argument without an encoding



Jab aap string value se pehle "b" or "B" laga kr send krte hai to bytes() support krega
=====================================================================================
x = bytes(b"Aman")
x
b'Aman'
type(x)
<class 'bytes'>

x = bytes(b'Aman')
x
b'Aman'
type(X)
type(x)
<class 'bytes'>

x = bytes(B"Aman")
x
b'Aman'
type(x)
<class 'bytes'>

x = bytes(B'Aman')
x
b'Aman'
type(x)
<class 'bytes'>
"""