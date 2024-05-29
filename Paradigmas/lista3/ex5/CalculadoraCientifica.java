package ex5;

public class CalculadoraCientifica extends Calculadora{
    double potencia(double x, double y)
    {
        try {
            return Math.pow(x, y);
        } catch (ArithmeticException e){
            System.out.println("ERRO. Expressão inderteminado.");
            return Double.NaN;
        }
    }
}
