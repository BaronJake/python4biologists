"""
Various regex practice problems using a list of accession numbers
"""
import re

accessions = [
    "xkn59438",
    "yhdck2",
    "eihd39d9",
    "chdsye847",
    "hedle3455",
    "xjhd53e",
    "45da",
    "de37dp",
]

# prints accession number if it contains a 5
for accession in accessions:
    if re.search(r".*5.*", accession):
        print(accession)
print("\n")

# prints accession number if it contains a d or e
for accession in accessions:
    if re.search(r".*[de].*", accession):
        print(accession)
print("\n")

# prints accession number if it contains a d and e in that order
for accession in accessions:
    if re.search(r".*d.*e.*", accession):
        print(accession)
print("\n")

# prints accession number if it contains a d and e with a single letter between them
for accession in accessions:
    if re.search(r".*d\w{1}e.*", accession):
        print(accession)
print("\n")

# prints accession number if it contains a do and e in any order
# The solution in the book doesn't seem to find all of the matches
for accession in accessions:
    if re.search(r".*(d.*e|e.*d).*", accession):
        print(accession)
print("\n")

# prints accession number if it starts with x or y
for accession in accessions:
    if re.search(r"^[xy]", accession):
        print(accession)
print("\n")

# prints accession number if it starts with x or y and ends with e
for accession in accessions:
    if re.search(r"^[xy].*e$", accession):
        print(accession)
print("\n")

# prints accession number if it ends with a d followed by either a,r,p
for accession in accessions:
    if re.search(r"\d{3,}", accession):
        print(accession)
print("\n")

for accession in accessions:
    if re.search(r".*d[arp]$", accession):
        print(accession)
