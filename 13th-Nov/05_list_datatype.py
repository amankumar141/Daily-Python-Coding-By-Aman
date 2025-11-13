# lists ka symbol "list" hota hai
# list = ordered sequence of objects
# denoted by symbol --> [ Value1, Value2, Value3, value4, .... ] 
# example: [ 1, 2, 3, 4, 5 ]

# only integers I gave 
x1 = [ 1, 2, 3, 4, 5 ]
print("x1 ka value : ", x1)
print("x1 ka type: ", type(x1))

# Only float values will also work
x2 = [ 1.1, 2.3, 3.5, 4.1, 5.7 ]
print("x2 ka value : ", x2)
print("x2 ka type: ", type(x2))

# only string bhi kaam krega 
x3 = [ "Aman", "Deepak", "Ghanashayam", "Niranjan" ]
print("x3 ka value : ", x3)
print("x3 ka type: ", type(x3))

# Boolean value bhi work krega
x4 = [ True, False ]
print("x4 ka value : ", x4)
print("x4 ka type: ", type(x4))

# Mixed bhi daal sakte hai
x5 = [ 1, 2.2, True, "Aman" ]
print("x5 ka value : ", x5)
print("x5 ka type: ", type(x5))

# list k under bhi list kaam krega 
x6 = [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]
print("x6 ka value : ", x6)
print("x6 ka type: ", type(x6))

# tuple and set bhi kaam krega 
x7 = [ (1,2), {3,4}, [1,5]]
print("x7 ka value : ", x7)
print("x7 ka type: ", type(x7))

# any data type use kr sakte 
x8 = [ 2+3j, 12, "Aman", 13.2, True, [1,2,3], (5,4,6), {9,10}, {1:"Aman", 2:"Deepak"}]
print("x8 ka value : ", x8)
print("x8 ka type: ", type(x8))

