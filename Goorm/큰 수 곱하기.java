import java.io.*;
import java.math.BigInteger;
import java.util.*;
class Main{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String temp[] = br.readLine().split(" ");
		BigInteger answer = new BigInteger("1");
		for(int i = 0; i < temp.length; i++) {
			answer = answer.multiply(BigInteger.valueOf(Integer.parseInt(temp[i])));
		}
		System.out.print(answer);
	}
}
