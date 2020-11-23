{-# LANGUAGE TemplateHaskell, ScopedTypeVariables #-}


module Types where

import qualified Data.Map.Strict as MS
import Data.Matrix
import Control.Lens

type Alphabet   = MS.Map String Int
type States     = MS.Map String Int
type Transition = Matrix Double
type Emission   = Matrix Double


data HMM = HMM 
            {
                _alphabet   :: Alphabet,
                _states     :: States,
                _transition :: Transition,
                _emission   :: Emission
            }

makeLenses ''HMM





type Col = Matrix Double