import java.util.*;

public class Num4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int result = 0;
		
		while(n != 1) {
			if(n % k == 0) {
				n = n / k;
			}
			else {
				n--;
			}
			result++;
		}
		
		System.out.println(result);
	}
}
