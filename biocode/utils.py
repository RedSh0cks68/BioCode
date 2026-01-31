# biocode/utils.py
import os

def count_nucleotides(sequence):
    sequence = sequence.upper()
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'U': sequence.count('U')
    }

# biocode/utils.py

def printh(term):
    """
    Specialized print helper for biology terms.
    Usage: printh("H-Gene") or printh("H-DNA")
    
    Looks for a text file in 'biocode/docs/' folder with name 'H-<term>.txt'
    and prints the path to the file.
    """
    # Ensure term starts with H- (optional check)
    if not term.startswith("H-"):
        term = f"H-{term}"
    
    # Build path to docs folder
    docs_folder = os.path.join(os.path.dirname(__file__), "docs")
    file_path = os.path.join(docs_folder, f"{term}.txt")
    
    if os.path.isfile(file_path):
        print(f"View info about {file_path}")
    else:
        print(f"No documentation found for '{term}'.")

