{-#LANGUAGE ScopedTypeVariables#-}
{-# LANGUAGE CPP #-}

#define traceLoc trace (__FILE__ ++":"++ show __LINE__)


module M1081profileHMM where



import Debug.Trace
import Types
import Data.Matrix hiding (trace)
import qualified Data.Map.Strict as MS
import qualified Data.Vector as V
import Data.List hiding (transpose)
import Data.Function
import Data.List.Split
import GHC.Stack

data State =  Ins | Del | Match deriving (Eq)

processAlignment :: HasCallStack =>
        Matrix String 
    ->  [Int]                   -- ^ List of indices of dropped columns
    ->  Matrix (String, String) -- ^ (Character, State) 
    ->  Int 
    ->  States
    ->  Transition 
    ->  Transition
processAlignment alignment dropped prevCol 1 states_ transitionHMM
    | elem 1 dropped = 
                let 
                    rows = nrows alignment
                    currCol = getCol 1 alignment
                    colWithStates = colVector $ V.map (\x -> (x, "2I0")) currCol
                    newTransition = setElem 1 (1, 2) transitionHMM
                in
                    trace ("FST DEF, FST GUARD OF PROCESS ALIGNMENT " ++ show 1) processAlignment alignment dropped colWithStates 2 states_ $! newTransition

    | otherwise = 
                let 
                    rows = nrows alignment
                    currCol = getCol 1 alignment
                    colWithStates = colVector $ V.map (\x -> (x, "3M1")) currCol  
                    newTransition = setElem 1 (1, 3) transitionHMM
                in
                    trace ("FST DEF, SEC GUARD OF PROCESS ALIGNMENT " ++ show 1) processAlignment alignment dropped colWithStates 2 states_ $! newTransition


processAlignment alignment dropped prevCol idxCurrCol states_ transitionHMM
    | idxCurrCol > ncols alignment = transitionHMM
    | otherwise = 
                let 
                    (newColWithStates, positions )= getNewCol prevCol currCol idxCurrCol dropped states_
                    currCol = colVector $ getCol (idxCurrCol+1) alignment

                    foldFunction = \matrix ((i,j),val) -> setElem val (i,j) matrix

                    newTransition = foldl foldFunction transitionHMM positions 
                in
                    trace ("SEC DEF, SEC GUARD OF PROCESS ALIGNMENT " ++ show idxCurrCol) processAlignment alignment dropped newColWithStates (idxCurrCol + 1) states_ $! newTransition



-------------------------------------
next :: HasCallStack => State -> String -> String
next st str
    | st == Match   = trace ("IN NEXT M " ++ str ++ "  " ++ ((show $ 3*(num+1) + 0) ++ "M" ++ show (num+1))) (show $ 3*num + 0) ++ "M" ++ show (num+1)
    | st == Del     = trace ("IN NEXT D " ++ str ++ "  " ++ ((show $ 3*(num+1) + 1) ++ "D" ++ show (num+1))) (show $ 3*num + 1) ++ "D" ++ show (num+1)
    | st == Ins     = trace ("IN NEXT I " ++ str ++ "  " ++ ((show $ 3*(num+1) + 2) ++ "I" ++ show (num+1))) (show $ 3*num + 2) ++ "I" ++ show (num+1)
    
    where
        pref = read $ return $ str!!0
        nextPref = pref + 3
        num = read $ return $ str!!2

getNewCol :: HasCallStack =>
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
            in trace ("NEW VECTOR \n" ++ show ((,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions)) (,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions
    | otherwise = 
            let
                currColList = head $ toLists currCol
                pairsStates = zipWith zipFunction (head $ toLists prevCol) (currColList)

                zipFunction = \(char1, state) char2 ->
                                        if char2 == "_" then (state, next Del state)
                                        else (state, next Match state)

                positions =  getPositions pairsStates states_
            in trace ("NEW VECTOR \n" ++ show ((,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions)) (,) (colVector $ V.fromList $ zip currColList (map snd pairsStates)) positions

getPositions :: HasCallStack => [(String, String)] -> States -> [((Int, Int), Double)]
getPositions transitions states_ = trace ("IN GET POSITIONS   " ++  show dictIndexed) dictIndexed
    where
        initStatesGroups = groupBy ((==) `on` fst) transitions
        dictStates = MS.fromList $ zip (nub transitions) (repeat 0)
        foldFunc = \group dict->
                        let
                            len = fromIntegral $ length group
                            subgroups = groupBy ((==) `on` snd) group
                        in  foldr (\subgroup dict->
                                                let
                                                    sublen = fromIntegral $ length subgroup
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


droppedCols :: HasCallStack => Matrix String -> Double -> [Int]
droppedCols matrix threshold = trace ("in dropped " ++ show dropped) map snd $ filter (\(a,b) -> a) (zip dropped [1..])
    where
        transposed = toLists $ transpose matrix
        dropped =  map   (\col -> 
                                    let
                                        len     = fromIntegral $ length col
                                        empty   = fromIntegral $ length $ filter (== "-") col
                                    in if empty/len > threshold then True else False
                                ) transposed
        
----------------------------------------------
prepareStates :: HasCallStack =>  Double -> Alphabet -> Matrix String -> States
prepareStates threshold alphabet_ alignment = trace ("IN PREPARE STATES " ++  (show $ generateStates lengthStates)) generateStates lengthStates
    where
        colsToDrop = droppedCols alignment threshold
        totalCols = ncols alignment
        lengthStates = totalCols - (length colsToDrop)

generateStates :: HasCallStack => Int -> States
generateStates len = trace ("LEN  " ++ show len ) MS.fromList $ zip statesString [1..]
    where
        source = "1S"
        initialIns = "2I0"
        intermediate = concatMap (\num -> map (++ show num)[show (3*num) ++ "M", show (3*num +1) ++ "D", show (3*num+2) ++ "I"])  [1..len]
        sink = "E"
        statesString = source : initialIns : intermediate ++ [sink]
----------------------------------------------

processInput :: HasCallStack => [String] -> (Double, Alphabet, Matrix String)
processInput input = (threshold, alphabetHMM, alignment)
    where

        splitt =  splitOn (return "--------") input

        threshold = read $ head (splitt !! 0)
        
        alphabet_ =  splitt !! 1
        alphabetHMM = MS.fromList $ zip (words (alphabet_!!0)) [1..]

        alignment = fromLists $ map (map return) $ splitt!!2

       


_main = do
    input <- fmap lines $ readFile "data/profileHMM.txt"
    (threshold, alphabetHMM, alignment) <- return $ processInput input
    states <- return $ prepareStates threshold alphabetHMM alignment
    colsToDrop <- return $ droppedCols alignment threshold
    transitionHMM <- return $ processAlignment alignment colsToDrop (matrix 1 1 (\_ -> ("", ""))) 1 states (zero (length states) (length states))
    print transitionHMM


