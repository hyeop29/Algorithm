import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int []a = new int[n + 1];
		int []s = new int[n + 1];
		int temp = 0;
		for (int i = 1; i < n + 1; i++) {
			a[i] = sc.nextInt();
			temp += a[i];
			s[i] = temp;
		}
		int []answers = new int[m];
		for (int k = 0; k < m; k++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			answers[k] = s[j] - s[i - 1];
		}
		
		for (int answer : answers) {
			System.out.println(answer);
		}
	}
}
