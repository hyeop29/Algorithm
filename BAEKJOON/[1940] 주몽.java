import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int []material = new int[n];
		for (int i = 0; i < n; i++) {
			material[i] = sc.nextInt();
		}
		Arrays.sort(material);
		
		int answer = 0;
		int start = 0;
		int end = n - 1;
		int sum = 0;
		while (start < end) {
			sum = material[start] + material[end];
			if (sum == m) {
				answer++;
				start++;
				end--;
			}
			else if(sum < m) {
				start++;
			}
			else {
				end--;
			}
		}
		System.out.print(answer);
	}
}
