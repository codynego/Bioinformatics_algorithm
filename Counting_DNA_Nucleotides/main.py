def count_dna(filepath):
    """
    Counts the occurrences of each nucleotide in a DNA sequence.

    :param file: Path to the file containing the DNA sequence.
    :return: A dictionary with nucleotides as keys and their counts as values.
    """
    with open(filepath, 'r') as f:
        dna_sequence = f.read().strip()

    nucleotide_counts = {
        'A': dna_sequence.count('A'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G'),
        'T': dna_sequence.count('T')
    }

    return nucleotide_counts

def main():
    """
    Main function to execute the nucleotide counting.
    """
    file_path = 'rosalind_dna.txt'
    counts = count_dna(file_path)
    
    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"{count} ", end="")

main()