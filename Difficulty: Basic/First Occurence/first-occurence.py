class Solution:
    def firstOccurence(self, txt, pat):
        n = len(txt)
        m = len(pat)

        # Loop through txt, check each substring of length m
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                return i  # Found the first occurrence
        return -1 