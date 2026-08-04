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


#insertion at a specific index
lst.insert(1, 'faizal')
print(lst)
# insert at lst position
lst.append("Ali")
print(lst)
#pop at specific idx --> if no idx pops from behind
lst.pop(2)
print(lst)
#remove the specific value from this list if multiple exists pop the first occurence
lst.remove('archis')

#to append one entire list into another use --> list1.extend(list2) -> o/p = [lis1_elements, list2_elements]
# lst.extend(listings) 
print(lst)

# sorting in descending order only if elements are of same type
lst.sort(reverse = True)

