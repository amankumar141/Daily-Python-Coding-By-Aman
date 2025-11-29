'''
Strings
====================================================================================================
String ko humlog single quotation marks (' ') ya double quotation marks (" ") se denote krte hai
Example: 
## jab aap single quotation marks (' ') use kr rahe hai string value ko assign krne me 
x = 'Aman'
print(x)
Aman
print(type(x))
<class 'str'>

## jab aap double quotation marks (" ") use kr rahe hai string value ko assign krne me 
y = "Deepak"
print(y)
Deepak
print(type(y))
<class 'str'>


Quotes Inside Quotes
==============================================================================================
## Jab aap double quotation marks (" ") k under single quotation marks (' ') use kr rahe hai 
print("It's alright")
It's alright

## Jab aap single quotation marks (' ') k under double quotation marks (" ") use kr rahe hai 
print('He is called "Johnny"')
He is called "Johnny"


Assign String to a Variable
===============================================================================================
## String ko humlog variable k under assign krte hai jab string value ko equal to operator k sath use krte hai
x = "Aman"
print(x)
Aman


Multi-line Strings
================================================================================================
## jab aap msg ko multiple lines me print() k under send krte to error aayega hame 
print(" This is line1
This is line2")
SyntaxError: unterminated string literal (detected at line 1)

Example :
## Jab aap single quotation marks (' ') k under double quotation marks (" ") ka symbol use krte hai tab 
print('''This is line1
This is line2''')
      
This is line1
This is line2


## Jab aap double quotation marks (" ") k under single quotation marks (' ') ka symbol use krte hai tab 
print("""This is line1
This is line2""")
      
This is line1
This is line2


'''