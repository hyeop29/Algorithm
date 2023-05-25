import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(br.readLine());
		long adjMatrix[][] = new long[n + 1][n + 1];
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < n + 1; j++) {
				if(i == j) {
					adjMatrix[i][j] = 0;
				}
				else {
					adjMatrix[i][j] = Integer.MAX_VALUE;
				}
			}
		}
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			adjMatrix[a][b] = Math.min(adjMatrix[a][b], c);
		}
		
		for(int k = 1; k < n + 1; k++) {
			for(int i = 1; i < n + 1; i++) {
				for(int j = 1; j < n + 1; j++) {
					adjMatrix[i][j] = Math.min(adjMatrix[i][j],adjMatrix[i][k] + adjMatrix[k][j]);
				}
			}
		}
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < n + 1; j++) {
				if (adjMatrix[i][j] == Integer.MAX_VALUE) {
					bw.write(0 + " ");
				}
				else {
					bw.write(adjMatrix[i][j] + " ");
				}
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
