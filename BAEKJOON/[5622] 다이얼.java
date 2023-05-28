import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char str[] = br.readLine().toCharArray();
		int answer = 0;
		for(int i = 0; i < str.length; i++) {
			if(str[i] >= 'W') {
				answer += 10;
			}
			else if(str[i] >= 'T') {
				answer += 9;
			}
			else if(str[i] >= 'P') {
				answer += 8;
			}
			else if(str[i] >= 'M') {
				answer += 7;
			}
			else if(str[i] >= 'J') {
				answer += 6;
			}
			else if(str[i] >= 'G') {
				answer += 5;
			}
			else if(str[i] >= 'D') {
				answer += 4;
			}
			else {
				answer += 3;
			}
		}
		System.out.print(answer);
	}
}
