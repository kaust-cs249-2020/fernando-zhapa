module H_221_exerciseBreak where

import Data.Function

fact :: Integer -> Integer
fact n
    | n < 0 = -1
    | n == 1 = 1
    | otherwise = n * fact (n-1)

choose :: Integer -> Integer -> Integer
choose n k = (fact n) `div` ((fact k) * (fact (n-k)))

approxProbAtLeastT :: 
    Integer -> -- length of the whole text
    Integer -> -- length of the alphabet
    Integer -> -- length of the k-mer
    Integer -> -- number of minimum times expected to occur
    Maybe Rational
approxProbAtLeastT n a k t 
    | n-t*(k-1) < t = Nothing
    | otherwise = Just $ ((/) `on` toRational) (choose (n-t*(k-1)) t) (a^(t*k)) 

approxProbExactT :: Integer -> Integer -> Integer -> Integer -> Maybe Rational
approxProbExactT n a k t
    | probNext == Nothing = probCurr
    | otherwise = (-) <$> probCurr <*> probNext
    where
        probCurr = approxProbAtLeastT n a k t
        probNext = approxProbAtLeastT n a k (t+1)


n = 1000
a = 4
k = 9
ts = [1..(n `div` k)]

probs = map (\t -> approxProbExactT n a k t) ts
expectedValue = foldr1 (\a b -> (+) <$> a <*> b) probs

main :: IO ()
main = do
    putStrLn $ show (fmap (fromRational . (500 *)) expectedValue)