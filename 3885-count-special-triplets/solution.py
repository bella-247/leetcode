class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        total_count = 0

        counter = Counter()
        left_needs_counter = Counter()

        for i, num in enumerate(nums):
            need = num * 2
