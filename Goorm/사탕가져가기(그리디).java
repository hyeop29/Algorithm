import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int answer[] = new int[2];
		int temp;
		for(int i = 0; i < t; i++) {
			temp = Integer.parseInt(st.nextToken());
			if (temp % 2 == 1) {
				answer[0]++;
			}
			else {
				answer[1]++;
			}
		}
		
		if(answer[0] != answer[1]) {
			System.out.print(Math.max(answer[0], answer[1]));
		}
		else {
			System.out.print("tie");
		}
		
	}
}
