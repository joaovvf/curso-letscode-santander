package br.com.letscode.java;
import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        System.out.println("Informe um número para a tabuada:\n");
        int numero = ler.nextInt();

        System.out.println("TABUADA DO NÚMERO: "+numero);

            for (int j=1; j <= 10; j++) {
                int resultado = numero * j;
                System.out.println(numero + " x " + j + " = " + resultado);
            }

    }
}
