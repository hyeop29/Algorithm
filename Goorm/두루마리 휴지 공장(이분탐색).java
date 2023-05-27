import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		long tissue[] = new long[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			tissue[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(tissue);
		long start = tissue[n - 1];
		long end = start + m;
		long mid;
		long check = 0;
		long answer = 0;
		while (start <= end) {
			mid = (start + end) / 2;
			check = 0;
			for(int i = 0; i < n; i++) {
				check += mid - tissue[i];
				if( check > m) {
					break;
				}
			}
			if(check > m) {
				end = mid - 1;
			}
			else {
				answer = mid;
				start = mid + 1;
			}
		}
		if (answer == 0) {
			System.out.print("No way!");
		}
		else {
			System.out.print(answer);
		}
	}
}
