print ("Hello world")

aList = [1,7,3,6,5,6]

lengthOfArray = len(aList)




print("the solution")
for i in range(0,lengthOfArray):
    # print (aList[0:i] )
    # print("sum is equal to: "+ str(sum(aList[0:i])))
    # print (aList[i+1:lengthOfArray] )
    # print("sum is equal to: " + str(sum(aList[i:lengthOfArray])))
    if(sum(aList[0:i]) == sum(aList[i+1:lengthOfArray])):
        print (i)
    else:
        print ("-1")