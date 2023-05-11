import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int answer = 1; // n 자기 자신인 경우
		int sum = 1;
		int start = 1;
		int end = 1;
		while (end != n) {
			if (sum == n) {
				answer++;
				sum = sum + ++end;
			}
			else if (sum > n) {
				sum = sum - start++;
			}
			else {
				sum = sum + ++end;
			}
		}
		System.out.print(answer);
	}

}
