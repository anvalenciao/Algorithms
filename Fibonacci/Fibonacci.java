/**
 * $ sudo update-alternatives --config java
 * > /usr/lib/jvm/java-11-openjdk-amd64/bin/java
 * $ javac Fibonacci.java
 * $ java Fibonacci
 */
import java.util.*;
import java.io.*;


public class Fibonacci {
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        while (line != null) {
            long n = Long.parseLong(line);
            System.out.println( (long)(1/Math.sqrt(5)*(Math.pow((1+Math.sqrt(5))/2,n+1)-Math.pow((1-Math.sqrt(5))/2,n+1))) );
            System.out.println( fib(n) );
            //System.out.println( fibrec(n) );
            line = br.readLine();
        }

        br.close();
    }

    /**
     * fibrec(0) = 1
     * fibrec(1) = 1
     * fibrec(n) = fibrec(n-1) + fibrec(n-2)
     */
    public static long fibrec(long n)
    {
        if ((n == 1) || (n == 0)) return(1);
        else return(fibrec(n-1) + fibrec(n-2));
    }


    public static long fib(long n) {
        // Pre Q: n=N && n>1
        // Pos R: n=N && n>1 && a = fib(n)
        // O(n)

        long k = 1;
        long a = 1;
        long b = 1;

        // Inv P: n=N && n>1 && a = fib(k) && 1 <= k <= n && b = fib(k-1)
        // Cota t = n-k
        while (k != n) {
            k++;
            long aux = a;
            a = a + b;
            b = aux;
        }

        // Pos R: n=N && n>1 && a = fib(n)

        return(a);
    }
}