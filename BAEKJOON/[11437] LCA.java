import java.io.*;
import java.util.*;
public class Main {
    static ArrayList<Integer> tree[];
    static int parent[], depth[];
    static boolean visited[];
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        tree = new ArrayList[n + 1];
        parent = new int[n + 1];
        depth = new int[n + 1];
        visited = new boolean[n + 1];
        for(int i = 1; i < n + 1; i++){
            tree[i] = new ArrayList<Integer>();
        }
        for(int i = 0; i < n - 1; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree[a].add(b);
            tree[b].add(a);
        }
        bfs(1);
//        System.out.println(Arrays.toString(parent));
//        System.out.println(Arrays.toString(depth));
        int m = Integer.parseInt(br.readLine());
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(findParent(a, b));
        }

    }
    public static void bfs(int index){
        Queue<Integer> queue = new LinkedList<>();
        int level = 1;
        int now_size = 1;
        int count = 0;

        visited[index] = true;
        queue.add(index);

        while(!queue.isEmpty()){
            int now_node = queue.poll();
            count++;

            for(int i : tree[now_node]){
                if(!visited[i]){
                    visited[i] = true;
                    parent[i] = now_node;
                    depth[i] = level;
                    queue.add(i);
                }
            }

            if(count == now_size){
                count = 0;
                now_size = queue.size();
                level++;
            }
        }
    }

    public static int findParent(int a, int b){
        if(depth[a] > depth[b]){
            int temp = b;
            b = a;
            a = temp;
        }
        while(depth[a] != depth[b]){
            b = parent[b];
        }
        while(a != b){
            a = parent[a];
            b = parent[b];
        }
        return a;
    }
}
