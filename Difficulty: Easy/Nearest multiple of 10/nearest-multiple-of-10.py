class Solution:
    def roundToNearest(self, s): 
        # Handle single-digit input directly
        if len(s) == 1:
            n = int(s)
            if n < 5:
                return "0"
            elif n > 5:
                return "10"
            else:
                return "0"
        
        last_digit = int(s[-1])   # Get the last digit
        prefix = s[:-1]           # All digits except the last one

        if last_digit < 5:
            # Round down → just replace last digit with 0
            return prefix + "0"
        elif last_digit > 5:
            # Round up → add 1 to the prefix
            prefix_list = list(prefix)
            i = len(prefix_list) - 1
            while i >= 0 and prefix_list[i] == '9':
                prefix_list[i] = '0'
                i -= 1
            if i >= 0:
                prefix_list[i] = str(int(prefix_list[i]) + 1)
            else:
                prefix_list.insert(0, '1')
            return "".join(prefix_list) + "0"
        else:  # last_digit == 5 → choose smaller multiple
            return prefix + "0"
