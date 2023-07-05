import java.io.*;
import java.util.*;
public class Main {
    static long tree[];
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int treeHeight = 0;
        int length = n;
        boolean maxleft = true;

        // n을 바탕으로 tree의 높이 구하기
        while (length != 0) {
            if (length > 1 && length % 2 != 0) {
                maxleft = false;
            }
            length /= 2;
            treeHeight++;
        }
        if (maxleft == true) {
            treeHeight--;
        }
        // 높이를 바탕으로 tree size 결정, double to int
        int treeSize = (int) Math.pow(2, treeHeight + 1);
        tree = new long[treeSize];
        // 배열 값이 입력될 tree 위치
        int leftNodeStartIndex = treeSize / 2;
        for (int i = 0; i < n; i++) {
            tree[leftNodeStartIndex + i] = Long.parseLong(br.readLine());
        }
        // 전체 노드를 완성한다.
        setTree(treeSize - 1);
        // System.out.println(Arrays.toString(tree));
        for(int i = 0; i < m + k; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if(a == 1){
                modefiedTree(leftNodeStartIndex + b - 1, c);
                // System.out.println(Arrays.toString(tree));
            }
            else{
                sectionOfSum(leftNodeStartIndex + b - 1, leftNodeStartIndex + (int)c - 1);
            }
        }
    }

    public static void setTree(int index){
        while(index > 1){
            tree[index/2] += tree[index];
            index--;
        }
    }

    public static void modefiedTree(int index, long value){
        long diff = value - tree[index];
        tree[index] = value;
        while(index > 1){
            tree[index / 2] += diff;
            index /= 2;
        }
    }

    public static void sectionOfSum(int start, int end){
        long sum = 0;
        while(start <= end){
            // System.out.println("start: " + start + "end :" + end);
            if(start % 2 == 1){
                sum += tree[start];
            }
            if(end % 2 == 0){
                sum += tree[end];
            }
            start = (start + 1) / 2;
            end = (end - 1) / 2;
        }
        System.out.println(sum);
    }
}
