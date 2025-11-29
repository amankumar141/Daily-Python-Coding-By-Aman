'''

Slicing 
========================================
aap range of characters return kr sakte hai slicing krke 

Concept yahi hai slicing ka 
Agar x = "Aman" hai toh 
string ka range 0-3 --> return krega "Aman"
agar range 1-3 hai --> return "man" krega
agar range 2-3 hai --> "an" return krega
agar range 3-3 hai --> only "n" return krega 


3 terms ko samajhna padega 
======================================
1) starting index --> aapko string ka range kha se start krna hai 
	(By default starting point "0" hota hai)
2) ending index --> aapko string ka range kha pe end krna hai 
	(by default ending point "len()"  hoga 
3) increment/decrement --> left to right indexing me ja rahe to increment hoga, right to left indexing kr rahe to decrement hoga negative me 
	(by default value "1" hota hai jo increment order me hota hai)

String[ Start_index : End_index : iteration ]


x = "0123456789"
print(x)
0123456789
type(x)
<class 'str'>

x[0]
'0'
x[1]
'1'
x[2]
'2'
x[3]
'3'
x[4]
'4'
x[5]
'5'
x[6]
'6'
x[7]
'7'
x[8]
'8'
x[9]
'9'
x[10]
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    x[10]
IndexError: string index out of range


print(x)
0123456789
len(x)
10

x
'0123456789'
x[0:10:1]
'0123456789'
x[0:10:2]
'02468'
x[0:10:3]
'0369'
x[0:10:4]
'048'

x
'0123456789'
x[0:10:1]
'0123456789'
x[1:10:1]
'123456789'
x[6:10:1]
'6789'
x[4:10:1]
'456789'


x
'0123456789'
x[0:9:1]
'012345678'
x[0:5:1]
'01234'
x[0:8:1]
'01234567'


Example :
x = "Deepak"
x
'Deepak'
x[0:6:1]
'Deepak'

x[0:4:1]
'Deep'

x[0:2:1]
'De'
x[4:6:1]
'ak'
x[2:4:1]
'ep'



Negative slicing :
=======================================================
right to left hota hai indexing 
starting and ending point right to left rakhte hai to negative -1 hoga
starting and ending point left to right rakhte hai to positive 1 hoga 
Example : 
x = "Deepak"
x[-7: :1]
'Deepak'
x[-1:-7:-1]
'kapeeD'

x[-5:-3:1]
'ee'

'''