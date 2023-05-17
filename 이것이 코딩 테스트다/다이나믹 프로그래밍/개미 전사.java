import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k[] = new int[n];
		int dp[] = new int[n];
		for(int i = 0; i < n; i++) {
			k[i] = sc.nextInt();
		}
		dp[0] = k[0];
		if (dp[0] < k[1]) {
			dp[1] = k[1];
		}
		else {
			dp[1] = dp[0];
		}
		
		for(int i = 2; i < n; i++) {
			if (dp[i - 1] < dp[i - 2] + k[i]) {
				dp[i] = dp[i - 2] + k[i];
			}
			else {
				dp[i] = dp[i - 1];
			}
		}
		System.out.print(dp[n - 1]);
	}
}
