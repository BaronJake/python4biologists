# reads a file, and slices off first 14 characters and writes the rest to to an output file
file = open("input/input.txt")
output = open("output/output.txt", "w",)
for line in file:
    seq = line[14:]
    output.write(seq)
    print(len(seq) - 1)
output.close()
file.close()

# opens a file of sequence data, and a file containing exon indexes
# concatenates coding sequences and writes to a new file
with open("input/genomic_dna.txt") as file:
    genomic = file.read()
exons = open("input/exons.txt")
coding = ""
for line in exons:
    start, stop = [int(x) for x in line.split(",")]
    coding = coding + genomic[start:stop]
with open("output/concatSeq.txt", "w",) as concatSeq:
    concatSeq.write(coding)
exons.close()
