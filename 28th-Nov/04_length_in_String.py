"""
String Length
===================
Python me strings ka length nikalna hai aapko to aap len() function use kr sakte hai
len() function wo string ka length return krta hai.

Example : 

x = "Deepak"
print(x)
Deepak
print(len(x))
6

x = "Aman"
print(x)
Aman
print(len(x))
4

x = "I am Aman and I am living in bangalore location"
print(x)
I am Aman and I am living in bangalore location
print(len(x))
47

x = "
Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications."
SyntaxError: unterminated string literal (detected at line 1)

x = """
Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications."""
print(x)

Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications.
print(len(x))
138

"""