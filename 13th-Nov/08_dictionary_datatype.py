# dictionary ka symbol "dict" hota hai
# dicktionary = unordered key:value pairs 
# denoted by symbols --> { Key1:Value1, key2:value2, ..... } 
# example: { 1:"Aman", 2:"Deepak", 3:"Ghanashayam" }
# key ho ya value, string rahega tabhi single ya double inverted comma lagana padega

# key and value dono numbers hai 
x1 = { 1:123, 3:3332, 5:322323, 233232:323232 }
print("x1 ka value : ", x1)
print("x1 ka type: ", type(x1))

# key ko number me lete hai and values ko string me lenge
x2 = { 1:"one", 2:"two", 3:"three"}
print("x2 ka value : ", x2)
print("x2 ka type : ", type(x2))

# key ko string le raha and value ko number le raha 
x3 = { "One":1, "two":2, "three":3 }
print("x3 ka value : ", x3)
print("x3 ka type : ", type(x3))

# key and value dono string me le raha hu 
x4 = { "one":"Aman", "two":"Deepak", "three":"ghanashayam" }
print("x4 ka value : ", x4)
print("x4 ka type: ", type(x4))

# any datatype aap le sakte ho key me and value me bhi
x5 = { 1:[1,2,3], "Aman":12.5, 12.6:True }
print("x5 ka value : ", x5)
print("x5 ka type : ", type(x5))
