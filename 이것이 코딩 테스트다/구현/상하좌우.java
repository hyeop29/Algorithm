import java.util.*;

public class Num1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		String[] plans = sc.nextLine().split(" ");
		
		int x = 1, y = 1;
		
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		char[] direction = {'L', 'R', 'U', 'D'};
		
		
		for(int i = 0; i < plans.length; i++) {
			int temp_x = -1, temp_y = -1;
			
			for(int j = 0; j < direction.length; j++) {
				if(plans[i].charAt(0) == direction[j]) {
					temp_x = x + dx[j];
					temp_y = x + dy[j];
				}
			}
			if(temp_x < 1 || temp_x > n || temp_y < 1 || temp_y > n) {
				continue;
			}
			x = temp_x;
			y = temp_y;
		}
		
		System.out.println(x + " " + y);
	}
