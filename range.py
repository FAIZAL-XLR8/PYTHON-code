a ="archedemis"
def isVowel(s):
    return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'

for i in range(0, len(a),1):
    if (isVowel(a[i])):
        print(a[i], "is Vowel")
    else :
        print (a[i], "is Consonant!")
#