import java.io.*;
import java.util.*;

class eventInfo implements Comparable<eventInfo>{
	int start;
	int end;
	
	public eventInfo(int start, int end) {
		this.start = start;
		this.end = end;
	}

	@Override
	public int compareTo(eventInfo o) {
		if (this.end == o.end) {
			return o.start - this.start;
		}
		else {
			return this.end - o.end;
		}
	}
	
	
}

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		
		ArrayList<eventInfo> event = new ArrayList<>();
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			event.add(new eventInfo(s, e));
		}
		
		Collections.sort(event);
		
		int init = 0;
		int answer = 0;
		for(eventInfo now : event) {
			if(now.start > init) {
				answer++;
				init = now.end;
			}
		}
		System.out.print(answer);
	}
}
