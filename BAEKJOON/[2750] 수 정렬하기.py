import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int temp[] = new int[n];
		for(int i = 0; i < n; i++) {
			temp[i] = sc.nextInt();
		}
		Arrays.sort(temp);
		for(int t : temp) {
			System.out.println(t);
		}
	}
}
