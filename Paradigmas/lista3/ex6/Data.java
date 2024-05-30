package ex6;
import java.time.LocalDate;

public class Data {
    private int dia;
    private int mes;
    private int ano;

    public Data(int dia, int mes, int ano) {
        if (dataValida(dia, mes, ano)) {
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        } else {
            System.out.println("Data inválida");
        }
    }

    public Data() {
        LocalDate dataAtual = LocalDate.now();
        this.dia = dataAtual.getDayOfMonth();
        this.mes = dataAtual.getMonthValue();
        this.ano = dataAtual.getYear();
    }

    // Método para verificar se o ano é bissexto
    private boolean isAnoBissexto(int ano) {
        return (ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0);
    }

    // Método para verificar se a data é válida
    private boolean dataValida(int dia, int mes, int ano) {
        if (ano < 1 || mes < 1 || mes > 12 || dia < 1) {
            return false;
        }
        int[] diasNoMes = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        // Verifica se é ano bissexto
        if (isAnoBissexto(ano) && mes == 2) {
            diasNoMes[1] = 29;
        }
        return dia <= diasNoMes[mes - 1];
    }

    public void imprimirData() {
        System.out.println(this.dia + "/" + this.mes + "/" + this.ano);
    }

    public void proximoDia() {
        if (dataValida(this.dia + 1, this.mes, this.ano)) {
            this.dia++;
        } else if (dataValida(1, this.mes + 1, this.ano)) {
            this.mes++;
            this.dia = 1;
        } else {
            this.ano++;
            this.mes = 1;
            this.dia = 1;
        }
    }

    public static void main(String[] args) {
        // Teste do construtor com parâmetros
        Data data1 = new Data(31, 12, 1900);
        data1.imprimirData(); // Output: 31/12/1900

        // Teste do método proximoDia()
        data1.proximoDia();
        data1.imprimirData(); // Output: 1/1/1901

        // Teste do construtor sem parâmetros
        Data dataAtual = new Data();
        dataAtual.imprimirData();
    }
}
