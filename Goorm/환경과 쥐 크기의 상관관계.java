import java.util.*;
import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		long a[] = new long[100001];
		long b[] = new long[100001];
		
		long maxA = 0;
		long maxB = 0;
		int temp = 0;
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i < n + 1; i++) {
			temp = Integer.parseInt(st.nextToken());
			if (temp > maxA) {
				maxA = temp;
			}
			a[temp]++;
		}
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i < n + 1; i++) {
			temp = Integer.parseInt(st.nextToken());
			if (temp > maxB) {
				maxB = temp;
			}
			b[temp]++;
		}
		
		long midA = findMidValue(a, maxA);
		long midB = findMidValue(b, maxB);
		
		System.out.println(midA + " " + midB);
		if(midA > midB) {
			System.out.print("good");
		}
		else {
			System.out.print("bad");
		}
	}

	private static long findMidValue(long[] a, long max) {
		long midSum = a[1] + a[2] + a[3];
		long midValue = 1;
		if(midSum < a[1] + a[2] + a[3] + a[4]) {
			midSum = a[1] + a[2] + a[3] + a[4];
			midValue = 2;
		}
		long temp = 0;
		for(int i = 3; i < max - 1; i++) {
			temp = a[i - 2] + a[i - 1] + a[i] + a[i + 1] + a[i + 2];
			if(temp > midSum) {
				midSum = temp;
				midValue = i;
			}
		}
		return midValue;
	}
}
