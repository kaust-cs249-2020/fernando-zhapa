module M1052probOutcomeGivenPath where


import qualified Data.Map.Strict as MS
import Control.Lens
import Data.Matrix


import Types

probOutcomeGivenPath :: [String] -> [String] -> HMM -> Double
probOutcomeGivenPath sequence path hmm = foldl foldFunction 1 seqPath
    where
        alphabetHMM = hmm^.alphabet
        statesHMM = hmm^.states
        emissionHMM = hmm^.emission
        seqPath = zip sequence path

        foldFunction = \prob (outcome, state) ->  
                                let idxAlphabet = alphabetHMM MS.! outcome
                                    idxState = statesHMM MS.! state
                                    nextProb = getElem idxState idxAlphabet emissionHMM

                                in prob*nextProb



processInput :: [String] -> ([String], [String], HMM)
processInput input = (sequence, path, hmm)
    where
        sequence = map return $ input !! 0
        
        alphabetHMM = MS.fromList $ zip (words (input!!2)) [1..]

        path = map return $ input !! 4

        statesHMM = MS.fromList $ zip (words (input!!6)) [1..]
        
        row1 = map read $ tail (words (input!!9))
        row2 = map read $ tail (words (input!!10))

        emissionHMM = fromLists [row1, row2]

        hmm = HMM alphabetHMM statesHMM (zero 1 1) emissionHMM


_main = do
    input <- fmap lines $ readFile "data/probOutcomeGivenPath.txt"
    (sequence, path, hmm) <- return $ processInput input
    prob <- return $ probOutcomeGivenPath sequence path hmm
    print prob
