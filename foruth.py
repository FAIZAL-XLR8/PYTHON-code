#type conversion from any datatype to bool
str1 = "alpha si "
str2 = ""
a = 0
b = 0.0
c = -1
print(bool(str1), type(str1)) #true
print(bool(str2), type(str2)) #false
print(bool(a), type(a)) #false
print(bool(b), type(b)) #false
print(bool(c), type(c)) #true
#there are 7 things which results in false
# 0, 0.0, "", '', {}, (), [], False
# a clear distinction in python compared to cpp
# that p/q form always results in float in python 
a = 12
b = 3
print(a/b)
print(type(a/b))