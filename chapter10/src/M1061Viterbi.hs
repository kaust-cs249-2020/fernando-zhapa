module M1061Viterbi where

import Types
import qualified Data.Map.Strict as MS
import Data.Matrix hiding (trace)
import qualified Data.Vector as V
import Control.Lens
import Data.Function
import Data.List hiding (transpose)
import Data.Ord
import Debug.Trace

submatrix' :: (Int, Int) -> (Int, Int) -> Matrix Double -> Matrix Double
submatrix' (srow, erow) (scol, ecol) = submatrix srow erow scol ecol 

setCol :: Int -> Col -> Matrix Double -> Matrix Double
setCol idx col mat 
    | idx == 1 = col <|> right
    | idx == (ncols mat) = left <|> col
    | otherwise = left <|> col <|> right
    where
        left = submatrix' (1,(nrows mat)) (1,idx-1) mat
        right = submatrix' (1,(nrows mat)) (idx+1, (ncols mat)) mat

dynamicPart :: Matrix Double -> Transition -> Double -> Int -> Matrix Double
dynamicPart viterbiGraph transitionHMM initialProb column
    | column == 1 = dynamicPart (mapCol (\_ x -> x*initialProb) column viterbiGraph) transitionHMM 1 $! column+1
    | column > ncols viterbiGraph = viterbiGraph
    | otherwise = dynamicPart updatedViterbiGraph transitionHMM 1 $! column+1
    where
        transitionMatrix = (toLists $ transpose transitionHMM)
        prevCol = V.toList $ getCol (column-1) viterbiGraph
        processCol = \col -> 
                        let
                            colToList = (V.toList col)
                            newCol = (zipWith (\x list -> foldr1 max (map (x*) (zipWith (*) prevCol list))) colToList transitionMatrix)
                        in (colVector $ V.fromList newCol)

        updatedViterbiGraph = setCol column (processCol (getCol column viterbiGraph)) viterbiGraph
        

maxi :: Ord a => [a] -> (a, Int)
maxi xs = maximumBy (comparing fst) (zip xs [0..])


backTracking :: Matrix Double -> Int -> Matrix Double -> [Int] -> [Int]
backTracking viterbiGraph column transitionHMM path
    | column == 1 = path
    | otherwise = backTracking viterbiGraph (column-1) transitionHMM $! (snd newChosen:path)

    where
        prevCol = V.toList $ getCol (column-1) viterbiGraph
        actualChosen = (head path) + 1
        
        transitionCol = V.toList $ getCol actualChosen transitionHMM
        newChosen = maxi $ zipWith (*) prevCol transitionCol


viterbi :: [String] -> HMM -> String
viterbi sequence hmm = trace (show viterbiForward) concat path
    where
        emissionHMM = hmm^.emission
        alphabetHMM = hmm^.alphabet
        transitionHMM = hmm^.transition
        statesHMM   = hmm^.states
        cols = length sequence
        initialProb = ((/) `on` fromIntegral) 1 (length statesHMM)
        emissions = \x -> let
                            idxAlphabet = alphabetHMM MS.! x
                        in getCol idxAlphabet emissionHMM   
        
        

        viterbiGraph = foldl1 (<|>) $ map (colVector. emissions) sequence

        viterbiForward = dynamicPart viterbiGraph transitionHMM initialProb 1

        pathInIdxs = backTracking viterbiForward cols transitionHMM [snd $ maxi $ V.toList $ getCol cols viterbiForward]

        path = map (\x -> head [ k |  k <- MS.keys statesHMM, (statesHMM MS.! k) == x+1 ]) pathInIdxs


processInput :: [String] -> ([String], HMM)
processInput input = (sequence, hmm)
    where
        sequence = map return $ input !! 0
        
        alphabetHMM = MS.fromList $ zip (words (input!!2)) [1..]

        statesHMM = MS.fromList $ zip (words (input!!4)) [1..]

        row1 = map read $ tail (words (input!!7))
        row2 = map read $ tail (words (input!!8))
        
        transitionHMM = fromLists [row1, row2]

        row3 = map read $ tail (words (input!!11))
        row4 = map read $ tail (words (input!!12))
        
        emissionHMM = fromLists [row3, row4]
        -- row1 = map read $ tail (words (input!!7))
        -- row2 = map read $ tail (words (input!!8))
        -- row3 = map read $ tail (words (input!!9))
        -- row4 = map read $ tail (words (input!!10))

        -- transitionHMM = fromLists [row1, row2, row3, row4]

        -- row5 = map read $ tail (words (input!!13))
        -- row6 = map read $ tail (words (input!!14))
        -- row7 = map read $ tail (words (input!!15))
        -- row8 = map read $ tail (words (input!!16))

        -- emissionHMM = fromLists [row5, row6, row7, row8]

        hmm = HMM alphabetHMM statesHMM transitionHMM emissionHMM


_main = do
    input <- fmap lines $ readFile "data/viterbi.txt"
    (sequence, hmm) <- return $ processInput input
    path <- return $ viterbi sequence hmm
    print path
