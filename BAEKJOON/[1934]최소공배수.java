import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(st.nextToken());
		int big = 0;
		int small = 0;
		int temp = 0;
		for(int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			
			if (a > b) {
				big = a;
				small = b;
			}
			else {
				big = a;
				small = b;
			}
			
			while(big % small != 0) {
				temp = big % small;
				big = small;
				small = temp;
				
			}
			bw.write((a * b) / small + "\n");
		}
		bw.flush();
		bw.close();
	}
}
