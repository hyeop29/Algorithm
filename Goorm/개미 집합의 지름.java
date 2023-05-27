import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int ant[] = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			ant[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(ant);
		int start = 0;
		int end = 0;
		int count = 0;
		while (start < n && end < n) {
			if(ant[end] - ant[start] <= d) {
				count = Math.max(count, end - start + 1);
				end++;
			}
			else {
				start++;
			}
		}
		
		System.out.print(n - count);
	}
}
