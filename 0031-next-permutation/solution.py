class Solution:
    def reverse(self, nums, start, end):
        i, j = start, end - 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        index = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            self.reverse(0, n)

        else:
            self.reverse(nums, index + 1, n)
            nxt = bisect_right(nums, nums[index], lo= index + 1, hi = n)
            nums[index], nums[nxt] = nums[nxt], nums[index]