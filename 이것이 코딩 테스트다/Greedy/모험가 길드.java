import java.util.*;

public class Num6 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		int count = 0;
		int result = 0;
		
		for(int i = 0; i < n; i++) {
			count++;
			if(count == arr[i]) {
				result++;
				count = 0;
			}
		}
		
		System.out.println(result);
	}
}
