package br.com.letscode.java;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex3 {
    public static void main(String[] args) {
        List frutas = new ArrayList<>();
        Scanner ler = new Scanner(System.in);

        for (int i=0; i < 5; i++) {
            System.out.println("Digite uma fruta para colocar no seu carrinho: \n");
            String fruta = ler.next();
            frutas.add(fruta);
            System.out.println("As frutas no seu carrinho são: " + frutas);
        }
    }
}
