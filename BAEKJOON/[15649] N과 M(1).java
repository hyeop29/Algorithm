import java.io.*;
import java.util.*;

public class Main {
    static boolean visited[];
    static int n, m, arr[];
    static BufferedWriter bw;
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new boolean[n + 1];
        arr = new int[m];

        find(arr, 0);
        bw.flush();
        bw.close();
    }

    private static void find(int[] arr, int index) throws IOException {
        if(index == m){
            for(int i = 0; i < m; i++){
                bw.write(arr[i] + " ");
            }
            bw.write("\n");
            return;
        }
        for(int i = 1; i < n + 1; i++){
            if(!visited[i]){
                visited[i] = true;
                arr[index] = i;
                find(arr, index + 1);
                visited[i] = false;
            }
        }
    }
}
