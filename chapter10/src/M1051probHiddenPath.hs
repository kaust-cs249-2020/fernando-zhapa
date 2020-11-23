{-# LANGUAGE ScopedTypeVariables #-}

module M1051probHiddenPath where


import qualified Data.Map.Strict as MS
import Data.Matrix
import Data.Function
import Control.Lens

import Types

    

probHiddenPath :: [String] -> HMM -> Double
probHiddenPath path hmm = snd $ foldl foldFunction (head path, initialProb) (tail path)
    where
        statesHMM =  hmm^. states
        transitionHMM = hmm^.transition

        initialProb = ((/) `on` fromIntegral) 1 (length statesHMM)

        foldFunction = \(prevState, accProb ) currState -> 
                                let idxPrev = statesHMM MS.! prevState
                                    idxCurr = statesHMM MS.! currState
                                    prob = getElem idxPrev idxCurr transitionHMM

                                in (currState, accProb*prob)


processInput :: [String] -> ([String], HMM)
processInput input = (path, hmm)
    where
        path = map return $ input !! 0
        statesHMM = MS.fromList $ zip (words (input!!2)) [1..]
        
        row1 = map read $ tail (words (input!!5))
        row2 = map read $ tail (words (input!!6))

        transition = fromLists [row1, row2]

        hmm = HMM MS.empty statesHMM transition (zero 1 1)



_main = do
    input <- fmap lines $ readFile "data/probHiddenPath.txt"
    (path, hmm) <- return $ processInput input
    prob <- return $ probHiddenPath path hmm
    print prob
