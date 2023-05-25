import java.io.*;
import java.util.*;
public class Main {
	static int n;
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		int park[][] = new int [n + 1][n + 1];
		int temp_park[][] = new int [n + 1][n + 1];
		
		int count = 0;
		int dx[] = {-1, 1, 0, 0};
		int dy[] = {0, 0, -1, 1};
		StringTokenizer st;
		for(int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j< n + 1; j++) {
				park[i][j] = Integer.parseInt(st.nextToken());
				if(park[i][j] > 0) {
					count++;
				}
			}
		}
		int nx, ny;
		int answer = 0;
		int temp;
		while (count > 0) {
			for(int i = 1; i < n + 1; i++) {
				for(int j = 1; j < n + 1; j++) {
					if(park[i][j] > 0) {
						temp = 0;
						for(int k = 0; k < 4; k++) {
							nx = i + dx[k];
							ny = j + dy[k];
							if(in_range(nx,ny) && park[nx][ny] <= 0) {
								temp++;
							}
						}
						temp_park[i][j] = park[i][j] - temp;
						if(temp_park[i][j] <= 0) {
							count--;
						}
						
					}
				}
			}
			for(int i = 1; i < n + 1; i++) {
				park[i] = temp_park[i].clone();
			}
			answer++;
		}
		
		System.out.print(answer);
	}
	public static boolean in_range(int x, int y) {
		return x > 0 && x < n + 1 && y > 0 && y < n + 1;
	}
}
