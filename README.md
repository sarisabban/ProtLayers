# ProtLayers
This script points out a PyMol code that highlights the different layers (Surface, Boundery, Core) of a protein.



## DESCRIPTION:
This script does the following:

1. Prints out PYMOL commands to select spesific amino acids in a protein depending on their layer calculated by their SASA (solvent-accessible surface area). These commands allow the user to colour different parts (default: Core=Red, Boundery=Magenta, Surface=Green) of a protein and better visualise it in order to take better decisions on refining it.

This script was written to run on GNU/Linux using python 3, it was not tested in Windows or MacOS.
This script will mostly be useful to refine proteins after a Rosetta FFL (Fold From Loop) computation, but can still be used to refine any protein.
Contact the author at sari.sabban@gmail.com for any questions regarding this script.



## HOW TO USE:
To use follow these steps:

1. Install biopython by running the following command in terminal (python3 -m pip install biopython) you need pip to be installed, if you do not have it you can install it in linux by running the following command in terminal (sudo apt-get install python3-pip).
2. Install DSSP in linux by running the following command in terminal (sudo apt-get install dssp).
3. Install numpy (python3 -m pip install numpy).
4. All files must be in the same directory as this script.
5. Run by navigating to working directory then typing this in the command line to loop through all .pdb files:
`./ProtLayers.py FINENAME.pdb`
6. Select all output all together and paste as is in the pymol terminal.



## REFERENCES:
1. Refere to the paper by (Koga et.al., 2012 - [PMID: 23135467](https://www.ncbi.nlm.nih.gov/pubmed/23135467)) Methods section's Sequence Design Protocol for more explanation on protein refinement and each layer's SASA parameters.
2. Refere to the paper by (Correia et.al., 2014 - [PMID: 24499818](https://www.ncbi.nlm.nih.gov/pubmed/24499818)) for details about the Rosetta Fold From Loop (FFL) protocol.
4. Refere to this [webpage](http://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ) for how to use BioPython.
5. Refere to the references (Cock et.al., 2009 - [PMID: 19304878](https://www.ncbi.nlm.nih.gov/pubmed/19304878)) and (Hamelryck and Manderick, 2003 - [PMID: 14630660](https://www.ncbi.nlm.nih.gov/pubmed/14630660)) regarding the applications used here from biopython.
6. Refere to the references (Kabsch W. and Sander C., 1983 - [PMID: 6667333](https://www.ncbi.nlm.nih.gov/pubmed/6667333)) regading DSSP.
7. Refere to the reference (Tien et.al., 2013 - [PMID: 24278298](https://www.ncbi.nlm.nih.gov/pubmed/24278298)) regarding Wilke SASA parameters.
