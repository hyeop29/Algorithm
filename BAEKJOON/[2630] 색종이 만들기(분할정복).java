import java.io.*;
import java.util.*;
public class Main {
	static int paper[][];
	static int white, blue;
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		paper = new int[n][n];
		
		white = 0;
		blue = 0;
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				paper[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		makeColorPaper(0, 0, n);
		System.out.println(white);
		System.out.println(blue);
	}
	private static void makeColorPaper(int x, int y, int n) {
		if(check(x, y, n)){
			if(paper[x][y] == 1) {
				blue++;
			}
			else {
				white++;
			}
			return;
		}
		int size = n / 2;
		makeColorPaper(x, y, size);
		makeColorPaper(x + size, y, size);
		makeColorPaper(x, y + size, size);
		makeColorPaper(x + size, y + size, size);
		
	}
	private static boolean check(int x, int y, int n) {
		int color = paper[x][y];
		for(int i = x; i < x + n; i++) {
			for(int j = y; j < y + n; j++) {
				if(color != paper[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}
