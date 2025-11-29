'''

What is Arrays : 
==========================================================================
## aap ek value ko variable me store kr rahe hai
x = 10
EK value ko variable me assign kr rahe hai
Example : 
x = 10
print(x)
10
len(x)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    len(x)
TypeError: object of type 'int' has no len()



## Multiple values ko aap variable me assign kr rahe hai
x = 10, 20, 30 
Multiple values ko variable me assign kr rahe hai
Example : 
x = [10, 20, 30, 40, 50]
print(x)
[10, 20, 30, 40, 50]
len(x)
5
x[0]
10
x[1]
20
x[2]
30
x[3]
40
x[4]
50
x[5]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x[5]
IndexError: list index out of range




Strings are Arrays
===============================================================
Python me strings arrays hota hai Unicode characters ka


Unicode --> Unicode characters ek standardized codes hai jo represent krta hai har possible text symbol ko across sare languages, scripts, platforms etc me.
Har characters chahe wo letters ho ya number ho ya enoji ho ya koi bhi symbol ko ek unique number value se assign krte hai, jisko Unicode bolte hai

letters : 
small letters --> a b c d ..... z
Capital letters --> A B C D ...... Z

numbers :
0 1 2 3 4 5 6 7 8 9

emoji :
WhatsApp pe emoji sab wahi symbols smile, angry, etc 

symbols :
! @ # $ % ^ & * ( ) [ ] { } ' " ? / | \ ~ ` : , < > . ; etc 

Example : 
ord('a')
97
ord("A")
65


## Python k pas character data type nahi hota hai, it means agar single character bhi agar single ya double quotation marks se show krte hai to wo signle string hota hai jiska length "1" hota hai
Example : 
x = 'a'
type(x)
<class 'str'>
len(x)
1

x = 'abcd'
type(x)
<class 'str'>
len(x)
4


## Square brackers ya big bracket se humlog strings ka ek ek elements access krte hai aur first element always "0" se start hota hai
Example : 
x = "Deepak"
print(x)
Deepak
print(x[0])
D
print(x[1])
e
print(x[2])
e
print(x[3])
p
print(x[4])
a
print(x[5])
k
print(x[6])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(x[6])
IndexError: string index out of range


## isko aap negative number se bhi access kr sakte hai, first element always start with "-1" in reverse order 
Example : 
x = "Deepak"
print(x)
Deepak
print(x[-1])
k
print(x[-2])
a
print(x[-3])
p
print(x[-4])
e
print(x[-5])
e
print(x[-6])
D
print(x[-7])
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(x[-7])
IndexError: string index out of range


'''