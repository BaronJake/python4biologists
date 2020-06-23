import os
import sys

# get command line args and sets them to ints
kmer_length = int(sys.argv[1])
cutoff_number = int(sys.argv[2])


def split_kmers(seq, kmer_dict):
    """ updates kmer counts for all kmers in current sequence """
    for index in range(len(seq) - kmer_length + 1):
        kmer = seq[index:index + kmer_length]
        curr_count = kmer_dict.get(kmer, 0)
        kmer_dict[kmer] = curr_count + 1
    return kmer_dict


# lists all files in the input directory with .dna extension
files = os.listdir("input")
files = [file for file in files if file.endswith(".dna")]

kmers = dict()

# reads sequences from files line by line and updates kmer counts
for file in files:
    data = open(f"input/{file}").readlines()
    for line in data:
        kmers = split_kmers(line.lower(), kmers)

# prints kmer if counts are above cutoff
for kmer, count in kmers.items():
    if count > cutoff_number:
        print(f"{kmer} count is {count}")