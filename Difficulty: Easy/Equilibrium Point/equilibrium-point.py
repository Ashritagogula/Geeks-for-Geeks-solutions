class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            total_sum -= arr[i]  # now total_sum is the right sum
            
            if left_sum == total_sum:
                return i  # equilibrium index found
            
            left_sum += arr[i]
        
        return -1  # no equilibrium index found
