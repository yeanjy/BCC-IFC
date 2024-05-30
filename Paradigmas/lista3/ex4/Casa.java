package ex4;

public class Casa {

    private Porta porta1, porta2, porta3;
    private String cor;

    public Casa(Porta porta1, Porta porta2, Porta porta3, String cor) {
        this.porta1 = porta1;
        this.porta2 = porta2;
        this.porta3 = porta3;
        this.cor = cor;
    }

    @Override
    public String toString() {
        return "Casa{" +
                "porta1=" + porta1 +
                ", porta2=" + porta2 +
                ", porta3=" + porta3 +
                ", cor='" + cor + '\'' +
                '}';
    }

    public Porta getPorta1() {
        return porta1;
    }

    public Porta getPorta2() {
        return porta2;
    }

    public Porta getPorta3() {
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

    public static class Porta {
      private boolean aberta;
      private String cor;
      private double dimensaoX, dimensaoY, dimensaoZ;

      @Override
      public String toString() {
        return "Porta{" +
                "aberta=" + aberta +
                ", cor='" + cor + '\'' +
                ", dimensaoX=" + dimensaoX +
                ", dimensaoY=" + dimensaoY +
                ", dimensaoZ=" + dimensaoZ +
                '}';
      }

      public Porta(boolean aberta, String cor, double dimensaoX, double dimensaoY, double dimensaoZ) {
        if (dimensaoX <= 0 || dimensaoY <= 0 || dimensaoZ <= 0) {
          throw new IllegalArgumentException("As dimensões devem ser maiores que zero.");
        }
        this.aberta = aberta;
        this.cor = cor;
        this.dimensaoX = dimensaoX;
        this.dimensaoY = dimensaoY;
        this.dimensaoZ = dimensaoZ;
      }

      public void abre() {
        this.aberta = true;
      }

      public void fecha() {
        this.aberta = false;
      }

      public void pinta(String cor) {
        this.cor = cor;
      }

      public boolean estaAberta() {
        return this.aberta;
      }
    }
}