class Solution {
    public int binarysearch(int[] arr, int k) {
        int low = 0, high = arr.length - 1;
        int result = -1; // store index of k if found
        
        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (arr[mid] == k) {
                result = mid;   // store index
                high = mid - 1; 
            } 
            else if (arr[mid] < k) {
                low = mid + 1;
            } 
            else {
                high = mid - 1;
            }
        }
        
        return result;
    }
}
