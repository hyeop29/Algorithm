import java.io.*;
import java.util.*;
public class Main {
	static int n, m, count;
	static int papper[][];
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		papper = new int[n][m];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				papper[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int bigDrawing = 0;
		int answer = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(papper[i][j] == 1) {
					answer++;
					count = 0;
					bfs(i, j);
					if(bigDrawing < count) {
						bigDrawing = count;
					}
				}
			}
		}
		System.out.println(answer);
		System.out.println(bigDrawing);
	}
	private static void bfs(int x, int y) {
		Queue<int []> queue = new LinkedList<>();
		papper[x][y]--;
		queue.add(new int[] {x, y});
		
		int tx, ty, nx, ny;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			tx = now[0];
			ty = now[1];
			count++;
			for(int i = 0; i < 4; i++) {
				nx = tx + dx[i];
				ny = ty + dy[i];
				if(in_range(nx, ny) && papper[nx][ny] == 1) {
					papper[nx][ny]--;
					queue.add(new int[] {nx, ny});
				}
			}
		}
	}
	private static boolean in_range(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}
}
