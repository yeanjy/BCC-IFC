#include <iostream>

class fatorial
{
public:
  long int recursiveFatorial(int n)
  {
    if(n<2)
    {
      return 1;
    }
    else {
      return n*recursiveFatorial(n-1);
    }
  }

  long int forFatorial(int n)
  {
    long int res = 1;
    for (int i  = n; i > 0 ; i--)
    {
      res *= i; 
    }
    return res;
  }
};

class FactoryMethod{
public:
  long int getFatorialMethod(bool isRercusive, int n){
    fatorial f;
    if (isRercusive)
    {
      return f.recursiveFatorial(n);
    }
    else {
      return f.forFatorial(n);  
    }
  }
}; 

int main()
{
  FactoryMethod f;
  std::cout << f.getFatorialMethod(false, 5) << std::endl;
  return 0;
}
