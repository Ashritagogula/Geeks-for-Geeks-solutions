// User function template for Java

class Solution {
    static String conRevstr(String S1, String S2) {
        // code here
       String res =  S1.concat(S2);
       String reversed = new StringBuilder(res).reverse().toString();
       return reversed;
    }
}


















