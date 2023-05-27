import java.io.*;
import java.util.*;
public class Main {
	static char video[][];
	static int n, m, count;
	static ArrayList<Integer> size;
	static boolean visited[][];
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		String str;
		char temp[] = new char[n];
		video = new char[m][n];
		for(int i = 0; i < m; i++) {
			str = br.readLine();
			temp = str.toCharArray();
			for(int j = 0; j < n; j++) {
				video[i][j] = temp[j];
			}
		}
		int answer = 0;
		visited = new boolean[m][n];
		size = new ArrayList<>();
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if (video[i][j] == '#') {
					count = 0;
					bfs(i, j);
					answer++;
					size.add(count);
					//System.out.println(Arrays.deepToString(video));
				}
			}
		}
		Collections.sort(size);
		System.out.println(answer);
		System.out.print(size.get(answer - 1));
	}
	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {x, y});
		
		int tx, ty, nx, ny;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			tx = now[0];
			ty = now[1];
			if(visited[tx][ty] == false) {
				visited[tx][ty] = true;
				video[tx][ty] = '.';
				count++;
				
				for(int i = 0; i < 4; i++) {
					nx = tx + dx[i];
					ny = ty + dy[i];
					if(in_range(nx, ny) && visited[nx][ny] == false && video[nx][ny] == '#') {
						queue.add(new int[] {nx, ny});
					}
				}
			}

		}
		
	}
	private static boolean in_range(int x, int y) {
		return x >= 0 && x < m && y >= 0 && y < n;
	}
}
