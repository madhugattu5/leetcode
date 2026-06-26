from typing import List
import bisect

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = 0
        result = 0

        sorted_prefix = [0]
        
        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1
            
            idx = bisect.bisect_left(sorted_prefix, prefix)
            result += idx
            
            bisect.insort(sorted_prefix, prefix)
        
        return result