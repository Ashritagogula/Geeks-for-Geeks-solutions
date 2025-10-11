class Solution {
    int maxSum = Integer.MIN_VALUE;

    int findMaxSum(Node root) {
        helper(root);
        return maxSum;
    }

    int helper(Node node) {
        if (node == null) return 0;
        int left = Math.max(0, helper(node.left));
        int right = Math.max(0, helper(node.right));
        maxSum = Math.max(maxSum, left + right + node.data);
        return node.data + Math.max(left, right);
    }
}
