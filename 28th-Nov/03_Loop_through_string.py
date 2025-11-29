'''
Looping Through a String
===================================================
String jo hai wo python me array hota hai, isliye humlog string me characters ko "for" loop se iterate kr sakte hai
Example: 
x = "Deepak"
for i in x:
    print(i)
    
D
e
e
p
a
k


How Loop will work, explained in  depth
====================================================================================================
x = "Deepak"

for i in x:
	print(i)

for i in "Deepak":
	print(i)

i in "Deepak" --> "i" temp variable hai
i (index 0) = D --> print(i) --> D print kr diya --> by default automatic +1 increase ho jata hai index 
i (index 0+1=1) = e --> print(i) --> e print kr diya --> by default +1 increate ho gaya 
i (index 1+1=2) = e --> print(i) --> e print kr diya --> +1 increase kr dega index 
i (index 2+1=3) = p --> print(i) --> p print kr diya --> +1 index badha dega 
i (index 3+1-4) = a --> print(i) --> a print kr diya --> +1 index badha dega 
i (index 4+1=5) = k --> print(i) --> k print kr diya --> +1 index badha dega 
i (index 5+1=6) = kuch nahi mikega --> loop ko end kr dega aur aapko output dega 

Output : 
======================
D
e
e
p
a
k


'''