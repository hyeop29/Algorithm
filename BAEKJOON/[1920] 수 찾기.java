import java.io.*;
import java.util.*;
public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int arr1[] = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			arr1[i] = Integer.parseInt(st.nextToken());
		}
		
		int m = Integer.parseInt(br.readLine());
		int arr2[] = new int[m];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < m; i++) {
			arr2[i] = Integer.parseInt(st.nextToken());
		}
		StringBuffer sb = new StringBuffer();
		Arrays.sort(arr1);
		for(int i = 0; i < m; i++) {
			sb.append(binarySearch(arr2[i], 0, n - 1, arr1)+ "\n");
		}		
		System.out.print(sb);
	}
	private static int binarySearch(int num, int i, int n, int[] arr) {
		if (i > n) {
			return 0;
		}
		int mid = (i + n) / 2;
		if (num == arr[mid]) {
			return 1;
		}
		if (arr[mid] > num) {
			return binarySearch(num, i, mid - 1, arr);
		}
		else {
			return binarySearch(num, mid + 1, n, arr);
		}
		
	}

}
