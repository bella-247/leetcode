
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1

        slow = 0
        count, curr = 1, chars[0]
        for fast in range(1,n):
            if chars[fast] != curr:
                chars[slow] = curr
                slow += 1
                if count > 1:
                    digits = int(log10(count)) + 1 # count length 
                    chars[slow: slow + digits] = list(str(count))
                    slow += digits

                count = 0
                curr = chars[fast]

            count += 1

        chars[slow] = curr
        slow += 1
        if count > 1:
            digits = int(log10(count)) + 1
            chars[slow: slow + digits] = list(str(count))
            slow += digits

        return slow
