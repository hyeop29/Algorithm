import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char name[] = br.readLine().toCharArray();
		int index = name.length - 1;
		for(int i = 0; i < name.length - 1; i++) {
			if(name[i + 1] < name[i]) {
				index = i;
				break;
			}
		}
		for(int i = 0; i < name.length; i++) {
			if(i == index) {
				continue;
			}
			bw.write(name[i]);
		}
		bw.flush();
		bw.close();
	}
}
