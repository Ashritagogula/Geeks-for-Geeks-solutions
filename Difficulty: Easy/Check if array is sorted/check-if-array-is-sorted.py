class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        if(arr == sorted(arr)):
            return True
        else:
            return False