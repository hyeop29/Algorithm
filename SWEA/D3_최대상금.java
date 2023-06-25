import java.io.*;
import java.util.*;
class Solution
{
	static int answer;
    static boolean visited[][];
    public static void main(String args[]) throws IOException{
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int count, arr[], depth;
        int T = Integer.parseInt(br.readLine());
        String money;

        for(int test_case = 1; test_case <= T; test_case++){
            st = new StringTokenizer(br.readLine());
            money = st.nextToken();
            count = Integer.parseInt(st.nextToken());
            depth = 0;
            visited = new boolean[count + 1][1000000];
            answer = 0;
            prize(money.toCharArray(), depth, count);
            System.out.println("#" + test_case + " " + answer);
        }
    }
    public static void prize(char[] money, int depth, int count){
        if(depth == count){
            answer = answer > Integer.valueOf(String.valueOf(money)) ? answer : Integer.valueOf(String.valueOf(money));
            return;
        }
        for(int i = 0; i < money.length - 1; i++){
            for(int j = i + 1; j < money.length; j++){
                char tempMoney[] = swap(money, i, j);
                // 중복 연산을 줄이기 위해 boolean visited[][] 사용
                if(!visited[depth + 1][Integer.valueOf(String.valueOf(tempMoney))]){
                    visited[depth + 1][Integer.valueOf(String.valueOf(tempMoney))] = true;
                    prize(tempMoney, depth + 1, count);
                }
            }
        }
    }

    public static char[] swap(char[] money, int i, int j){
        char cloneMoney[] = money.clone();
        char temp = cloneMoney[i];
        cloneMoney[i] = cloneMoney[j];
        cloneMoney[j] = temp;
        return cloneMoney;
    }
}
