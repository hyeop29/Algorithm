import java.io.*;
import java.util.*;
public class Main {
	static int arr[][];
	static int n, k, count, maxCount;
	static boolean visited[][];
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		
		arr = new int[n + 1][n + 1];
		visited = new boolean[n + 1][n + 1];
		for(int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j < n + 1; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		maxCount = 0;
		k = arr[x][y];
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < n + 1; j++) {
				if(arr[i][j] == k) {
					count = 0;
					bfs(i, j);
					maxCount = Math.max(maxCount, count);
				}
			}
		}
		System.out.print(maxCount);
	}
	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {x,y});
		
		int tx, ty, nx, ny;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			tx = now[0];
			ty = now[1];
			if(visited[tx][ty] == false) {
				visited[tx][ty] = true;
				count++;
				arr[tx][ty]--;
				for(int i = 0; i < 4; i++) {
					nx = tx + dx[i];
					ny = ty + dy[i];
					if(in_range(nx, ny) && visited[nx][ny] == false && arr[nx][ny] == k) {
						queue.add(new int[] {nx, ny});
					}
				}
			}
			

		}
		
	}
	private static boolean in_range(int x, int y) {
		return x > 0 && x <= n && y > 0 && y <= n;
	}
	

}
