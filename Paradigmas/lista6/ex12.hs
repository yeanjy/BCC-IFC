import Data.Char (isLower)

soMinusculas :: String -> String
soMinusculas str = filter isLower str
