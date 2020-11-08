from dictionaries import molecularMassesNoRepeat
from joblib import Parallel, delayed
import multiprocessing

def countPeptidesWithMass(mass, currMass = 0):
    numberPeptides = 0
    for _, value in molecularMassesNoRepeat.items():
        newMass = currMass + value
        if newMass == mass:
            numberPeptides += 1
        elif newMass < mass:
            numberPeptides += countPeptidesWithMass(mass, newMass)
    return numberPeptides
    

def auxCountPeptideWithMass(mass, index, currMass = 0):
    numberPeptides = 0
    masses = [*molecularMassesNoRepeat.values()]
    aminoMass = masses[index]
    newMass = currMass + aminoMass
    if newMass == mass:
        numberPeptides += 1
    elif newMass < mass:
        numberPeptides += countPeptidesWithMass(mass, newMass)
    return numberPeptides

    
def parallelCountPeptidesWithMass(mass, currMass = 0):
    
    inputs = range(len(molecularMassesNoRepeat))
    num_cores = multiprocessing.cpu_count()

    numberPeptides = sum(Parallel(n_jobs=num_cores)(delayed(auxCountPeptideWithMass)(mass,i) for i in inputs))

    return numberPeptides


if __name__ == "__main__":
    
    mass = 1024

    print(parallelCountPeptidesWithMass(mass))