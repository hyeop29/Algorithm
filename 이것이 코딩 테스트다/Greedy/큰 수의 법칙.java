import java.util.*;

public class Num2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		int count = 0;
		int result = 0;
		
		for(int i = 0; i < m; i++) {
			if(count == k) {
				result += arr[n - 2];
				count = 0;
			}
			else {
				result += arr[n -1];
				count++;
			}
		}
		
		System.out.println(result);
		
	}
}
