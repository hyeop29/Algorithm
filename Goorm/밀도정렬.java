import java.util.*;
import java.io.*;
class info implements Comparable<info>{
	int no;
	double m; //밀도
	int w; //무게
	public info(int no, double m, int w) {
		this.no = no;
		this.m = m;
		this.w = w;
	}
	@Override
	public int compareTo(info o) {
		int result = Double.compare(o.m, this.m);
		if(result == 0){
			if(this.w == o.w) {
				return this.no - o.no;
			}
			else {
				return o.w - this.w;
			}
		}
		else {
			return result;
		}
	}
	public String toString() {
		return no + " " + m + " " + w + " ";
	}
}


class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		ArrayList<info> highInfo1 = new ArrayList<>();
		
		for(int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			highInfo1.add(new info(i, w/v, w));
		}
		Collections.sort(highInfo1);
		System.out.println(highInfo1.get(0).no);
	}
}
