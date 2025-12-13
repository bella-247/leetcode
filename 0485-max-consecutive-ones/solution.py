class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            else:
                length = 0

            longest = max(longest, length)

        return longest