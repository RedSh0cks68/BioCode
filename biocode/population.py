# biocode/population.py

def hardy_weinberg(p):
    """
    Calculate genotype frequencies under Hardy-Weinberg equilibrium.
    p: frequency of dominant allele
    Returns: dict with 'AA', 'Aa', 'aa' frequencies
    """
    q = 1 - p
    return {'AA': p**2, 'Aa': 2*p*q, 'aa': q**2}
