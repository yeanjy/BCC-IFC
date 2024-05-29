package ex3;

public class porta {
  private boolean aberta;
  private String cor;
  private double dimensaoX, dimensaoY, dimensaoZ;

  porta(boolean aberta, String cor, double dimensaoX, double dimensaoY, double dimensaoZ)
  {
    this.aberta = aberta;
    this.cor = cor;
    this.dimensaoX = dimensaoX;
    this.dimensaoY = dimensaoY;
    this.dimensaoZ = dimensaoZ;
  }

  public void abre() {this.aberta = true;}
  public void fecha() {this.aberta = false;}
  public void pinta (String cor) {this.cor = cor;}
  public boolean estaAberta() {return this.aberta;}
}
