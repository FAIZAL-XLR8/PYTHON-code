str = "a"
print(str)
print(ord(str))

"""
here we need to note that 
ord is for the ascii values but the 
chr is for the character changes
like chr(65) will result in A
"""
print("here is the use of chr", "hello ")
print(chr(65))
aizen = "aizen"
print(aizen[0], aizen[2], aizen[4])

"""
slicing of the string

variable_name[start_idx : end_idx : step] (end_idx not included)
step is completely optional and by default taken as 1

start_idx starts from 0 and
end idx can also be represnted as -1 to -n from right to left
-4 -3 -2 -1 

 """
aizen = "aizen"

print(aizen[-4 : -1])
