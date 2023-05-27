import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt();
		if (k == 1) {
			System.out.print(0);
		}
		else if (k == 2) {
			System.out.print(1);
		}
		else{
			long fk[] = new long[k + 1];
			fk[1] = 0;
			fk[2] = 1;
			for(int i = 3; i < k + 1; i++) {
				fk[i] = (fk[i - 1] + fk[i - 2]) % 1000000007;
			}
			System.out.print(fk[k]);
		}
	}
}
