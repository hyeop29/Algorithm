import java.io.*;
import java.util.*;
public class Main {
	static int[] set;
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		set = new int[n + 1];
		for(int i = 0; i < n + 1; i++) {
			set[i] = i;
		}
		
		int temp = 0;
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int cal = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (cal == 0) {
				int represent_A = find(a);
				int represent_B = find(b);
				
				if (represent_A < represent_B) {
					set[represent_B] = represent_A;
					temp = find(b);
				}
				else if (represent_B < represent_A) {
					set[represent_A] = represent_B;
					temp = find(a);
				}
				else {
					continue;
				}
			}
			else {
				if(find(a) == find(b)) {
					bw.write("YES\n");
				}
				else {
					bw.write("NO\n");
				}
			}
		}
		bw.flush();
		bw.close();
	}
	private static int find(int index) {
		if (set[index] == index) {
			return index;
		}
		else {
			return set[index] = find(set[index]);
		}
	}
}
