class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
   
        for j in range(n):
            if nums[i] == nums[j]:
                continue
            
            i += 1
            nums[i] = nums[j]

        return i + 1

