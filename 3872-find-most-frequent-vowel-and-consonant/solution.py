class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a" : 0,"e" : 0, "i" : 0, "o" : 0, "u" : 0}
        consonants = Counter()

        max_vowel_freq = 0
        max_cons_freq = 0

        for c in s:
            if c in vowels:
                vowels[c] += 1
                max_vowel_freq = max(max_vowel_freq, vowels[c])

            else:
                consonants[c] += 1
                max_cons_freq = max(max_cons_freq, consonants[c])

        return max_vowel_freq + max_cons_freq
