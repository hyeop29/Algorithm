import java.io.*;
import java.util.Arrays;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		long result[] = new long[input.length()];
		for(int i = 0; i < input.length(); i++) {
			result[i] = Integer.parseInt(input.substring(i, i + 1));
		}
		boolean two = false;
		boolean one = false;
		boolean to = false;
		boolean ot = false;
		int count1 = 0;
		int count2 = 0;
		int tot = 0;
		int oto = 0;
		for(int i = 0; i < input.length(); i++) {
			if((count1 >= 1 && count2 >= 1) || (tot >= 1 && count2 >= 1) || (tot >= 1 && count1 >= 1) || (oto >= 1 && count1 >= 1)
					|| (oto >= 1 && count2 >= 1) || (tot >= 1 && oto >= 1)) {
				break;
			}
			if(to && result[i] == 2) {
				to = false;
				tot++;
				count2--;
			}
			else if(ot && result[i] == 1) {
				ot = false;
				oto++;
				count1--;
			}
			else if(one && result[i] == 2) {
				one = false;
				ot = true;
				count1++;
			}
			else if(two && result[i] == 1) {
				two = false;
				to = true;
				count2++;
			}
			else if(result[i] == 1) {
				one = true;
			}
			else if(result[i] == 2) {
				two = true;
			}
			else if(result[i] > 2) {
				one = false;
				two = false;
				to = false;
				ot = false;
			}
		}
		if((count1 >= 1 && count2 >= 1) || (tot >= 1 && count2 >= 1) || (tot >= 1 && count1 >= 1) || (oto >= 1 && count1 >= 1)
				|| (oto >= 1 && count2 >= 1) || (tot >= 1 && oto >= 1)) {
			System.out.print("Yes");
		}
		else {
			System.out.print("No");
		}
	}
}
