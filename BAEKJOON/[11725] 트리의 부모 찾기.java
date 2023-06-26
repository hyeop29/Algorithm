import java.io.*;
import java.util.*;
public class Main{
    static boolean visited[];
    static ArrayList<Integer> tree[];
    static int parent[];
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        parent = new int[n + 1];
        tree = new ArrayList[n + 1];
        visited = new boolean[n + 1];
        for(int i = 1; i < n + 1; i++){
            tree[i] = new ArrayList<>();
        }
        for(int i = 0; i < n - 1; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            tree[x].add(y);
            tree[y].add(x);
        }
        dfs(1);
        for(int i = 2; i < n + 1; i++){
            System.out.println(parent[i]);
        }
    }
    public static void dfs(int node){
        for(int i : tree[node]){
            if(!visited[i]){
                visited[i] = true;
                parent[i] = node;
                dfs(i);
            }
        }
    }
}
