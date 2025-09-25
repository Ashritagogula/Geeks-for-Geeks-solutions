class Solution {
    public static double posAverage(int[] arr) {
        int sum = 0, count = 0;
        for (int num : arr) {
            if (num >= 0) {   // check non-negative
                sum += num;
                count++;
            }
        }
        if (count == 0) return 0.0;  // no non-negative numbers
        return (double) sum / count;
    }
}
