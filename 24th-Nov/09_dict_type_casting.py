"""
7) dict() --> dictionary data type me convert krne k liye
dictionary ko humlog key-value pair me likhte hai aur seperate colon se krte hai
x = { 1:"Aman", 2:"Deepak" }
# only key print krna hai mujhe
x.keys()
dict_keys([1, 2])

# only value print krna hai mujhe
x.values()
dict_values(['Aman', 'Deepak'])

# Key and Values dono pair me print krna hai
x.items()
dict_items([(1, 'Aman'), (2, 'Deepak')])


## jab aap tuple value dict() me pass krte hai tph error aata hai
x = dict( (10,20,30) )
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    x = dict( (10,20,30) )
TypeError: cannot convert dictionary update sequence element #0 to a sequence

## jab aap list value dict() me pass krte hai to error aata hai
x=dict([10,20,30])
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    x=dict([10,20,30])
TypeError: cannot convert dictionary update sequence element #0 to a sequence

## jab aap set value ko dict() me pass krte hai to error aata hai
x = dict({10,20,30})
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    x = dict({10,20,30})
TypeError: cannot convert dictionary update sequence element #0 to a sequence


## jab aap dictionary value ko dict() me pass kr rahe hai to error nahi aayega 
qki dictionary ka concept hi hai key-velue pair me data isliye only dictionary ko support krta hai
x = dict({1:"Aman", 2:"Deepak"})
x
{1: 'Aman', 2: 'Deepak'}
type(x)
<class 'dict'>

"""