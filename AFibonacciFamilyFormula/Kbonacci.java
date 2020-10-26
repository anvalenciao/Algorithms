/**
 * $ sudo update-alternatives --config java
 * > /usr/lib/jvm/java-11-openjdk-amd64/bin/java
 * $ javac Kbonacci.java
 * $ java Kbonacci
 */
import java.util.*;
import java.io.*;


public class Kbonacci {
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        while (line != null) {
            String[] data = line.split(" ");
            int k = Integer.parseInt(data[0]);
            long n = Long.parseLong(data[1]);
            System.out.println( fib(k,n) );
            line = br.readLine();
        }

        br.close();
    }

    public static long[][] MatrixMult(int k, long[][] A, long[][] B)
    {
        long[][] R = new long[k][k];
        for (int i=0; i<k; i++) {
            for (int j=0; j<k; j++) {
                R[i][j] = 0;
                for (int l=0; l<k; l++) {
                    R[i][j] = (R[i][j] + A[i][l] * B[l][j]) % 1000000009;
                }
            }
        }
        return(R);
    }

    public static long fib(int k, long n) 
    {
        if (k == 1 || k == 0 || n == 1) return(1);

        long[][] I = new long[k][k]; 
        long[][] A = new long[k][k];
        for (int i=0; i < k; i++) {
            for (int j=0; j<k; j++) {
                A[i][j] = 0;
                I[i][j] = 0;
            }
        }

        for (int i=0; i<k; i++) {
            I[i][i] = 1;
            A[0][i] = 1;
        }
        for (int j=0; j<k-1; j++) {
            A[j+1][j] = 1;
        }

        long[][] Ans = I;

        /*
        int m = 0;
        while (m != n) {
            Ans = MatrixMult(k, A, Ans);
            m++;
        }
        */

        Ans = MatrixPow(k, A, n);

        return(Ans[0][0]);
    }

    public static long[][] MatrixPow(int k, long[][] A, long b)
    {
        long[][] I = new long[k][k];
        for (int i=0; i<k; i++) {
            I[i][i] = 1;
        }
        if (b==0) return(I);
        else if (b==1) return(A);
        else if (b%2 == 0) {
            long[][] R = MatrixPow(k, A, b/2);
            return(MatrixMult(k, R , R));
        }
        else return(MatrixMult(k, A, MatrixPow(k, A, b-1)));
    }
}