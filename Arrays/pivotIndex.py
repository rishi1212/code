class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lengthOfArray = len(nums)
        for i in range(0,lengthOfArray):
            if(sum(nums[0:i]) == sum(nums[i+1:lengthOfArray])):
                return i
        return -1