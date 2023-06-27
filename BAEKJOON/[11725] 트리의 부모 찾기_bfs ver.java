import java.io.*;
import java.util.*;
public class Main {
    static boolean visited[];
    static int parent[];
    static ArrayList<Integer> tree[];
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        tree = new ArrayList[n + 1];
        for(int i = 1; i < n + 1; i++){
            tree[i] = new ArrayList<>();
        }
        visited = new boolean[n + 1];
        parent = new int[n + 1];

        // Tree의 간선은 node 개수 - 1
        for(int i = 0; i < n - 1; i++){
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            tree[v1].add(v2);
            tree[v2].add(v1);
        }
        bfs(1);

        for(int i = 2; i < n + 1; i++){
            System.out.println(parent[i]);
        }
    }
    public static void bfs(int node){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        int now;

        while(!queue.isEmpty()){
            now = queue.poll(); //poll vs remove : remove는 큐가 비어 있는 경우
            for(int temp : tree[now]){
                if(!visited[temp]){
                    parent[temp] = now;
                    visited[temp] = true;
                    bfs(temp);
                }
            }
        }
    }
}
