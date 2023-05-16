import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int n = Integer.parseInt(st.nextToken());
		int x = 0;
		PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) -> {
			int abs_o1 = Math.abs(o1);
			int abs_o2 = Math.abs(o2);
			if (abs_o1 == abs_o2) {
				return o1 - o2;
			}
			return abs_o1 - abs_o2;
		});
		StringBuffer sb = new StringBuffer();
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			x = Integer.parseInt(st.nextToken());
			if (x != 0) {
				queue.add(x);
			}
			else {
				if(queue.size() == 0) {
					sb.append("0\n");
				}
				else {
					sb.append(String.valueOf(queue.poll()));
					sb.append("\n");
				}
			}
		}
		System.out.print(sb);
	}
}
