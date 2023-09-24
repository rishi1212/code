print ("Hello world")

nums = [1,2,3,4]

lengthOfArray = len(nums)
largestNumber = max(nums)
for i in range(0,lengthOfArray):
    if((nums[i]!=largestNumber) & (nums[i]*2 >= largestNumber)):
        print (nums.index(largestNumber))
