class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            c=target-nums[i]
            if c in nums[i+1:]:
                c_index = nums.index(c, i + 1)
                return[i,c_index]
        return[]
        