class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        total_count = 0

        freq = Counter()
        left_needs_count = [0] * n

        for i in range(n):
            num = nums[i]
            need = num * 2
            left_needs_count[i] = freq[need]
            freq[num] += 1

        for i in range(n):
            need = nums[i] * 2
            left_needs = left_needs_count[i]
            total_needs = freq[need]

            if nums[i] == need:
                total_needs -= 1

            right_needs = total_needs - left_needs

            total_count += (left_needs * right_needs)


        return total_count % mod
