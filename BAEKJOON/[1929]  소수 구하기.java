import java.io.*;
import java.util.*;
public class 소수구하기 {
	public static void main(String args[]) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		boolean firstPrime = true;
		int pn[] = new int[m + 1];
		Arrays.fill(pn, 1);
		pn[1] = 0;
		for(int i = 2; i < m + 1; i++) {
			if (pn[i] == 0) {
				continue;
			}
			for(int j = i + i; j < m + 1; j += i) {
				pn[j] = 0;
			}
		}
		for(int i = n; i < m + 1; i++) {
			if (pn[i] == 0) {
				continue;
			}
			if (!firstPrime) {
				bw.write("\n");
			}
			firstPrime = false;
			bw.write(i + "");
		}
		bw.flush();
		bw.close();
		
	}
}
