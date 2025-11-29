'''

Check String
=======================
Agar aapko koi word check krna hai string me hai ya nahi to aap "in" keyword k help se easily find kr sakte hai
Example : 
x = "I am Aman and working in IT"
"IT" word check krna hai x me hai ya nahi 

x = "I am Aman and working i IT"
print("IT" in x)
True

print("it" in x)
False


x = "Deepak is living in UP"
if "Deepak" in x:
    print("Yes, Deepak is available in x")
    
Yes, Deepak is available in x


x = "Deepak is living in UP"
if "deepak" in x:
    print("Yes, deepak is available in x")
else:
    print("No, deepak is not available in x")

No, deepak is not available in x



x = "Deepak is living in UP"
if "Deepak" in x:
    print("Yes, Deepak is available in x")

    
Yes, Deepak is available in x

if "Deepak" not in x:
    print("Yes, Deepak is available in x")

if "deepak" not in x:
    print("Yes, deepak is not available in x")

    
Yes, deepak is not available in x

'''