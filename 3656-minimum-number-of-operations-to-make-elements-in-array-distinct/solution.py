class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in seen:
                return ceil((i + 1) / 3)

            seen.add(num)

        return 0