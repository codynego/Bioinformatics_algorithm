def DNA_to_RNA(file):
    with open(file, 'r') as f:
        sequence = f.read().strip()
        rna = sequence.replace('T', 'U')

        return rna

def main():
    file_path = 'rosalind_rna.txt'
    RNA = DNA_to_RNA(file_path)

    with open('new_rna.txt', 'w') as f:
        f.write(RNA.strip())
    print(RNA.strip())

if __name__ == '__main__':
    main()