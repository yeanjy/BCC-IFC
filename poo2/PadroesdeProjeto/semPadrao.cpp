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

int main()
{
  fatorial f;
  std::cout << f.recursiveFatorial(3) << std::endl;
}
