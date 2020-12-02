{-#LANGUAGE ScopedTypeVariables#-}

module M1081profileHMM where


import Types
import Data.Matrix
import qualified Data.Map.Strict as MS
import qualified Data.Vector as V
import Data.List hiding (transpose)
import Data.Function

data State =  Ins | Del | Match

processAlignment :: 
        Matrix String 
    ->  [Int]                   -- | List of indices of dropped columns
    ->  Matrix (String, String) -- | (Character, State) 
    ->  Int 
    ->  States
    ->  Transition 
    ->  Transition
processAlignment alignment dropped prevCol 0 states_ transitionHMM
    | elem 0 dropped = 
                let 
                    rows = nrows alignment
                    currCol = getCol 1 alignment
                    colWithStates = colVector $ V.map (\x -> (x, "I0")) currCol
                    newTransition = setElem 1 (1, 2) transitionHMM
                in
                    processAlignment alignment dropped colWithStates 1 states_ newTransition

    | otherwise = 
                let 
                    rows = nrows alignment
                    currCol = getCol 1 alignment
                    colWithStates = colVector $ V.map (\x -> (x, "M1")) currCol  
                    newTransition = setElem 1 (1, 3) transitionHMM
                in
                    processAlignment alignment dropped colWithStates 1 states_ newTransition


processAlignment alignment dropped prevCol idxCurrCol states_ transitionHMM =
                let 
                    (newColWithStates, positions )= getNewCol prevCol currCol idxCurrCol dropped states_
                    currCol = colVector $ getCol (idxCurrCol+1) alignment

                    foldFunction = \matrix ((i,j),val) -> setElem val (i,j) matrix

                    newTransition = foldl foldFunction transitionHMM positions 
                in
                    processAlignment alignment dropped newColWithStates (idxCurrCol + 1) states_ newTransition



-------------------------------------
next :: State -> String -> String
next st str
    | st == Match   = "M" ++ show (num+1)
    | st == Ins     = "I" ++ show (num+1)
    | st == Del     = "D" ++ show (num+1)

    where
        num = read $ return $ str!!1

getNewCol :: 
        Matrix (String, String) 
    ->  Matrix String 
    ->  Int 
    ->  [Int] 
    ->  States 
    ->  (Matrix (String, String), [((Int, Int), Double)])
getNewCol prevCol currCol idxCol dropped states_
    | elem idxCol dropped = 
            let
                currColList = head $ toLists currCol
                pairsStates = zipWith zipFunction (head $ toLists prevCol) (currColList)

                zipFunction = \(char1, state) char2 ->
                                        if char2 == "_" then (state, state)
                                        else (state, next Ins state)

                positions =  getPositions pairsStates states_
            in (,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions
    | otherwise = 
            let
                currColList = head $ toLists currCol
                pairsStates = zipWith zipFunction (head $ toLists prevCol) (currColList)

                zipFunction = \(char1, state) char2 ->
                                        if char2 == "_" then (state, next Del state)
                                        else (state, next Match state)

                positions =  getPositions pairsStates states_
            in (,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions

getPositions :: [(String, String)] -> States -> [((Int, Int), Double)]
getPositions transitions states_ = dictIndexed
    where
        initStatesGroups = groupBy ((==) `on` fst) transitions
        dictStates = MS.fromList $ zip (nub transitions) (repeat 0)
        foldFunc = \group dict->
                        let
                            len = length group
                            subgroups = groupBy ((==) `on` snd) group
                        in  foldr (\subgroup dict->
                                                let
                                                    sublen = length subgroup
                                                in
                                                    MS.insert (subgroup!!0) (sublen/len) dict     
                                            ) dict subgroups
        
        newDict = foldr foldFunc dictStates initStatesGroups

        dictIndexed = map  (\((st1, st2), prob) ->
                                let 
                                    idx1 = states_ MS.! st1
                                    idx2 = states_ MS.! st2
                                in ((idx1, idx2), prob)
                            ) $ MS.toList newDict


droppedCols :: Matrix String -> Double -> [Int]
droppedCols matrix threshold = map snd $ filter (\(a,b) -> a) (zip transposed [1..])
    where
        transposed = toLists $ transpose matrix
        dropped = map   (\col -> 
                            let
                                len = length col
                                empty = len $ filter (=="_")
                            in if empty/len > threshold then True else False
                        ) transposed
        
----------------------------------------------
prepareStates :: Double -> Alphabet -> Matrix String -> States
prepareStates threshold alphabet_ alignment = generateStates lengthStates
    where
        colsToDrop = dropped alignment threshold
        totalCols = ncols alignment
        lengthStates = totalCols - (length colsToDrop)

generateStates :: Int -> States
generateStates len = MS.fromList $ zip statesString [1..]
    where
        source = "S"
        initialIns = "I0"
        intermediate = concatMap (\num -> map (++ show num)["M", "D", "I"])  [1..len]
        sink = "E"
        statesString = source : initialIns : intermediate ++ [sink]
----------------------------------------------

processInput :: [String] -> (Double, Alphabet, [String])
processInput input = (threshold, alphabetHMM, alignment)
    where

        splitt =  splitOn (return "--------") input

        threshold = map return $ (splitt !! 0) !! 0
        
        alphabet_ =  splitt !! 1
        alphabetHMM = MS.fromList $ zip (words (alphabet_!!0)) [1..]

        alignment =  splitt!!2

       


_main = do
    input <- fmap lines $ readFile "../data/profileHMM.txt"
    (threshold, alphabetHMM, alignment) <- return $ processInput input
    states <- return $ prepareStates threshold alphabetHMM alignment
    colsToDrop <- droppedCols alignment threshold
    transitionHMM <- processAlignment alignment colsToDrop (zero 1 1) 0 states (zero (length states) (length states))
    print transitionHMM


