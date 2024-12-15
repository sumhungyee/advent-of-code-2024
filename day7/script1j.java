import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.Math;
// :(
public class script1j {
    public static void main(String[] args) throws IOException {
        String filePath = "input.txt";
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        long result = 0;
        while((line = reader.readLine()) != null) {
            String[] lineArr = line.split(" ");
            long[] intArr = new long[lineArr.length];
            lineArr[0] = lineArr[0].substring(0, lineArr[0].length() - 1);
            for (int i = 0; i < lineArr.length; i++) {
                intArr[i] = Long.parseLong(lineArr[i]);
            }

            int ops = 0b0;
            long curr = 0;
            
            do {
                curr = intArr[1];
                for (int i = 0; i < intArr.length - 2; i++) {
                    long op = (ops >> i) & 0b1;
                    if (op == 0) {
                        curr *= intArr[i + 2];
                    } else {
                        curr += intArr[i + 2];
                    }
                    if (curr > intArr[0]) break;
                }
                if (curr == intArr[0]) {
                    result += intArr[0];
                    break;
                }
                ops = (ops + 1) % (int) Math.pow(2, intArr.length - 2);
            } while (ops != 0);
       
        }

        System.out.println(result);
        reader.close();
    }
}
