# biocode/graph.py
"""
BIOCODE Graph Module
Provides visualization tools for biological data.
"""

import matplotlib.pyplot as plt


class Graph:
    """
    Graphing utilities for BIOCODE.
    Accessed via: bc.graph
    """

    def plot_allele_frequencies(self, allele_freqs):
        """
        Plot allele frequencies as a bar chart.

        Parameters:
            allele_freqs (dict): {"A": 0.4, "a": 0.6}
        """
        if not isinstance(allele_freqs, dict):
            raise TypeError("allele_freqs must be a dictionary")

        if not allele_freqs:
            raise ValueError("allele_freqs cannot be empty")

        alleles = list(allele_freqs.keys())
        freqs = list(allele_freqs.values())

        plt.figure()
        plt.bar(alleles, freqs)
        plt.xlabel("Allele")
        plt.ylabel("Frequency")
        plt.title("Allele Frequencies")
        plt.ylim(0, 1)
        plt.show()

    def plot_genotype_distribution(self, genotype_counts):
        """
        Plot genotype distribution.

        Parameters:
            genotype_counts (dict): {"AA": 10, "Aa": 20, "aa": 5}
        """
        if not isinstance(genotype_counts, dict):
            raise TypeError("genotype_counts must be a dictionary")

        labels = list(genotype_counts.keys())
        values = list(genotype_counts.values())

        plt.figure()
        plt.bar(labels, values)
        plt.xlabel("Genotype")
        plt.ylabel("Count")
        plt.title("Genotype Distribution")
        plt.show()


# 🔑 THIS LINE MAKES bc.graph WORK
graph = Graph()

__all__ = ["graph", "Graph"]
