import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(bf.readLine());
		int dp[] = new int[n + 1];
		int before[] = new int[n + 1];
		
		for(int i = 2; i < n + 1; i++) {
			dp[i] = dp[i - 1] + 1;
			before[i] = i - 1;
			if(i % 3 == 0 && dp[i/3] + 1 < dp[i]) {
				dp[i] = dp[i/3] + 1;
				before[i] = i/3;
			}
			if (i % 2 == 0 && dp[i/2] + 1 < dp[i]) {
				dp[i] = dp[i/2] + 1;
				before[i] = i/2;
			}
		}
		bw.write(dp[n]+"\n");
		while (n != 1) {
			bw.write(n + " ");
			n = before[n];
		}
        bw.write(n + "");
		bw.flush();
		bw.close();
		bf.close();
	}
}
