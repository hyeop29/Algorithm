import java.io.*;
import java.util.*;
public class Main {
	static int video[][];
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		String str;
		video = new int[n][n];
		for(int i = 0; i < n; i++) {
			str = br.readLine();
			for(int j = 0; j < n; j++) {
				video[i][j] = Integer.parseInt(str.substring(j, j + 1));
			}
		}
		quadTree(0, 0, n);
	}
	private static void quadTree(int x, int y, int n) {
		if(check(x, y, n)) {
			System.out.print(video[x][y]);
			return;
		}
		int size = n / 2;
		System.out.print("(");
		quadTree(x, y, size);
		quadTree(x, y + size, size);
		quadTree(x + size, y, size);
		quadTree(x + size, y + size, size);
		System.out.print(")");
		
	}
	private static boolean check(int x, int y, int n) {
		int color = video[x][y];
		for(int i = x; i < x + n; i++) {
			for(int j = y; j < y + n; j++) {
				if(color != video[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}
