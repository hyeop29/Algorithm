import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String sNum = sc.next();
		
		char[] cNum = sNum.toCharArray();
		int answer = 0;
		for (int i = 0; i < cNum.length; i++) {
			answer += cNum[i] - 48;
		}
		System.out.print(answer);
	}
}
