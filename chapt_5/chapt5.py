# a function to take a protein seq and amino acid
# returns the percent of the protein made up by the acid
def percent_acid(protein, amino_acid):
    return protein.upper().count(amino_acid.upper()) / len(protein) * 100


assert percent_acid("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert percent_acid("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert percent_acid("msrslllrfllfllllpplp", "L") == 50
assert percent_acid("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

# takes a list and accumulates protein content of all of the amino acids in the list
def percent_acids(protein, amino_acids=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    total_percent = 0
    for acid in amino_acids:
        total_percent += percent_acid(protein, acid)
    return total_percent


assert percent_acids("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert percent_acids("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]) == 55
assert percent_acids("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]) == 70
assert percent_acids("MSRSLLLRFLLFLLLLPPLP") == 65
