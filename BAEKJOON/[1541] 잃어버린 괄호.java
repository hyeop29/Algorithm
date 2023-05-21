import java.util.*;
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		String num[] = s.split("-");
		String temp[];
		int sum = 0;
		int answer = 0;
		for(int i = 0; i < num.length; i++) {
			temp = num[i].split("[+]");
			sum = 0;
			for(int j = 0; j < temp.length; j++) {
				sum += Integer.parseInt(temp[j]);
			}
			if (i == 0) {
				answer += sum;
			}
			else {
				answer -= sum;
			}
		}
		System.out.print(answer);
	}
}
