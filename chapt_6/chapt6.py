"""
various conditional statement practice problems with input coming from .csv file
"""

# function to return AT content
def at_content(seq):
    """ function to return AT content"""
    seq = seq.upper()
    AT_content = seq.count("A") + seq.count("T")
    return AT_content / len(seq)


# opens file and stores lines in list
with open("input/data.csv") as file:
    data = file.readlines()

# prints gene names is the species is D. melanogaster or D. simulans
# new line print at end of loop is to separate outputs from different exercise sections
for line in data:
    spec_name, sequence, gene_name, expression_level = line.split(",")
    expression_level = int(expression_level.strip())
    if "Drosophila melanogaster" in spec_name or "Drosophila simulans" in spec_name:
        print(gene_name)
print("\n")

# prints gene name if length of sequence is between 90 and 110
for line in data:
    spec_name, sequence, gene_name, expression_level = line.split(",")
    expression_level = int(expression_level.strip())
    length = len(sequence)
    if 90 < length < 110:
        print(gene_name)
print("\n")

# prints gene names if AT content is greater than 0.5 and exp level > 200
for line in data:
    spec_name, sequence, gene_name, expression_level = line.split(",")
    expression_level = int(expression_level.strip())
    if at_content(sequence) > 0.5 and expression_level > 200:
        print(gene_name)
print("\n")

# prints gene name for species other than D. melanogaster if it starts with k or h
for line in data:
    spec_name, sequence, gene_name, expression_level = line.split(",")
    expression_level = int(expression_level.strip())
    if "Drosophila melanogaster" != spec_name and (
        gene_name.startswith("k") or gene_name.startswith("h")
    ):
        print(gene_name)
print("\n")

# prints message stating whether AT content is high, medium or low
for line in data:
    spec_name, sequence, gene_name, expression_level = line.split(",")
    expression_level = int(expression_level.strip())
    qual_at_content = None
    if at_content(sequence) > 0.65:
        qual_at_content = "High"
    elif at_content(sequence) < 0.45:
        qual_at_content = "Low"
    else:
        qual_at_content = "Medium"
    print(f"The AT content for {gene_name} is {qual_at_content}")
