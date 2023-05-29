import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		HashSet<Integer> temp = new HashSet<>();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < n; i++) {
			temp.add(Integer.parseInt(st.nextToken()));
		}
		ArrayList<Integer> sortTemp = new ArrayList<>(temp);
		Collections.sort(sortTemp);
		
		for(int i : sortTemp) {
			System.out.print(i + " ");
		}
	}
}
