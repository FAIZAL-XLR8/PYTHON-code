#since tuples cant be updated/immutable we do it by converting into a list
tuple1 = ("a", "b", "c")
print(tuple1)
list1 = list(tuple1)
list1.append("d")
tuple1 = tuple(list1)
print(tuple1)

#adding two tuples
tuple2 = tuple(("alpha", "beta")) #always two braces
tuple3 = tuple1 + tuple2
print(tuple3)

#unpacking a tuple
(x, y, z, a, b, c) = tuple3
print(x, y, z, a, b, c)
#unpacking a list
[x, y, z, a] = list1
print(x, y, z, a)

