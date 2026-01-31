# biocode/mutations.py

def snp(sequence, position, new_base):
    """
    Single Nucleotide Polymorphism (SNP)
    position: 0-based index
    new_base: new nucleotide
    """
    seq_list = list(sequence.upper())
    seq_list[position] = new_base.upper()
    return "".join(seq_list)

def insertion(sequence, position, insertion_seq):
    """Insert a sequence at the given position"""
    return sequence[:position] + insertion_seq.upper() + sequence[position:]

def deletion(sequence, position, length=1):
    """Delete `length` nucleotides starting from `position`"""
    return sequence[:position] + sequence[position+length:]
