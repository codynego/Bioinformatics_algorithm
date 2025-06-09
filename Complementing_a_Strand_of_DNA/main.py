def DNA_complement(file):
    with open(file, 'r') as f:
        sequence = f.read().strip()
        reverse_sequence = sequence[::-1]
        complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        new_reverse_sequence = ''.join(complement_map[base] for base in reverse_sequence)
        return new_reverse_sequence


complement = DNA_complement('rosalind_revc.txt')
print("complementary sequence:", complement)

with open('compliment.txt', 'w') as f:
    f.write(complement.strip())
