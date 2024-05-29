package ex5;

public class Calculadora {
    public double multiplicar(double x, double y)
    {
        return x*y;
    }

    public double dividir(double x, double y) {
        try {
            return x/y;
        } catch (ArithmeticException e) {
            System.out.println("ERRO. Divisão por zero.");
            return Double.NaN;
        }
    }

    public double somar (double x, double y)
    {
        return x+y;
    }

    public double subtrair (double x, double y)
    {
        return x-y;
    }
}