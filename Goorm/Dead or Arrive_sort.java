import java.util.*;
import java.io.*;

class car implements Comparable<car> {
	int no;
	int v;
	int w;
	public car(int no, int v, int w) {
		this.no = no;
		this.v = v;
		this.w = w;
	}
	@Override
	public int compareTo(car o) {
		if(this.v == o.v) {
			if(this.w == o.w) {
				return o.no - this.no;
			}
			return o.w - this.w;
		}
		else {
			return this.v - o.v;
		}
	}
	
	public String toString() {
		return no + " "+ v + " " + w;
	}
}

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<car> carInfo = new ArrayList<>();
		StringTokenizer st;
		for(int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			carInfo.add(new car(i, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		Collections.sort(carInfo);
		int answer = 0;
		int tempV = 0;
		for(car temp : carInfo) {
			if(tempV < temp.v) {
				tempV = temp.v;
				answer += temp.no;
			}
		}
		
		System.out.print(answer);
	}

}
