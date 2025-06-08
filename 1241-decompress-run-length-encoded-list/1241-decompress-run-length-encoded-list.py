from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # This will hold our decompressed result
        decompressed: List[int] = []
        
        
        for i in range(0, len(nums), 2): #start=0:,  stop=len(nums), step=2: jump in increments of 2
            freq = nums[i]        
            val  = nums[i + 1]    
            
            # extend is another function like append, but it can take entire list at a time
            decompressed.extend([val] * freq)
        
        return decompressed


