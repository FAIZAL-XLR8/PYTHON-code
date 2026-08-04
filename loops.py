# lst = ['apple', 'guava', 'banana']
# for item in lst:
#     print(item)
#     # if item == 'banana':
#     #     break
# else: #else statement in for loop signifies that if loop ends this 
#     #else block statment will execute(only when no break/return statement
#     #takes uh out of loop)
#     print("Work was done and loop was excuted!")
# for x in range(2,10, 3):
#     #2 means start from 2,  10 is excluded and steps are of 3
#     # steps are optional and if no start given then 0 is default
#     # start --> [2, 10) 
#     print(x)
# #simple hai
# num1 = int(input("Enter the first value : "))
# num2 = int(input("Enter the second value : "))
# if num1 > num2 :
#     print("One wins")
# elif (num1 == num2):
#     print("Draw occured!")
# else:
#     print("Two wins!")

#while loops
# i = 1
# sum1 = 0 
# sum2 = 9
# while (i < 10) :
#     if i % 2 == 0:
#         sum1 += i
#     else :
#         sum2 += i
#     i+= 1
# else :
#     print("This while loop over")
# print(sum1, "sum2 is", sum2)


#iterating over characters in reverse order in a string
a = 'alphaismybrother'

for i in range(len(a) - 1, -1, -1): #end has to be -1 because to acess that and steps is -1 because we are decreasing
    print (i)
else :
    print("done")
