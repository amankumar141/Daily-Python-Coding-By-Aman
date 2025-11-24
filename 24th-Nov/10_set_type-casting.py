"""
8) set() --> set data type me convert krne k liye 

Examples : 
## jab aap tuple value ko set() me send kr rahe hai
x = set( (1,2,3) )
x
{1, 2, 3}
type(x)
<class 'set'>

## jab aap list value ko set() me send kr rahe hai 
x = set( [1,2,3] )
x
{1, 2, 3}
type(x)
<class 'set'>

## Jab aap set value ko set() me send kr rahe hai
x = set( {1,2,3} )
x
{1, 2, 3}
type(x)
<class 'set'>


## jab aap dictionary value ko set() me send kr rahe hai to
x = set( {1:"Aman", 2:"Deepak"} )
x
{1, 2}
type(x)
<class 'set'>

# Exception case/Feature of sets (Jab aap duplicate value send kr rahe hai set() me)
x = set( {1:"Aman", 2:"Deepak", 1:"Niranjan", 3:"Abhi", 2:"Ghanashayam"} )
x
{1, 2, 3}
type(x)
<class 'set'>

"""