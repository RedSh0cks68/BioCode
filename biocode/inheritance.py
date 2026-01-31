# biocode/inheritance.py

def punnett_square(parent1, parent2):
    """
    Returns genotype probabilities for a monohybrid cross.
    parent1, parent2: lists of 2 alleles each
    """
    probs = {}
    for a1 in parent1:
        for a2 in parent2:
            genotype = "".join(sorted(a1 + a2))
            probs[genotype] = probs.get(genotype, 0) + 0.25
    return probs
