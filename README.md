## <center>Supply Code for MDPI Molecules 2020 Draft</center>

#### FlowChart
<p style = "text-align:center;"><img src = "img/MDPI_Molecules_X_ray_2020.png" width = "60%"></p>

<p style = "text-align:center;"><img src = "img/MDPI_Molecules_Summary.png" width = "60%"></p>

#### HBOS
* Calcualte the HBOS score for each residue of proteins in a folder

* Used to identify the potential anomalous residue in proteins

> python -W ignore HBOS/detection.py datasetFolder Analysis

* Calcualte the HBOS score for each residue of proteins in a folder

* Used to generate the reference

* Considering NCS byremoving the chains having 95% similarity or above with any other chains in the same protein

* Each row in the output csv file contains: protein id, chain id, residue index, residue name, d-sidechain, d-block, phi, psi, chi-1, HBOS of d-sidechain, HBOS of d-block, HBOS of phi, HBOS of psi, HBOS of chi-1

> python -W ignore HBOS/NCSAnomaly.py datasetFolder Analysis

#### Analysis
* Contains the HBOS database

#### Utils

#### Plots

#### Datasets
* protein list for each dataset

#### Setup
* The code was written in Python 2.7
* Need BioPython 1.69 or above installed
* Support cif files only
