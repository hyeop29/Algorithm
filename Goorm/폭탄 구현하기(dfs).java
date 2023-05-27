import java.io.*;
import java.util.*;
public class Main {
	static int map[][];
	static int n;
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		map = new int[n + 1][n + 1];
		int x, y;
		for(int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			dfs(x, y);
		}
		int answer = 0;
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < n + 1; j++) {
				answer += map[i][j];
			}
		}
		System.out.print(answer);
	}
	private static void dfs(int x, int y) {
		int nx, ny;
		map[x][y]++;
		for(int i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			if(in_range(nx, ny)) {
				map[nx][ny]++;
			}
		}
		
	}
	private static boolean in_range(int x, int y) {
		return x > 0 && x <= n && y > 0 && y <= n;
	}
}
