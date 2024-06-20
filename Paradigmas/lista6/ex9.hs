listaAbsoluta :: (Enum a, Num a , Ord a) => a -> [a]
listaAbsoluta n = [0..abs n]
