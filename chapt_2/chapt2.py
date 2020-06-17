# prints AT content
seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
AT = (seq.count("A") + seq.count("T")) / len(seq)
print(AT)

# creates a complementary sequence
# uses lowercase to prevent subsequent lines replacing already replaced bases
compseq = seq.replace("A", "t")
compseq = compseq.replace("T", "a")
compseq = compseq.replace("C", "g")
compseq = compseq.replace("G", "c")
print(compseq.upper())

# finds a sequence and prints its range
nseq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ind = nseq.find("GAATTC")
print(ind + 1, len(nseq) - ind - 1)

# takes out the exons, leaving only coding sequence
# prints coding sequence and percent coding and sequence with exons lowercase
introns = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
coding = introns[:63] + introns[90:]
print(coding)
print(len(coding) / len(introns) * 100)
print(introns[:63] + introns[63:90].lower() + introns[90:])
