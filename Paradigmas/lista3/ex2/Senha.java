package ex2;

public class Senha {
    private String senha;
    private int tentativas = 0;

    public Senha(String senha) {
        this.senha = senha;
    }

    public void entraSenha(String senha) {
        if (this.tentativas < 3) {
            if (senha.equals(this.senha)) {
                this.tentativas = 0;
                System.out.println("Senha correta.");
            } else {
                this.tentativas++;
                System.out.println("Senha incorreta. " + (3 - this.tentativas) + " tentativas restantes.");
            }
        } else {
            System.out.println("Senha bloqueada.");
        }
    }

    public void trocarSenha(String old_senha, String new_senha) {
        if (this.tentativas >= 3) {
            System.out.println("Senha bloqueada.");
        } else if (old_senha.equals(this.senha)) {
            this.senha = new_senha;
            System.out.println("Senha alterada.");
        } else {
            this.tentativas++;
            System.out.println("Senha antiga incorreta.");
        }
    }

    public void printarSenha() {
        System.out.println(this.senha);
    }

    public static void main(String[] args) {
        Senha senha = new Senha("abcde");
        senha.printarSenha();
        senha.entraSenha("bla");
        senha.entraSenha("bla");
        senha.entraSenha("bla");
        senha.entraSenha("bla");
        senha.entraSenha("abcde");
        senha.trocarSenha("bla", "ble");
        senha.trocarSenha("abcde", "12345");
        senha.printarSenha();
    }
}
