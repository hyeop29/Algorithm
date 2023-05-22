import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int indegree[] = new int[n + 1];
		
		ArrayList<Integer>[] students = new ArrayList[n + 1];
		for(int i = 1; i < n + 1; i++) {
			students[i] = new ArrayList<>();
		}
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int small = Integer.parseInt(st.nextToken());
			int big = Integer.parseInt(st.nextToken());
			students[small].add(big);
			indegree[big]++;
		}
		Queue<Integer> queue = new LinkedList<>();
		for(int i = 1; i < n + 1; i++) {
			if (indegree[i] == 0) {
				queue.add(i);
			}
		}
		int student;
		int count = 0;
		while(!queue.isEmpty()) {
			student = queue.poll();
			count++;
			if (count == n) {
				bw.write(student+"");
				break;
			}
			bw.write(student + " ");
			for(int s : students[student]) {
				indegree[s]--;
				if (indegree[s] == 0) {
					queue.add(s);
				}
			}
		}
		bw.flush();
		bw.close();
	}
}
