# biocode/gene.py

class Gene:
    """
    Represents a gene with alleles and allows genotype/phenotype calculations.
    """

    def __init__(self, name, alleles, dominance=None):
        self.name = name
        self.alleles = alleles
        # Default all alleles to unknown dominance if not provided
        self.dominance = dominance or {allele: "unknown" for allele in alleles}

    def genotype_probability(self, parent1_alleles, parent2_alleles):
        """
        Computes offspring genotype probabilities using a Punnett square.

        parent1_alleles, parent2_alleles: lists of two alleles each, e.g., ["R", "r"]
        Returns: dict of genotype -> probability
        """
        probs = {}
        for a1 in parent1_alleles:
            for a2 in parent2_alleles:
                genotype = "".join(sorted(a1 + a2))
                probs[genotype] = probs.get(genotype, 0) + 0.25
        return probs

    def phenotype_probability(self, parent1_alleles, parent2_alleles):
        """
        Computes phenotype probabilities based on allele dominance.
        Returns: dict of phenotype -> probability
        """
        genotype_probs = self.genotype_probability(parent1_alleles, parent2_alleles)
        phenotype_probs = {}

        for genotype, prob in genotype_probs.items():
            phenotype = self._genotype_to_phenotype(genotype)
            phenotype_probs[phenotype] = phenotype_probs.get(phenotype, 0) + prob

        return phenotype_probs

    def _genotype_to_phenotype(self, genotype):
        """
        Converts a genotype to a phenotype based on dominance rules.
        """
        for allele in genotype:
            if self.dominance.get(allele) == "dominant":
                return f"{self.name}_dominant"
        return f"{self.name}_recessive"
