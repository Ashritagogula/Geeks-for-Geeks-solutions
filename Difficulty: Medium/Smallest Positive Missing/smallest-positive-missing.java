class Solution {
    public int missingNumber(int[] arr) {
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
            // Place each number at its correct index (arr[i] = i+1)
            while (arr[i] > 0 && arr[i] <= n && arr[arr[i] - 1] != arr[i]) {
                int temp = arr[arr[i] - 1];
                arr[arr[i] - 1] = arr[i];
                arr[i] = temp;
            }
        }
        
        // Find first index where arr[i] != i + 1
        for (int i = 0; i < n; i++) {
            if (arr[i] != i + 1)
                return i + 1;
        }
        
        // If all are in correct place
        return n + 1;
    }
}
