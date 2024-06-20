clonaNumeros :: [a] -> [a]
clonaNumeros [] = []
clonaNumeros (x:xs) = x : x : clonaNumeros xs
