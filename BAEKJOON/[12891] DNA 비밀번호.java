import java.io.*;
import java.util.*;
public class Main {
	static int check;
	public static void main(String[] args) throws IOException {		
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		char dna[] = new char[s];
		dna = bf.readLine().toCharArray();
		int temp[] = new int[4];
		int checkArr[] = new int[4];
		check = 0;
		st = new StringTokenizer(bf.readLine());
		for(int i = 0; i < 4; i++) {
			checkArr[i] = Integer.parseInt(st.nextToken());
			if (checkArr[i] == 0) {
				check++;
			}
		}

		int answer = 0;
		for(int i = 0; i < p; i++) {
			add(dna[i], temp, checkArr);
		}
		if (check == 4) {
			answer++;
		}
		for(int i = p; i < s; i++) {
			int j = i - p;
			delete(dna[j], temp, checkArr);
			add(dna[i], temp, checkArr);
			if (check == 4) {
				answer++;
			}
		}
		System.out.print(answer);
	}

	private static void delete(char c, int[] temp, int[] checkArr) {
		switch (c) {
		case 'A' :
			if (temp[0] == checkArr[0]) {
				check--;
			}
			temp[0]--;
			break;
		case 'C' :
			if (temp[1] == checkArr[1]) {
				check--;
			}
			temp[1]--;
			break;
		case 'G' :
			if (temp[2] == checkArr[2]) {
				check--;
			}
			temp[2]--;
			break;
		case 'T' :
			if (temp[3] == checkArr[3]) {
				check--;
			}
			temp[3]--;
			break;
		}
		
	}

	private static void add(char c, int[] temp, int[] checkArr) {
		switch (c) {
		case 'A' :
			temp[0]++;
			if (temp[0] == checkArr[0]) {
				check++;
			}
			break;
		case 'C' :
			temp[1]++;
			if (temp[1] == checkArr[1]) {
				check++;
			}
			break;
		case 'G' :
			temp[2]++;
			if (temp[2] == checkArr[2]) {
				check++;
			}
			break;
		case 'T' :
			temp[3]++;
			if (temp[3] == checkArr[3]) {
				check++;
			}
			break;
		}
	}
	
}
