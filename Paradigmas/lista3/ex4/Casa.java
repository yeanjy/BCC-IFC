public class Casa {

    private porta porta1, porta2, porta3;
    private String cor;

    public Casa(porta porta1, porta porta2, porta porta3, String cor) {
        this.porta1 = porta1;
        this.porta2 = porta2;
        this.porta3 = porta3;
        this.cor = cor;
    }

    public porta getPorta1() {
        return porta1;
    }

    public porta getPorta2() {
        return porta2;
    }

    public porta getPorta3() {
        return porta3;
    }

    public String getCor() {
        return cor;
    }

    public int quantasPortasEstaoAberta() {
        return ((porta1.estaAberta()?1:0) + (porta2.estaAberta()?1:0) + (porta3.estaAberta()? 1: 0));
    }
    public void pinta (String cor)
    {
        this.cor = cor;
    }
}