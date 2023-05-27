import java.io.*;
import java.util.*;
public class Main {
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	static int miro[][];
	static boolean visited[][];
	static int n;
	static int m;
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		miro = new int[n][m];
		visited = new boolean[n][m];
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			String temp = st.nextToken();
			
			for(int j = 0; j < m; j++) {
				miro[i][j] = Integer.parseInt(temp.substring(j, j + 1));
			}
		}
		bfs(0, 0);
		System.out.print(miro[n - 1][m - 1]);
	}
	private static void bfs(int x, int y) {
		Queue<int[]>queue = new LinkedList<>();
		queue.add(new int[] {x,y});
		
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			visited[now[0]][now[1]] = true;
			
			for(int i = 0; i < 4; i++) {
				int nx = now[0] + dx[i];
				int ny = now[1] + dy[i];
				if (in_range(nx, ny) && visited[nx][ny] == false && miro[nx][ny] == 1) {
					miro[nx][ny] = miro[nx][ny] + miro[now[0]][now[1]];
					queue.add(new int[] {nx, ny});
				}
			}
		}
	}
	private static boolean in_range(int x, int y) {
		return x < n && x >= 0 && y < m && y >= 0;
	}
}
