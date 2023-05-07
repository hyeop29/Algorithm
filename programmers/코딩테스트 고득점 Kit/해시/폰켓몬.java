import java.util.*;

class Solution{
    public int solution(int[] nums){
        int max_P = nums.length / 2;
        
        HashSet<Integer> set = new HashSet<>();
        for(int n : nums){
            set.add(n);
        }
        if (max_P > set.size()){
            return set.size();
        }
        else{
            return max_P;
        }
    }
}
