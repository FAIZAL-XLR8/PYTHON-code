#tuples are ordered and unchangeable yaani no add or remove allowed
#  after intitalisation, it can allows duplicates
tuple1 = ("alpha",) #for a single element last me comma is needed for python
print(type(tuple1))
tuple2 = ("apple", "bananan", "alko")
print(tuple2)
tuple3 = tuple(("apple", "baba"))
print(type(tuple3))
print(tuple3)

#tuples indexing starts from 0 and len() takes lenght
print(len(tuple2))

#accessing tuples
tuple4 = ("alpha", "betta", "gama", "omega")
print(tuple4[-1])
