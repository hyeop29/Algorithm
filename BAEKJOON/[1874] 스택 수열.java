import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int stack[] = new int[n];
		for(int i = 0; i < n; i++) {
			stack[i] = sc.nextInt();
		}
		Stack<Integer> s = new Stack<>();
		StringBuffer bf = new StringBuffer();
		int count = 1;
		boolean check = true;
		for(int i = 0; i < n; i++) {
			while(stack[i] >= count) {
				s.push(count);
				bf.append("+\n");
				count++;
			}
			if (s.pop() > stack[i]) {
				System.out.print("NO");
				check = false;
				break;
			}
			else {
				bf.append("-\n");
			}
		}
		if (check) {
			System.out.print(bf);
		}
	}
}
