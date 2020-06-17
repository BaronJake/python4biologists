file_name = "input/genomic_dna.txt"
with open(file_name) as file:
    content = file.read().strip()
with open("output/coding.txt", "w") as coding:
    coding.write(content[:63] + content[90:])
with open("output/noncoding.txt", "w") as noncoding:
    noncoding.write(content[63:90])


with open("output/fasta.txt", "w") as fasta:
    fasta.write(">ABC123\nATCGTACGATCGATCGATCGATCGCTAGACGTATCG\n")
    fasta.write(">DEF456\n" + "actgatcgacgatcgatcgatcgatcacgact\n".upper())
    fasta.write(">HIJ789\nACTGACACTGTACTGTACATGTG")

with open("output/ABC123.fasta", "w") as abc:
    abc.write(">ABC123\nATCGTACGATCGATCGATCGATCGCTAGACGTATCG")
with open("output/DEF456.fasta", "w") as de:
    de.write(">DEF456\n" + "actgatcgacgatcgatcgatcgatcacgact".upper())
with open("output/HIJ789.fasta", "w") as hij:
    hij.write(">HIJ789\nACTGACACTGTACTGTACATGTG")
