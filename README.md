## <center>Supply Code for MDPI Molecules 2020 Draft</center>

#### FlowChart
<p style = "text-align:center;"><img src = "img/MDPI_Molecules_X_ray_2020.png" width = "60%"></p>

<p style = "text-align:center;"><img src = "img/MDPI_Molecules_Summary.png" width = "80%"></p>

#### HBOS
* <font color="red">detection.py</font>, calcualte the HBOS score for each residue of proteins in a folder

* Used to identify the potential anomalous residue in proteins

* Each row in the output csv file contains: protein id, chain id, residue index, residue name, d-sidechain, d-block, phi, psi, chi-1, HBOS of d-sidechain, HBOS of d-block, HBOS of phi, HBOS of psi, HBOS of chi-1

	> python -W ignore HBOS/detection.py datasetFolder Analysis

* <font color="red">NCSAnomaly.py</font>, calcualte the HBOS score for each residue of proteins in a folder

* Used to generate the reference

* Considering NCS byremoving the chains having 95% similarity or above with any other chains in the same protein

* Each row in the output csv file contains: protein id, chain id, residue index, residue name, d-sidechain, d-block, phi, psi, chi-1, HBOS of d-sidechain, HBOS of d-block, HBOS of phi, HBOS of psi, HBOS of chi-1

	> python -W ignore HBOS/NCSAnomaly.py datasetFolder Analysis

* <font color = "red">resolution.py</font>, download cif files by resolution

* Download cif files by release time with RCSB search engine, save them into a download folder

* Use resolution.py to select the cif files downloaded within the specified resolution range by meta data in the corresponding xml files, default range is 0 to 4 angstrom

	> python HBOS/resolution.py cifFolder targetFolder

* <font color = "red">labelling.py</font>, check the label in validation reports for each residue labelled by HBOS score with meta data in the corresponding xml files

	> python HBOS/labelling.py detection.cvs, "detection.cvs" is the output of "detection.py"

* <font color = "red">count.py and countResidue.py</font>, count residue numbers in a dataset for different types of residues

	> python -W ignore count.py cifFolder
	
	> python countResidue.py count.csv, "count.csv" is the output of "count.py"

* <font color = "red">DSSP.py and DSSPResidue.py</font>, check the identify of secondary structure (Helix, Sheet, et. al.) for each residue labelled by HBOS score
	> python DSSP.py detection.py, "detection.py" is the output of "detection.py"
	
	> python DSSPResidue.py dssp.csv, "dssp.csv" is the output of "DSSP.py"

#### Analysis
* Contains the HBOS database

#### Plots
* Some MATLAB functions used for plotting the figures in the draft

#### Datasets
* protein list for each dataset

#### Setup
* The code was written in Python 2.7
* Need BioPython 1.69 or above installed
* Need DSSP module installed
	> conda install -c salilab dssp
* Support cif files only
