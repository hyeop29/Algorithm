import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		boolean visited[] = new boolean[100001];
		Queue<int []> queue = new LinkedList<>();
		visited[n] = true;
		queue.add(new int[] {n , 0});
		
		int dx[] = {-1, 1};
		int nx;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			if (now[0] == k) {
				System.out.print(now[1]);
				queue.clear();
				break;
			}
			for(int i = 0; i < 3; i++) {
				if(i == 2) {
					nx = 2 * now[0];
				}
				else {
					nx = now[0] + dx[i];
				}
				if(in_range(nx) && visited[nx] == false) {
					visited[nx] = true;
					queue.add(new int[] {nx, now[1] + 1});
				}
			}
			
		}
		
	}

	private static boolean in_range(int x) {
		return x >= 0 && x <= 100000;
	}
}
