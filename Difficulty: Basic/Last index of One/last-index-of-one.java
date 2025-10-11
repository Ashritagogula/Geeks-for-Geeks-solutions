// User function Template for Java

class Solution {
    public int lastIndex(String s) {
        //he asked last index, so loop from last
        for(int i = s.length()-1 ;i>=0; i--){
            if(s.charAt(i) == '1'){
                return i;
            }
        }
        return -1;
    }
}