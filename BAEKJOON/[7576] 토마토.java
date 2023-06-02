import java.io.*;
import java.util.*;
public class Main {
	static int n, m, count, tomato[][];
	static boolean visited[][];
	static Queue<int[]> queue;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	public static void main(String args[])  throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		tomato = new int[n][m];
		visited = new boolean[n][m];
		count = 0;
		queue = new LinkedList<>();
		int orign = 0;
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m;  j++) {
				tomato[i][j] = Integer.parseInt(st.nextToken());
				if(tomato[i][j] == 0) {
					count++;
				}
				else if(tomato[i][j] == 1) {
					visited[i][j] = true;
					orign++;
					queue.add(new int[] {i, j});
				}
			}
		}
		bfs();
		int total = orign + count;
		int max = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(max < tomato[i][j]){
					max = tomato[i][j];
				}
				if(tomato[i][j] > 0){
					total--;
				}
			}
		}
		if(count == 0){
			System.out.print(0);
		}
		else if(total == 0){
			System.out.print(max - 1);
		}
		else{
			System.out.print(-1);
		}
	}
	private static void bfs(){
		int tx, ty, nx, ny, now[];
		while (!queue.isEmpty()){
			now = queue.poll();
			tx = now[0];
			ty = now[1];
			for(int i = 0; i < 4; i++){
				nx = tx + dx[i];
				ny = ty + dy[i];
				if(in_range(nx, ny) && visited[nx][ny] == false && tomato[nx][ny] == 0){
					visited[nx][ny] = true;
					tomato[nx][ny] = tomato[tx][ty] + 1;
					queue.add(new int[] {nx, ny});
				}
				else if(in_range(nx, ny) && visited[nx][ny] == true){
					if(tomato[nx][ny] > tomato[tx][ty] + 1){
						tomato[nx][ny] = tomato[tx][ty] + 1;
						queue.add(new int[] {nx, ny});
					}
				}
			}
		}
	}
	private static boolean in_range(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}
}
