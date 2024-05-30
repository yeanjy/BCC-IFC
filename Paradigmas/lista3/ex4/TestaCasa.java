package ex4;

public class TestaCasa {

    public static void main(String[] args) {
        Casa.Porta porta1 = new Casa.Porta(false, "azul", 1.3, 2, 3);
        Casa.Porta porta2 = new Casa.Porta(true, "vermelho", 1.3, 2, 3);
        Casa.Porta porta3 = new Casa.Porta(true, "verde", 1.3, 2, 3);

        Casa minha_casa = new Casa(porta1, porta2, porta3, "azul");
        System.out.println("Cor da casa: " + minha_casa.getCor());
        System.out.println("Quantidade de portas abertas: " + minha_casa.quantasPortasEstaoAberta());
        minha_casa.pinta("amarelo");
        System.out.println("Cor da casa pintada: " + minha_casa.getCor());
        System.out.println(minha_casa.getPorta1().toString());
        System.out.println(minha_casa.getPorta2().toString());
        System.out.println(minha_casa.getPorta3().toString());

    }
}
