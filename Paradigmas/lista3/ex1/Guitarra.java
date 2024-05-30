package ex1;

public class Guitarra implements Instrumento{
    @Override
    public void tocar() {
        System.out.println("Tocando a guitarra");
    }
    @Override
    public void afinar() {
        System.out.println("Afinando a guitarra");
    }
}
