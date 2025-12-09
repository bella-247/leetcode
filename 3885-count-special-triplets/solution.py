
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        total_count = 0

        counter = Counter()
        left_needs_counter = Counter()

        for i, num in enumerate(nums):
            need = num * 2
            left_needs_counter[i] = counter[need]
            counter[num] += 1

        for index, left_needs in left_needs_counter.items():
            need = nums[index] * 2
            total_needs = counter[need]

            # in the case of zero we need to remove 1 from the total needs cause current zero is also considered and we don't want that 
            if nums[index] == 0: