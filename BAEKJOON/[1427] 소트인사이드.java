import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine()); 
		String temp = st.nextToken();
		Integer inside[] = new Integer[temp.length()];
		for(int i = 0; i < temp.length(); i++) {
			inside[i] = Integer.parseInt(temp.substring(i, i+1));
		}
		Arrays.sort(inside, Collections.reverseOrder());
		for(int i = 0; i < temp.length(); i++) {
			System.out.print(inside[i]);
		}	
		
	}
}
