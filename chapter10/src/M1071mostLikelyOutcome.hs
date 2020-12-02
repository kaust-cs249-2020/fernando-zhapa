module M1071mostLikelyOutcome where

import Types
import qualified Data.Map.Strict as MS
import Data.Matrix hiding (trace)
import qualified Data.Vector as V
import Control.Lens
import Data.Function
import Data.List hiding (transpose)
import Data.Ord
import Debug.Trace
import M1061Viterbi (submatrix', setCol)
import Data.List.Split


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
                            newCol = (zipWith (\x list -> foldr1 (+) (map (x*) (zipWith (*) prevCol list))) colToList transitionMatrix)
                        in (colVector $ V.fromList newCol)

        updatedViterbiGraph = setCol column (processCol (getCol column viterbiGraph)) viterbiGraph
        

-- maxi :: Ord a => [a] -> (a, Int)
-- maxi xs = maximumBy (comparing fst) (zip xs [0..])


-- backTracking :: Matrix Double -> Int -> Matrix Double -> [Int] -> [Int]
-- backTracking viterbiGraph column transitionHMM path
--     | column == 1 = path
--     | otherwise = backTracking viterbiGraph (column-1) transitionHMM $! (snd newChosen:path)

--     where
--         prevCol = V.toList $ getCol (column-1) viterbiGraph
--         actualChosen = (head path) + 1
        
--         transitionCol = V.toList $ getCol actualChosen transitionHMM
--         newChosen = maxi $ zipWith (*) prevCol transitionCol


mostLikelyOutcome :: [String] -> HMM -> Double
mostLikelyOutcome sequence hmm =  foldr1 (+) $ V.toList $ getCol cols viterbiForward
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



        -- pathInIdxs = backTracking viterbiForward cols transitionHMM [snd $ maxi $ V.toList $ getCol cols viterbiForward]

        -- path = map (\x -> head [ k |  k <- MS.keys statesHMM, (statesHMM MS.! k) == x+1 ]) pathInIdxs


processInput :: [String] -> ([String], HMM)
processInput input = (sequence, hmm)
    where

        splitt =  splitOn (return "--------") input

        sequence = map return $ (splitt !! 0) !! 0
        
        alphabet_ =  splitt !! 1
        alphabetHMM = MS.fromList $ zip (words (alphabet_!!0)) [1..]

        states_ = splitt !! 2
        statesHMM = MS.fromList $ zip (words (states_!!0)) [1..]

        transition_ = splitt !! 3
        rowsTransition = map ((map (read)) . tail.words) $ tail transition_
        transitionHMM = fromLists rowsTransition

        
        emission_ = splitt !! 4
        rowsEmission = map ((map (read)) . tail.words) $ tail emission_
        emissionHMM = fromLists rowsEmission

        hmm = HMM alphabetHMM statesHMM transitionHMM emissionHMM


_main = do
    input <- fmap lines $ readFile "../data/mostLikelyOutcome.txt"
    (sequence, hmm) <- return $ processInput input
    path <- return $ mostLikelyOutcome sequence hmm
    print path
