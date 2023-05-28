import java.io.*;
import java.util.*;
public class Main {
	static char star[][];
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		star = new char[n][n];
		
		makeStar(0, 0, n);
		
		for(int i = 0; i < n; i++) {
			bw.write(star[i]);
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
	private static void makeStar(int x, int y, int n) {
		if(n == 3) {
			for(int i = x; i < x + n; i++) {
				for(int j = y; j < y + n; j++) {
					star[i][j] = '*';
					if( i == x + n/3 && j == y + n/3) {
						star[i][j] = ' ';
					}
				}
			}
			return;
		}
		int size = n / 3;
		
		makeStar(x, y, size);
		
		makeStar(x + size, y, size);
		makeStar(x + size + size, y, size);
		
		makeStar(x, y + size, size);
		makeStar(x, y + size + size, size);
		
		makeStar(x + size, y + size + size, size);
		makeStar(x + size + size, y + size, size);
		
		empty(x + size, y + size, size);
		makeStar(x + size + size, y + size + size, size);
		
	}
	private static void empty(int x, int y, int size) {
		for(int i = x; i < x + size; i++) {
			for(int j = y; j < y + size; j++) {
				star[i][j] = ' ';
			}
		}
		
	}
}
