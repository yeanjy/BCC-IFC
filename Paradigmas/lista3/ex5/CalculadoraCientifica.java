package ex5;

public class CalculadoraCientifica extends Calculadora{
    double potencia(double x, double y)
    {
        if (x == 0 && y == 0)
            return Double.NaN;
        return Math.pow(x, y);
    }
}
