package br.com.letscode.java;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ex4 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);


        List<String> frutas = new ArrayList<>();
        frutas.add("MAÇA");
        frutas.add("BANANA");
        frutas.add("MELANCIA");
        frutas.add("MORANGO");
        frutas.add("MANGA");

        System.out.println("Insira o nome da fruta para verificar se está em promoção: \n");
        String fruta = ler.next().toUpperCase();
        if (frutas.contains(fruta)) {
            System.out.printf("Ótima escolha, %s está na promoção!", fruta);
        }

        else {
            System.out.println("Essa fruta não está na promoção :(");
        }


    }
}
