# biocode/__init__.py

# Gene module
from .gene import Gene

# Sequence module
from .sequence import DNA, RNA

# Mutations module
from .mutations import snp, insertion, deletion

# Inheritance module
from .inheritance import punnett_square

# Population genetics module
from .population import hardy_weinberg

# Utilities
from .utils import count_nucleotides

from .utils import printh

from .graph import graph



# Optional: you can add __all__ for cleaner imports in "from biocode import *"
__all__ = [
    "Gene",
    "DNA",
    "RNA",
    "snp",
    "insertion",
    "deletion",
    "punnett_square",
    "hardy_weinberg",
    "count_nucleotides",
    "printh",
]
