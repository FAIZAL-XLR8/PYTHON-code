#list ka scene hai ye ki we can add elements of multiple datatype
#it is ordered(fllowss indexing), changeable(can append/pop elements)
#and allows duplicates
listings = [10, 11, 20]
print(listings)
#creating the lists with list constructor
lst = list(("apple", "guava", "archis")) #double brace always needed otherwise it will give error
print(lst)

#we can access the lists elements wth idx = 0 as start point
print(lst[0])
#we can have a subpart of a list
sublist = lst[0:2]
print(sublist)
#checking if an item exists in list
is_present  = bool('apple' in lst)

# #check if an item does not exist
not_present = bool('apple' not in lst)
print(not_present)
print(is_present)
print(lst[-3 : -1])