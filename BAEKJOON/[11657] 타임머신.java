import java.util.*;
class Edgeinfo {
	int b;
	int c;
	public Edgeinfo(int b, int c) {
		this.b = b;
		this.c = c;
	}
	
	public String toString() {
		return "Edge{" + b + " " + c + "}"; 
	}
}
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		long distance[] = new long[n + 1]; // 실제 거리값을 담아주는 배열
		Arrays.fill(distance, Integer.MAX_VALUE);
		distance[1] = 0;
		
		// 인접 edge list 초기화
		ArrayList<Edgeinfo> adjacencyList[] = new ArrayList[n + 1]; 
		for(int i = 1; i < n + 1; i++) {
			adjacencyList[i] = new ArrayList<Edgeinfo>();
		}
		
 		for(int i = 0; i < m; i++) {
			int a = sc.nextInt();
 			int b = sc.nextInt();
 			int c = sc.nextInt();
 			adjacencyList[a].add(new Edgeinfo(b,c));
		}
 		
// 		System.out.println(Arrays.toString(adjacencyList));
 		
 		for(int i = 1; i < n; i++) {
 			for(int j = 1; j < n + 1; j++) {
 				if(distance[j] == Integer.MAX_VALUE) {
 					continue;
 				}
 				for(Edgeinfo des : adjacencyList[j]) {
 					if(distance[des.b] > distance[j] + des.c) {
 						distance[des.b] = distance[j] + des.c;
 					}
 				}
 			}
 		}
 		boolean timeMachine = false;
 		for(int i = 1; i < n + 1; i++) {
 			if(distance[i] == Integer.MAX_VALUE) {
 				continue;
 			}
 			for(Edgeinfo des : adjacencyList[i]) {
 				if(distance[des.b] > distance[i] + des.c) {
 					timeMachine = true;
 					break;
 				}
 			}
 			if (timeMachine) {
 				break;
 			}
 		}
 		
 		if (timeMachine) {
 			System.out.print(-1);
 		}
 		else {
 			for(int i = 2; i < n + 1; i++) {
 				if (distance[i] == Integer.MAX_VALUE) {
 					System.out.println(-1);
 				}
 				else {
 					System.out.println(distance[i]);
 				}
 			}
 		}
	}
}
