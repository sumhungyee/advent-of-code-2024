import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
// :(
public class script2j {
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

            String ops = "0".repeat(intArr.length - 2); // trinary now
            long curr = 0;
            do {
                curr = intArr[1];
                for (int i = 0; i < intArr.length - 2; i++) {   
                    long op = Integer.valueOf(String.valueOf(ops.charAt(intArr.length - 3 - i)));
                    if (op == 0) {
                        curr *= intArr[i + 2];
                    } else if (op == 1) {
                        curr += intArr[i + 2];
                    } else if (op == 2) {
                        curr = Long.valueOf(String.valueOf(curr) + String.valueOf(intArr[i + 2]));
                    } else {
                        System.out.println(op);
                        throw new RuntimeException();
                    }
                    if (curr > intArr[0]) break;
                }
                if (curr == intArr[0]) {
                    result += intArr[0];
                    break;
                }
                ops = addOneTrinary(ops, intArr.length - 2);
            } while (Long.valueOf(ops) != 0);
       
        }
        System.out.println(result);
        reader.close();
    }

    public static String addOneTrinary(String num, int limit) {
        char[] val = String.valueOf(num).toCharArray();
        boolean carry = true;
        int idx = val.length - 1;
        while (carry) {
            
            if (val[idx] == '0' || val[idx] == '1') {
                val[idx] = (char) (val[idx] + 1);
                carry = false;
            } else {
                val[idx] = '0';
                idx--;
                if (idx == -1) carry = false;
                
            }
        }
        return String.valueOf(val);
    }
}
