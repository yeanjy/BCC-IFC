package ex2;

import java.util.Scanner;

public class Senha {
    private String senha;
    private int tentativa;

    public Senha(String senha) {
        this.senha = senha;
        this.tentativa = 1;
    }

    public void trocarSenha(String senhaAntiga, String senhaNova) {
        if (this.tentativa > 3) {
            System.out.println("Senha bloqueada");
            return;
        }

        if (this.senha.equals(senhaAntiga)) {
            this.tentativa = 1;
            this.senha = senhaNova;
            System.out.println("Senha alterada com sucesso");
        }
        else {
            this.tentativa++;
            if (this.tentativa > 3) {
                System.out.println("Senha bloqueada");
            } else {
                System.out.println("Senha incorreta, ainda possui " + (4 - this.tentativa) + " tentativas.");
            }
        }
    }

    public void entraSenha(String senha) {
        if (this.tentativa > 3) {
            System.out.println("Senha bloqueada");
            return;
        }

        if (senha.equals(this.senha)) {
            System.out.println("Senha correta");
            this.tentativa = 1;
        }
        else {
            this.tentativa++;
            if (this.tentativa > 3) {
                System.out.println("Senha bloqueada");
            } else {
                System.out.println("Senha incorreta, ainda possui " + (4 - this.tentativa) + " tentativas.");
            }
        }
    }

    void run() {
        Scanner in = new Scanner(System.in);
        boolean isRunning = true;
        while (isRunning) {
            if (this.tentativa > 3) {
                return;
            }

            System.out.println("Opções: ");
            System.out.println("1 - Entrar");
            System.out.println("2 - Trocar senha");
            System.out.println("3 - Sair");
            String entradaStr = in.nextLine();
            int entrada;
            try {
                entrada = Integer.parseInt(entradaStr);
            } catch (NumberFormatException e) {
                System.out.println("Opção inválida");
                continue;
            }

            switch (entrada) {
                case 1:
                    System.out.println("Digite a sua senha: ");
                    String senha = in.nextLine();
                    entraSenha(senha);
                    break;

                case 2:
                    System.out.println("Digite a sua senha antiga: ");
                    String senhaAntiga = in.nextLine();
                    System.out.println("Digite a sua senha nova: ");
                    String senhaNova = in.nextLine();
                    trocarSenha(senhaAntiga, senhaNova);
                    break;

                case 3:
                    System.out.println("Saindo do sistema");
                    isRunning = false;
                    break;

                default:
                    System.out.println("Opção inválida");
            }
        }
        in.close();
    }

    public static void main(String[] args) {
        Senha minhaSenha = new Senha("bla");
        minhaSenha.run();
    }
}
