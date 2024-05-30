package ex5;

public class TestarCalculadora {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        CalculadoraCientifica calccien = new CalculadoraCientifica();

        System.out.println("Resultado de somar(2, 3): " + calc.somar(2, 3));
        System.out.println("Resultado de dividir(0, 0): " + calc.dividir(0, 0));
        System.out.println("Resultado de multiplicar(13, 22): " + calc.multiplicar(13, 22));
        System.out.println("Resultado de subtrair(11, 22): " + calc.subtrair(11, 22));
        System.out.println("Resultado de potencia(0, 0): " + calccien.potencia(0, 0));
    }
}
