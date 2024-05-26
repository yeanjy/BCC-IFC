public class Senha {
    private String senha;
    private int tentativa;

    public Senha(String senha, int tentativa) {
        this.senha = senha;
        this.tentativa = tentativa;
    }

   public void entraSenha(String senha)
   {
       if (this.tentativa >= 3)
       {
           System.out.println("Senha bloqueado");
           return;
       }

       if (senha.equals(this.senha))
       {
           System.out.println("Senha correta");
           this.tentativa = 0;
       }
       else
       {
           ++tentativa;
           System.out.println("Senha incorreta, ainda possui " + this.tentativa + " tentativas.");
       }
   }
}
