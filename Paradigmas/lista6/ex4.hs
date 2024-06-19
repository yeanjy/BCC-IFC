multiplicaNaturais (0,_) = 0
multiplicaNaturais (_,0) = 0
multiplicaNaturais (x,y)
  | y > 0 = x + multiplicaNaturais(x, y-1)
