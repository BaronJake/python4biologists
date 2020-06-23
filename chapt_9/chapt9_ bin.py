"""
Reads sequences from input/*.dna files and writes sequences to different directories based on sequence length
"""
import os

# create directories for different length sequences
bin_dict = dict()
for index in range(1, 11):
    bin_dict[index] = f"output/{index}00-{index}99"
    if not os.path.exists(bin_dict[index]):
        os.mkdir(bin_dict[index])

# lists all files in the input directory with .dna extension
files = os.listdir("input")
files = [file for file in files if file.endswith(".dna")]

# opens all valid files
# checks the length of the sequence on each line
# writes the sequence to the appropriate bin
for file in files:
    data = open(f"input/{file}").readlines()
    for line in data:
        bin_number = len(line) // 100
        output_bin = f"{bin_number}00-{bin_number}99"
        file_number = len(os.listdir(f"output/{output_bin}")) + 1
        output_file = open(f"output/{output_bin}/{file_number}.dna", "w")
        output_file.write(line)
        output_file.close()
