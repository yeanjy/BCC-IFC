multiplica(x, y)
  | y == 0 = 0
  | y > 0 = x + multiplica(x, y-1)
  | y < 0 = -multiplica(x, -y)
