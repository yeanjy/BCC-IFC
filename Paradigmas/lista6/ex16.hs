filtraLista :: (Eq a) => [a] -> [a]
filtraLista [] = []
filtraLista (x:xs) = x : filtraLista (filter (/= x) xs)
