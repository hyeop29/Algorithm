import java.io.*;
import java.util.*;
public class Main {
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	static int[] check;
	static boolean Bipartite;
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		// testcase 입력 받기
		int k = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			int v = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			// 필요한 항목 초기화
			graph = new ArrayList[v + 1];
			visited = new boolean[v + 1];
			check = new int[v + 1];
			Bipartite = true;
			
			for(int j = 1; j < v + 1; j++) {
				graph[j] = new ArrayList<>();
			}
			// graph 값 담아주기
			for(int j = 0; j < e; j++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				
				graph[start].add(end);
				graph[end].add(start);
			}
			
			for(int j = 1; j < v + 1; j++) {
				if (!visited[j]) {
					dfs(j);
				}
				if (!Bipartite) {
					bw.write("NO\n");
					break;
				}
			}
			if (Bipartite) {
				bw.write("YES\n");
			}
		}
		bw.flush();
		bw.close();
	}
	private static void dfs(int node) {
		visited[node] = true;
		for(int n : graph[node]) {
			if(!visited[n]) {
				check[n] = (check[node] + 1) % 2;
				dfs(n);
			}
			else {
				if (check[n] == check[node]) {
					Bipartite = false;
					break;
				}
			}
		}
	}
}
