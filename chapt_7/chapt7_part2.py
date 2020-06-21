import re

with open("input/dna.txt") as file:
    sequence = file.read().strip()


def find_restriction_sites(seq, pattern, restriction_site):
    sites = []
    for match in re.finditer(pattern, seq):
        site = match.start() + restriction_site
        sites.append(site)
    return sites


lengths = [0]
lengths.extend(find_restriction_sites(sequence, "A[AGCT]TAAT", 3))
lengths.extend(find_restriction_sites(sequence, "GC[AG][AT]TG", 4))
lengths.append(len(sequence))
lengths.sort()
for index in range(1, len(lengths)):
    lengths[index] = lengths[index] - lengths[index - 1]
print(lengths)
