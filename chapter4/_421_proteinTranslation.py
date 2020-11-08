from dictionaries import geneticCode

def proteinTranslation(rna, geneticCode):

    # Input: An RNA string Pattern and the array GeneticCode.
    # Output: The translation of Pattern into an amino acid string Peptide.
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        aminoacid = geneticCode[codon]
        if aminoacid != "*":
            protein += aminoacid
        else:
            break
    return protein


if __name__ == "__main__":
    
    file = open("data/proteinTranslation.txt")

    rna = file.readline()

    print(proteinTranslation(rna, geneticCode))
