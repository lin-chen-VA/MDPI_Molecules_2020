import pandas as pd
import sys

def main():
    """Count the number of residues for each SSE type
    """
    table = pd.read_csv(sys.argv[1], header = None)

    output = {
            'G': [0]*18,
            'H': [0]*18,
            'I': [0]*18,
            'E': [0]*18,
            'B': [0]*18,
            'T': [0]*18,
            'S': [0]*18,
            '-': [0]*18
            }

    residue_types=['ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    SSE_types = ['G', 'H', 'I', 'E', 'B', 'T', 'S', '-']
    outputTable = pd.DataFrame(output, index=residue_types)
    outputTable.at['ARG', '-'] += 1

    for index, row in table.iterrows():
        if row.get(3) in residue_types and row.get(4) in SSE_types:
            outputTable.at[row.get(3), row.get(4)] += 1

    outputTable.to_csv('residue'+sys.argv[1])
    print(outputTable)

if __name__ == '__main__':
    main()
