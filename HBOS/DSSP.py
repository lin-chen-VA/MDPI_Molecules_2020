#!/usr/bin/python3

from Bio.PDB import *
from Bio.PDB.DSSP import DSSP
import shutil
import urllib2
from contextlib import closing

import os
def file_exist(filename):
    """Check if a file exist

    Args:
        filename (str): file name

    Returns:
        bool: True: if the file exists; False, otherwise
    """
    exists = os.path.isfile(filename)
    if exists:
        return True
    else:
        return False

from os import listdir
from os.path import isfile, join
def get_files(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    files = [f for f in files if f.endswith('cif')]
    return files

import sys
import csv
def csv_dict():
    """Build a dict from csv file

    Returns:
        dict: key is the PDB ID, value is a list of residue ID, each residue ID contains chain ID, index, and residue name
    """
    csv_file = sys.argv[1]
    d = {}
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] in d.keys():
                d[row[0]].append([row[1], row[2], row[3]])
            else:
                d[row[0]] = [[row[1], row[2], row[3]]]
    return d

def getPDB(pdb):
    url = 'https://files.rcsb.org/download/'+pdb+'.pdb'
    response = urllib2.urlopen(url)
    the_page = response.read()
    f = open(pdb+'.pdb', 'w')
    f.write(the_page)

def getDSSP(pdb_file):
    parser = PDBParser()
    name = os.path.splitext(os.path.basename(pdb_file))[0]
    structure = parser.get_structure(name, pdb_file)
    model = structure[0]
    dssp = DSSP(model, pdb_file, dssp='mkdssp')
    return dssp

def letter3to1(res):
    if res.upper() == 'ALA': return 'A'
    if res.upper() == 'ARG': return 'R'
    if res.upper() == 'ASN': return 'N'
    if res.upper() == 'ASP': return 'D'
    if res.upper() == 'CYS': return 'C'
    if res.upper() == 'GLN': return 'Q'
    if res.upper() == 'GLU': return 'E'
    if res.upper() == 'GLY': return 'G'
    if res.upper() == 'HIS': return 'H'
    if res.upper() == 'ILE': return 'I'
    if res.upper() == 'LEU': return 'L'
    if res.upper() == 'LYS': return 'K'
    if res.upper() == 'MET': return 'M'
    if res.upper() == 'PHE': return 'F'
    if res.upper() == 'PRO': return 'P'
    if res.upper() == 'SER': return 'S'
    if res.upper() == 'THR': return 'T'
    if res.upper() == 'TRP': return 'W'
    if res.upper() == 'TYR': return 'Y'
    if res.upper() == 'VAL': return 'V'
    return '-'

def getSSE(residue, dssp):
    key = (residue[0], (' ', int(residue[1]), ' ')) # create the dssp key
    name = residue[2]
    dssp_output = dssp[key]
    if letter3to1(name) != dssp_output[1]:
        raise Exception("Residue name does not match ...")
    return dssp_output[2]

import pandas as pd
def main():
    """Identify SSE for detected anomalous residue
    DSSP: conda install -c salilab dssp
    Ref: https://biopython.org/DIST/docs/api/Bio.PDB.DSSP%27-module.html
    """
    #table = pd.read_csv(sys.argv[1], header = None)

    dssp_file = open('dssp.csv', 'a')
    csvdict = csv_dict()
    for pdb in csvdict:
        try:
            getPDB(pdb) # download the pdb file
        except Exception, err:
            print(pdb, err)
            for residue in csvdict[pdb]:
                dssp_file.write(pdb+','+residue[0]+','+residue[1]+','+residue[2]+','+'PDB_Removed'+'\n')
            continue
        dssp = getDSSP(pdb+'.pdb') # create dssp
        residues = csvdict[pdb]
        for residue in residues:
            try:
                SSE = getSSE(residue, dssp)
                dssp_file.write(pdb+','+residue[0]+','+residue[1]+','+residue[2]+','+SSE+'\n')
            except Exception, err:
                print(pdb, err)
                dssp_file.write(pdb+','+residue[0]+','+residue[1]+','+residue[2]+','+'Residue_Name_Not_Match'+'\n')
    dssp_file.close()
    #pdbFiles = list(csvdict.keys())

    #getPDB(pdbFiles[0])

    #table.insert(4, 'validation', value = result_list)
    #table.to_csv('output.csv', index=False, header=False)

if __name__ == '__main__':
    """Identify the SSE for each detected anomalous residue
       >>>python DSSP.py detection.csv
    """
    main()
