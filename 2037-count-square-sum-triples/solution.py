class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = [i ** 2 for i in range(1, n + 1)]

        for i in range(n):
            target = squares[i]
            left, right = 0, n - 1

            while left < right:
                summ = squares[left] + squares[right]
                if summ == target:
                    count += 2
                    left += 1
                    right -= 1

                elif summ > target:
                    right -= 1
                
                else: # summ < target
                    left += 1

        return count