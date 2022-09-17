package br.com.letscode.java;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex5 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        List<String> frutasCliente =  new ArrayList<>();
        List<String> frutasPromocao = new ArrayList<>();
        frutasPromocao.add("MORANGO");
        frutasPromocao.add("ABACAXI");
        frutasPromocao.add("BANANA");
        int breaker = 0;
        int desconto = 0;

        while (breaker != 1) {
            System.out.println("Insira sua lista de compras: \n");
            String fruta = ler.next().toUpperCase();
            if (frutasPromocao.contains(fruta)) {
                frutasCliente.add(fruta);
                desconto += 5;
            }

            else {
                desconto += 0;
            }
            System.out.println("Digite qualquer numero para continuar e digite 1 para parar: ");
            breaker = ler.nextInt();
        }

        System.out.println("Seu desconto é de " + desconto + "%");
        System.out.println("Suas frutas na promoção são: " + frutasCliente);


    }
}
