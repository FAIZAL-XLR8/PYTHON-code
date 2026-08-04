lst = ['apple', 'guava', 'banana']
for item in lst:
    print(item)
    # if item == 'banana':
    #     break
else: #else statement in for loop signifies that if loop ends this 
    #else block statment will execute(only when no break/return statement
    #takes uh out of loop)
    print("Work was done and loop was excuted!")
for x in range(2,10, 3):
    #2 means start from 2,  10 is excluded and steps are of 3
    # steps are optional and if no start given then 0 is default
    # start --> [2, 10) 
    print(x)
