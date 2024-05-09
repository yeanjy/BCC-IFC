public class labeledloop {
  public static void main(String[] args) {
    outer:
    for (int i = 0; i < 10; i++) {
      System.out.println("Loop de fora: " + i);
      for (int j = 0; j < 10; j++) {
        System.out.println("Loop de dentro: " + j);
        if(i==7 && j==7) 
          break outer;
     } 
    }
  }  
}
