package ex3;

public class Porta {
    private boolean aberta;
    private String cor;
    private double dimensaoX, dimensaoY, dimensaoZ;

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

    public void abre() {this.aberta = true;}
    public void fecha() {this.aberta = false;}
    public void pinta (String cor) {this.cor = cor;}
    public boolean estaAberta() {return this.aberta;}
}
