package br.com.letscode.java;

import java.sql.SQLOutput;

public class main {
    public static void main(String[] args) {
        //Write your code here
        boolean fimDeSemana = true;
        boolean fazendoSol = true;
        boolean vamosAPraia = fimDeSemana && fazendoSol;

        // Tabela verdade
        // Operador $$ (AND)
        // true && true = true
        // true && false = false
        // false && true = false
        // false && false = false

        //Operador || (OR)
        System.out.println(vamosAPraia);

        String mensagem = fimDeSemana ? "É fim de semana!" : "Não é fim de semana";
        System.out.println(mensagem);

    }
}
