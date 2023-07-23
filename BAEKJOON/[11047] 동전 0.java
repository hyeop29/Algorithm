import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int A[] = new int[n];
		for(int i = 0; i < n; i++) {
			A[i] = sc.nextInt();
		}
		int answer = 0;
		int count = n - 1;
		while (k != 0) {
			if (k < A[count]) {
				count--;
				continue;
			}
			k -= A[count];
			answer += 1;
		}
		System.out.print(answer);
	}
}
