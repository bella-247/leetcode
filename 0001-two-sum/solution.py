class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        hash_map = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hash_map:
                return [hash_map[num2], i]
            else:
                hash_map[nums[i]] = i 
        return [-1,-1]
