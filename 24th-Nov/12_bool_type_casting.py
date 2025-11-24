"""
10) bool() --> Boolean data type me convert krne k liye 
Boolean bas 2 value ko support krta hai 
====================================================================
a) True --> True ka value "1" hota hai 
x = True
x
True
type(x)
<class 'bool'>

x = bool(1)
x
True
type(x)
<class 'bool'>

==================================================================

b) False  --> False ka value "0" hota hai
x = False
x
False
type(x)
<class 'bool'>


x= bool(0)
x
False
type(x)
<class 'bool'>
====================================================================


# Any positive or negative numbers including floting numbers except 0 and 0.0
x = bool(232)
x
True
type(x)
<class 'bool'>

x = bool(-3434)
x
True
type(x)
<class 'bool'>

x = bool(3343.33)
x
True
type(x)
<class 'bool'>

x=bool(-33423.2323)
x
True
type(x)
<class 'bool'>

x=bool(0.00001)
x
True
type(x)
<class 'bool'>

=======================================================
# 0 and 0.0 only having False 
x=bool(0)
x
False
type(x)
<class 'bool'>


x = bool(0.0)
x
False
type(x)
<class 'bool'>

"""