import java.util.Random;
public class labeledloop {
  public static void main(String[] args) {
    Random generate = new Random();
    outer:
    for (int i = 0; i < 10; i++) {
      System.out.println("Loop de fora: " + i);
      for (int j = 0; j < 10; j++) {
        System.out.println("Loop de dentro: " + j);
        if(i==generate.nextInt(10) && j==generate.nextInt(10))  
          break outer;
     } 
    }
  }  
}
