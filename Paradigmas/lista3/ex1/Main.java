package ex1;

public class Main {
    public static void main(String[] args) {
        Instrumento guitarra = new Guitarra();
        Instrumento piano = new Piano();
        guitarra.tocar();
        guitarra.afinar();
        piano.tocar();
        piano.afinar();
    }
}