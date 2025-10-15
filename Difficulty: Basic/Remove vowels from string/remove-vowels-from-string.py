class Solution:
    def removeVowels(self, s):
        vowels = set('aeiou')
        result = ''
        for c in s:
            if c not in vowels:
                result += c
        return result
