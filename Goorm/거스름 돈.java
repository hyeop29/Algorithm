import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n =  sc.nextInt();
		int answer = 0;
		
		while(n != 0) {
			if (n >= 40) {
				answer += n / 40;
				n = n - 40 * (n / 40);
			}
			else if (n >= 20) {
				answer += n / 20;
				n = n - 20 * (n / 20);
			}
			else if (n >= 10) {
				answer += n / 10;
				n = n - 10 * (n / 10);
			}
			else if (n >= 5) {
				answer += n / 5;
				n = n - 5 *(n / 5);			
			}
			else {
				answer += n;
				n = 0;
			}
		}
		System.out.print(answer);
	}
}
