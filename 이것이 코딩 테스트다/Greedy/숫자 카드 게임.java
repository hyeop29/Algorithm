import java.util.*;

public class Num3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int result = 0;
		int temp;
		
		for(int i = 0; i < n; i++) {
			int min_value = sc.nextInt();
			
			for(int j = 1; j < m; j++) {
				temp = sc.nextInt();
				if(min_value > temp) {
					min_value = temp;
				}
			}
			
			if(result < min_value) {
				result = min_value;
			}
		}
		System.out.println(result);
	}
}
