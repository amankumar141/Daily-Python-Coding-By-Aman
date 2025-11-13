# String ka symbol "str" hota hai
# string = ordered sequence of characters
# string --> empty bhi ho sakta hai, one ya more than one characters ka group bhi ho sakta hai
# string ko single inverted comma (' ') ya double inverted comman (" ") k sath denote krte hai
# why two type of denote in string 
# case-1 when ' using as msg --> "Aman's Laptop"
# case-2 when " using as msg --> 'Deepak or "Deepu" anyone name'
# example 

x1 = "Aman"
print("x1 ka value : ", x1)
print("x1 ka type : ", type(x1))

x2 = 'Deepak'
print("x2 ka value : ", x2)
print("x2 ka type : ", type(x2))

# case-1 when ' using as msg --> "Aman's Laptop"
x3 = "Aman's Laptop"
print("x3 ka value : ", x3)
print("x3 ka type : ", type(x3))

# case-2 when " using as msg --> 'Deepak or "Deepu" anyone name'
x4 = 'Deepak or "Deepu" anyone name'
print("x4 ka value : ", x4)
print("x4 ka type : ", type(x4))

# Special type me comments ko bhi aap use kr sakte hai
x5 = ''' This is multi line comment 
with single 
inverted comma'''
print("x5 ka value: ", x5)
print("x5 ka type: ", type(x5))

# another way 
x6 = """ This is also multi line 
comment with double 
inverted comma"""
print("x6 ka value: ", x6)
print("x6 ka type: ", type(x6))