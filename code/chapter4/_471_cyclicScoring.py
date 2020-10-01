from _4111_theoreticalSpectrum import cyclicSpectrum
from dictionaries import molecularMasses

def cScore(peptide, spectrum):
    # Input: An amino acid string Peptide and a collection of integers Spectrum.
    # Output: The score of cyclic spectrum of peptide against Spectrum, Score(Peptide, Spectrum).
    peptideSpec = []
    peptideSpec = cyclicSpectrum(peptide)
    score = 0
    accPep = 0
    accSpec = 0

    while accSpec < len(spectrum) and accPep < len(peptideSpec):
        if peptideSpec[accPep] == spectrum[accSpec]:
            score += 1
            accSpec += 1
            accPep += 1 
        elif peptideSpec[accPep] < spectrum[accSpec]:
            accPep += 1
        else:
            accSpec += 1
    return score


if __name__ == "__main__":
    
    file = open('data/score.txt','r')

    peptide = file.readline().rstrip('\n')
    spectrum = [ int(i) for i in file.readline().rstrip('\n').split(' ')]

    print(cScore(peptide, spectrum))