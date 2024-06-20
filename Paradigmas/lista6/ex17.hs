primeirosN :: Int -> [a] -> [a]
primeirosN n _   
  | n <= 0 = []   
primeirosN _ [] = [] 
primeirosN n (x:xs) = x : primeirosN (n - 1) xs
