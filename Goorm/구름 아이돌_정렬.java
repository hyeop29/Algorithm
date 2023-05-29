import java.io.*;
import java.util.*;
class idole implements Comparable<idole>{
	int no;
	int score;
	
	public idole(int no, int score) {
		this.no = no;
		this.score = score;
	}
	@Override
	public int compareTo(idole o) {
		return o.score - this.score;
	}
}
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<idole> big3 = new ArrayList<>();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 1; i < n + 1; i++) {
			big3.add(new idole(i, Integer.parseInt(st.nextToken())));
		}
		Collections.sort(big3);
		System.out.print(big3.get(0).no + " " + big3.get(1).no + " " + big3.get(2).no);
	}
}
