isTriangle (a, b, c) 
  | a <= 0 || b <= 0 || c <= 0 = "NAOTRI"
  | a == b && b == c && a == c = "equilatero"
  | a /= b && b /= c && a /= c = "escaleno"
  | otherwise = "isosceles"

