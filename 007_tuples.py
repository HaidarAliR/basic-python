import sys
#type of 1D ARRAY: tuples, set, list

# tuples
a = (1,2,3,4,5,6)
#list (more efficent, less features)
b = [1,2,3,4,5,6]

# print(b)
#
# print(type(b))

print (sys.getsizeof(a))
print (sys.getsizeof(b))
print(dir('tuple'))
print(dir('list'))