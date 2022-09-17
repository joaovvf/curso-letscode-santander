package br.com.letscode.java;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.TextStyle;
import java.util.Locale;

public class strings {

    public static void main(String[] args) {
        //Olá {nome}. Hoje é {dia-da-semana}, BOM DIA.

        String nome = "João";

        // ISO 8601
        LocalDate hoje = LocalDate.now();
        Locale brasil =  new Locale("pt", "BR");
        //Locale brasil =  new Locale("pt", "BR");

        String diaSemana = hoje.getDayOfWeek().getDisplayName(TextStyle.FULL, brasil);
        String saudacao;

        LocalDateTime agora = LocalDateTime.now();
        if (agora.getHour() >= 0 && agora.getHour() < 12) {
            saudacao = "BOM DIA";
        } else if(agora.getHour() >= 12 && agora.getHour() < 18) {
            saudacao = "BOA TARDE";
        } else if (agora.getHour() >= 18 && agora.getHour() < 24) {
            saudacao = "boa noite";
        } else {
            saudacao = "Bem vindo";
        }

        System.out.printf("Olá, %s. Hoje é %s, %s.%n", nome, diaSemana, saudacao.toUpperCase());


    }
}
