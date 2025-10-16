class Solution:
    def reverseingroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            arr[i:i+k] = arr[i:i+k][::-1]
        return arr
