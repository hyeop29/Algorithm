import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
	int v;
	int w;
	
	public Edge(int v, int w) {
		this.v = v;
		this.w = w;
	}
	
	@Override
	public int compareTo(Edge e) {
		return this.w - e.w;
	}
}


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int v_num = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		
		int start = Integer.parseInt(br.readLine());
		
		ArrayList<Edge> adjacencyList[] = new ArrayList[v_num + 1];
		for (int i = 1; i < v_num + 1; i++) {
			adjacencyList[i] = new ArrayList<Edge>();
		}
		
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjacencyList[u].add(new Edge(v, w));
		}
		// start에서 각 정점으로 거리를 기록할 배열, 초기값은 MAX_VALUE를 넣어준다.
		int distance[] = new int[v_num + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);
		distance[start] = 0;
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start, 0));
		while(!pq.isEmpty()) {
			Edge now = pq.poll();
			for(Edge next : adjacencyList[now.v]) {
				if(distance[next.v] > now.w + next.w) {
					distance[next.v] = now.w + next.w;
					pq.add(new Edge(next.v, distance[next.v]));
				}
			}
		}
		
		for(int i = 1; i < v_num + 1; i++) {
			if(distance[i] == Integer.MAX_VALUE) {
				bw.write("INF\n");
				continue;
			}
			bw.write(distance[i] + "\n");
		}
		bw.flush();
		bw.close();
	}
}
