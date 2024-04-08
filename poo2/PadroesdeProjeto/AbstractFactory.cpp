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

class AbstractFactory{
public:
  virtual long int getFatorial(int n) = 0;
  virtual ~AbstractFactory() = default;
};

class forFatorialFactory : public AbstractFactory{
public:
  long int getFatorial(int n) override{
    fatorial f;
    return f.forFatorial(n);
  }
  
  ~forFatorialFactory() = default;
};

class recursiveFactory : public AbstractFactory{
public:
  long getFatorial(int n) override{
    fatorial f;
    return f.recursiveFatorial(n);
  }

  ~recursiveFactory() = default;
};

int main(){
  AbstractFactory *f  = new forFatorialFactory();  
  std::cout << f->getFatorial(4) <<std::endl;

  AbstractFactory *ff = new recursiveFactory();
  std::cout << ff->getFatorial(7) << std::endl;

  delete f;
  return 0;
}
