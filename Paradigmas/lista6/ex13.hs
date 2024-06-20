import Data.Char (toUpper)
substituiVogais :: [Char] -> [Char]
substituiVogais str = map substituir str
  where
    substituir c
      | c `elem` "aeiou" = toUpper c
      | otherwise = c
