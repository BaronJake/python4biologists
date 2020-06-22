import re

with open("input/dna.txt") as file:
    sequence = file.read().strip()


def find_restriction_sites(seq, pattern, restriction_site):
    """
    Takes a sequence, a pattern, and where in the pattern the restriction site is
    Returns indexes of restriction sites
    """
    sites = []
    for match in re.finditer(pattern, seq):
        site = match.start() + restriction_site
        sites.append(site)
    return sites


# Add the start and end indexes and create a list of restriction sites
lengths = [0]
lengths.append(len(sequence))
lengths.extend(find_restriction_sites(sequence, "A[AGCT]TAAT", 3))
lengths.extend(find_restriction_sites(sequence, "GC[AG][AT]TG", 4))

# get the restriction sites in the right order and subtract to find fragment lengths
lengths.sort()
for index in range(1, len(lengths)):
    lengths[index] = lengths[index] - lengths[index - 1]
print(lengths)
