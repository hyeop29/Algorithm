import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long dp[] = new long[n + 1];
		for(int i = 1; i < n + 1; i++) {
			dp[i] = dp[i - 1] + (long) Math.pow(3, i);
		}
		System.out.print(dp[n]);
	}
}
