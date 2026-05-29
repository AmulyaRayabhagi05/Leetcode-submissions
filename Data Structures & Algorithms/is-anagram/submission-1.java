class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charS= s.toCharArray();
        char[] charT= t.toCharArray();

        Arrays.sort(charS);
        Arrays.sort(charT);
        if(charS.length != charT.length){
            return false;
        }
        return Arrays.equals(charS, charT);
    }
}
