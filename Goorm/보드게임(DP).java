import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long dp[] = new long[n + 1];
		
		if(n == 1 || n == 2) {
			System.out.print(1);
		}
		else {
			dp[0] = 1;
			dp[1] = 1;
			dp[2] = 1;
			for(int i = 3; i < n + 1; i++) {
				dp[i] = (dp[i - 1] + dp[i - 3]) % 1000000007;
			}
			System.out.print(dp[n]);
		}
	}
}
