import java.io.*;
import java.util.*;
public class Main {
	static int r, c;
	static char miro[][], Jmiro[][];
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	static boolean fire, escape, Jvisited[][], Fvisited[][];
	static Queue<int []> queue1, queue2;
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		miro = new char[r][c];
		Jmiro = new char[r][c];
		Jvisited = new boolean[r][c];
		Fvisited = new boolean[r][c];
		queue1 = new LinkedList<>();
		queue2 = new LinkedList<>();
		
		for(int i = 0; i < r; i++) {
			miro[i] = br.readLine().toCharArray();
			Jmiro[i] = miro[i].clone();
		}
		int answer = 0;
		while(fire == false && escape == false) {
			answer++;
			for(int i = 0; i < r; i++) {
				for(int j = 0; j < c; j++) {
					if(miro[i][j] == 'F' && Fvisited[i][j] == false) {
						queue1.add(new int[] {i, j});
					}
				}
			}
			Fbfs();

			for(int i = 0; i < r; i++) {
				for(int j = 0; j < c; j++) {
					if(Jmiro[i][j] == 'J') {
						Jvisited[i][j] = true;
						queue2.add(new int[] {i, j});
					}
				}
			}
			Jbfs();
		}
		
		if(fire) {
			System.out.print("IMPOSSIBLE");
		}
		else {
			System.out.print(answer);
		}
		
	}
	private static void Fbfs() {
		int tx, ty, nx, ny;
		while(!queue1.isEmpty()) {
			int now[] = queue1.poll();
			tx = now[0];
			ty = now[1];
			Fvisited[tx][ty] = true;
			for(int i = 0; i < 4; i++) {
				nx = tx + dx[i];
				ny = ty + dy[i];
				if(in_range(nx, ny) && miro[nx][ny] != '#' && Fvisited[nx][ny] == false) {
					miro[nx][ny] = 'F';
				}
			}
		}
	}
	private static boolean in_range(int x, int y) {
		return x >= 0 && x < r && y >= 0 && y < c;
	}
	private static void Jbfs() {
		int tx, ty, nx, ny;
		boolean move = false;
		while(!queue2.isEmpty()) {
			int now[] = queue2.poll();
			tx = now[0];
			ty = now[1];
			Jmiro[tx][ty] = '.';
			for(int i = 0; i < 4; i++) {
				nx = tx + dx[i];
				ny = ty + dy[i];
				if(in_range(nx, ny) && miro[nx][ny] != 'F' && miro[nx][ny] != '#' && Jvisited[nx][ny] == false) {
					Jmiro[nx][ny] = 'J';
					move = true;
				}
				else if(!in_range(nx, ny)) {
					escape = true;
					queue2.clear();
					break;
				}
			}
			
		}
		if(!move && !escape) {
			fire = true;
		}
	}		
		
}
