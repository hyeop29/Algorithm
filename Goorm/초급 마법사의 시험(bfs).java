import java.io.*;
import java.util.*;
class Coordinate {
    int x;
    int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coordinate that = (Coordinate) o;
        return x == that.x && y == that.y;
    }

    @Override
    public int hashCode() {
        return x * 31 + y;
    }
}
public class Main {
	static int forest[][];
	static HashMap<Integer, HashSet<Coordinate>> visited;
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	static int r;
	static int c;
	static ArrayList<Integer> answer;
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		// r이 세로, c가 가로
		forest = new int[r + 1][c + 1];
		for(int i = 1; i < r + 1; i++) {
			String line = br.readLine();
			for(int j = 1; j < c + 1; j++) {
				forest[i][j] = line.charAt(j - 1) - '0';
			}
		}
		
		answer = new ArrayList<>();
		visited = new HashMap<>();
		bfs(1, 1, 0, k);
		Collections.sort(answer);
		if(!answer.isEmpty()) {
			System.out.print(answer.get(0));
		}
		else {
			System.out.print(-1);
		}
		
	}
	public static void bfs(int x, int y, int d, int mp) {
		Queue<int []> queue = new LinkedList<>();
		queue.add(new int[] {x, y, d, mp});
		visited.put(mp, new HashSet<>());
		visited.get(mp).add(new Coordinate(0, 0));
		int nx, ny;
		int tx, ty, td, tmp;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			tx = now[0];
			ty = now[1];
			td = now[2];
			tmp = now[3];
			if(tx == r && ty == c) {
				answer.add(td);
			}
			for(int i = 0; i < 4; i++) {
				nx = tx + dx[i];
				ny = ty + dy[i];
				if(in_range(nx, ny) && !visited.get(tmp).contains(new Coordinate(nx, ny))) {
					if(forest[nx][ny] == 1) {
						if(tmp >= 10) {
							nx += dx[i];
							ny += dy[i];
							if(in_range(nx, ny) && forest[nx][ny] == 0) {
								queue.add(new int[] {nx, ny, td + 1, tmp - 10});
								visited.putIfAbsent(tmp - 10, new HashSet<>());
								visited.get(tmp - 10).add(new Coordinate(nx, ny));
							}
							
						}
					}
					else {
						queue.add(new int[] {nx, ny, td + 1, tmp});
						visited.putIfAbsent(tmp, new HashSet<>());
						visited.get(tmp).add(new Coordinate(nx, ny));
					}
				}
			}
		}
	}
	public static boolean in_range(int x, int y) {
		return x > 0 && x <= r && y > 0 && y <= c;
	}
}
