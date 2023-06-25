import java.io.*;
import java.util.*;
class Solution
{
public static void main(String args[]) throws IOException{
        //System.setIn(new FileInputStream("res/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = 10;
        int answer[] = new int[T + 1];
        for(int test_case = 1; test_case < T + 1; test_case++){
            int n = Integer.parseInt(br.readLine()); // 건물개수 n개 입력 받기
            st = new StringTokenizer(br.readLine());
            int arr[] = new int[n];
            for(int i = 0; i < n; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            answer[test_case] = rightOfView(n, arr);
        }
        for(int i = 1; i < T + 1; i++){
            System.out.println("#"+ i + " " + answer[i]);
        }
    }
    public static int rightOfView(int n, int[] arr){
        int total = 0, gap = 0;
        int check, maxValue;
        int temp[] = {-2, -1, 1, 2};
        for(int i = 2; i < n - 2; i++){
            maxValue = Integer.MAX_VALUE;
            check = 0;
            for(int j = 0; j < 4; j++){
                gap = arr[i] - arr[i + temp[j]];
                if(gap <= 0){
                    check = 1;
                    break;
                }
                if(maxValue > gap){
                    maxValue = gap;
                }
            }
            if(check == 0){
                total += maxValue;
            }
        }
        return total;
    }
}
