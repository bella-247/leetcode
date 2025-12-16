class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        lines = {"electronics", "grocery", "pharmacy", "restaurant"}

        n = len(code)
        valids = [
            (businessLine[i], code[i])
            for i in range(n)
            if code[i] and 
            isActive[i] and 
            businessLine[i] in lines and 
            all(c.isalnum() or c == "_" for c in code[i])
        ]

        valids.sort()

        return [c for _, c in valids]

        