import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long dp[] = new long[n + 1];
		dp[1] = 3;
		
		for(int i = 2; i < n + 1; i++) {
			dp[i] = (dp[i - 1] * 2) % 100000007;
		}
		
		System.out.print(dp[n]);
	}
}
