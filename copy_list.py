#we can copy lists
lst1 = list((10, 20, 30, 100))
print(lst1)
lst2 = lst1.copy()
print(lst2)

#we can use list's own constructor
lst3 = list(lst1)
print(lst3)

#slicicing method 
lst4 = lst3[:]
print(lst4)