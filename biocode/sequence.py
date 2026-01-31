# biocode/sequence.py

class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def complement(self):
        return self.sequence.translate(str.maketrans("ATCG", "TAGC"))
    
    def reverse_complement(self):
        return self.complement()[::-1]
    
    def transcribe(self):
        """DNA -> RNA transcription"""
        return self.sequence.replace("T", "U")
    
    def gc_content(self):
        gc_count = self.sequence.count("G") + self.sequence.count("C")
        return gc_count / len(self.sequence) * 100

class RNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def translate(self):
        """Translate RNA to protein sequence"""
        codon_table = {
            'AUG':'M', 'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
            'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
            'AUU':'I', 'AUC':'I', 'AUA':'I',
            'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
            # … add the full codon table for completeness
        }
        protein = ""
        for i in range(0, len(self.sequence)-2, 3):
            codon = self.sequence[i:i+3]
            protein += codon_table.get(codon, "X")  # X = unknown codon
        return protein
