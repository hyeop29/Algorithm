import java.util.*;

public class Num3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String data = sc.nextLine();
		int x = data.charAt(1) - '0';
		int y = data.charAt(0) - 'a' + 1;
		
		int[] dx = {1, -1};
		int[] dy = {2, -2};
		int result = 0;
		
		// 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
		for(int i = 0; i < dx.length; i++) {
			for(int j = 0; j < dy.length; j++) {
				int temp_x = x + dx[i];
				int temp_y = y + dy[j];
				
				if(temp_x > 0 && temp_x < 9 && temp_y > 0 && temp_y < 9) {
					result++;
				}
			}
		}
		
		int[] temp = {};
		temp = dx;
		dx = dy;
		dy = temp;
		// 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
		for(int i = 0; i < dx.length; i++) {
			for(int j = 0; j < dy.length; j++) {
				int temp_x = x + dx[i];
				int temp_y = y + dy[j];
				
				if(temp_x > 0 && temp_x < 9 && temp_y > 0 && temp_y < 9) {
					result++;
				}
			}
		}
		System.out.println(result);
	}

}
