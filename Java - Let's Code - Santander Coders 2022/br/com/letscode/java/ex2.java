package br.com.letscode.java;

import java.util.Scanner;

public class ex2 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        System.out.println("Informe a temperatura em Celsiu(Cº): \n");
        float temperaturaC = ler.nextInt();
        System.out.println(temperaturaC);
        float temperaturaF = (temperaturaC * 9/5) + 32;
        System.out.printf("A temperatura %.2f Cº é igual a %.2f Fº", temperaturaC, temperaturaF);
    }
}
