#!/usr/bin/python

import csv
import sys

def countResidues(row, l):
    name = row[0]
    if name == 'ARG': l[0] += int(row[1])
    if name == 'ASN': l[1] += int(row[1])
    if name == 'ASP': l[2] += int(row[1])
    if name == 'CYS': l[3] += int(row[1])
    if name == 'GLN': l[4] += int(row[1])
    if name == 'GLU': l[5] += int(row[1])
    if name == 'HIS': l[6] += int(row[1])
    if name == 'ILE': l[7] += int(row[1])
    if name == 'LEU': l[8] += int(row[1])
    if name == 'LYS': l[9] += int(row[1])
    if name == 'MET': l[10] += int(row[1])
    if name == 'PHE': l[11] += int(row[1])
    if name == 'PRO': l[12] += int(row[1])
    if name == 'SER': l[13] += int(row[1])
    if name == 'THR': l[14] += int(row[1])
    if name == 'TRP': l[15] += int(row[1])
    if name == 'TYR': l[16] += int(row[1])
    if name == 'VAL': l[17] += int(row[1])

    return l

with open(sys.argv[1], newline='') as f:
    reader = csv.reader(f, delimiter = ',')
    l = [0]*18
    for row in reader:
        countResidues(row, l)

    print(l)
