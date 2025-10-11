class Solution {
    boolean isBinary(String s) {
        // Your code here
        for(int i = 0; i < s.length(); i++){
            char checkIndex = s.charAt(i);
            if(checkIndex != '1' && checkIndex != '0'){
                return false;
            }
        }
        return true;
    }
}