package ex1;

public class Piano implements Instrumento {
    @Override
    public void tocar() {
        System.out.println("Tocando o piano");
    }
    @Override
    public void afinar() {
        System.out.println("Afinando o piano");
    }
}
