import java.util.*;
class Solution {
    public int solution(int N, int number) {
        if (number == N) {
            return 1;
        }
        List<Set<Integer>> dp = new ArrayList<>();
        for(int i = 0; i < 9; i++){
            dp.add(new HashSet<>());
        }
        // 1개 표현할 수 있는 수는 N 하나 뿐.
        dp.get(1).add(N);
        for(int i = 2; i < 9; i++){
            Set<Integer> d = dp.get(i);
            for(int j = 1; j < i; j++){
                for(int pre : dp.get(j)){
                    for(int next : dp.get(i - j)){
                        d.add(pre + next);
                        d.add(pre - next);
                        d.add(pre * next);
                        if(next != 0){
                            d.add(pre / next);
                        }
                    }
                }
            }
            d.add(Integer.parseInt(String.valueOf(N).repeat(i)));
            for(int temp : d){
                if (temp == number){
                return i;
                }
            }
        }
        return -1;
    }   
}
