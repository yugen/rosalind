# Rosalind ID: DNA
# NOTES: Necleic acids are a type of macromolecule contained in the necleus of a cell.
#        Nucleic acides are polymers, repeating chains of similarly structured molecules known as monomers
#        A monomer ina nucleic acid is known as a nucleotide and is used as a unit of strand (nucleotide) length
#        DNA is a type of nucleic acid (deoxyribose necleic acid) with phosphate bases consisting of adenine (A), cytosine (C), guanine (G), and thymine (T)

# best answer
# * expands iterator to function arguments
# * input() waits for input from the user.
# * String ACGT is coerced to list to be used in map    
print(*map(input().count, "ACGT"))

## My answer
# import sys

# if len(sys.argv) < 2:
#     print("You must submit a sequence string")
#     sys.exit()

# tokens = ['A', 'C', 'G', 'T']
# sequence = sys.argv[1]


# counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0};
# outputString = ''
# for tkn in tokens:
#     cnt = sequence.count(tkn)
#     counts[tkn] = cnt

# print(" ".join(map(lambda x: str(x), counts.values())))


