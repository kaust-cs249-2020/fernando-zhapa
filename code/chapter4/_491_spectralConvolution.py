import sys
sys.path.append('..')

from lib import spacedPrint

def spectralConvolution(spectrum):
    # Input: A collection of integers Spectrum.
    # Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order.
    spectral = []
    for i in range(0,len(spectrum)):
        for j in range(len(spectrum)-1,i,-1):
            diff = spectrum[j] - spectrum[i]
            if diff != 0:
                spectral.append(diff)
    return spectral

if __name__ == "__main__":
    
    file = open('data/spectralConvolution.txt', 'r')

    spectrum = [int(i) for i in file.readline().rstrip('\n').split(' ')]

    spacedPrint(spectralConvolution(spectrum))