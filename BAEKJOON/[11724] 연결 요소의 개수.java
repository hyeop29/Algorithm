import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		ArrayList<Integer> arr[] = new ArrayList[n + 1];
		boolean visited[] = new boolean[n + 1]; // boolean 초기값은 false
		int answer = 0;
		for(int i = 1; i < n + 1; i++) {
			arr[i] = new ArrayList<Integer>();
		}
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(bf.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			arr[u].add(v);
			arr[v].add(u);
		}
		for(int i = 1; i < n + 1; i++) {
			if (visited[i] == false) {
				dfs(i, visited, arr);
				answer++;
			}
		}
		System.out.print(answer);
	}
	private static void dfs(int v, boolean[] visited, ArrayList<Integer>[] arr) {
		visited[v] = true;
		int temp = 0;
		for(int i = 0; i < arr[v].size(); i++) {
			temp = arr[v].get(i);
			if (visited[temp] == false) {
				dfs(temp, visited, arr);
			}
		}
	}
}
