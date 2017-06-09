# ProtLayers
This script calculates the different layers (Surface, Boundery, Core) of a protein then opens Pymol to highlight them.



## DESCRIPTION:
This script does the following:

1. Calculates the different layers (Surface, Boundery, Core) of a protein by calculating each amino acid's SASA (solvent-accessible surface area).
2. It then uses this information to write up Pymol commands that colour these different layers in Pymol.
3. It then puts these commands into a temporary (temp) file which is used to open Pymol and execute these commands, this strange setup is done because this script runs in python 3 and the educational Pymol runs python 2 and will not execute all biology related python 2 modules.
4. Pymol will open showing the protein in cartoon structure and each layer highlighted in a different colour.
5. Once Pymol is exited the temp file is deleted.

These commands allow the user to colour different parts (default: Core=Red, Boundery=Magenta, Surface=Green) of a protein and better visualise it in order to take better decisions on refining it.

This script was written to run on GNU/Linux using python 3, it was not tested in Windows or MacOS.
This script will mostly be useful to refine proteins after a Rosetta FFL (Fold From Loop) computation, but can still be used to refine any protein.
Contact the author at sari.sabban@gmail.com for any questions regarding this script.



## HOW TO USE:
To use follow these steps:

1. Install DSSP in linux by running the following command in terminal (sudo apt-get install dssp).
2. Install PyMOL by running the following command in terminal (sudo apt-get install pymol).
3. Install biopython by running the following command in terminal (python3 -m pip install biopython) you need pip to be installed, if you do not have it you can install it in linux by running the following command in terminal (sudo apt-get install python3-pip).
4. Install numpy (python3 -m pip install numpy).
5. The .pdb file must be in the same directory as this script.
6. Run by navigating to working directory then typing this in the command line:
`python3 ProtLayers.py FINENAME.pdb`
7. If you want to apply the code to multiple structures use the ProtLayers_code.py script which will print on the terminal the Pymol code, after which you can copy/paste into the Pymol terminal. That way the layers for multiple structures will be highlighted.


## REFERENCES:
1. Refere to the paper by (Koga et.al., 2012 - [PMID: 23135467](https://www.ncbi.nlm.nih.gov/pubmed/23135467)) Methods section's Sequence Design Protocol for more explanation on protein refinement and each layer's SASA parameters.
2. Refere to the paper by (Correia et.al., 2014 - [PMID: 24499818](https://www.ncbi.nlm.nih.gov/pubmed/24499818)) for details about the Rosetta Fold From Loop (FFL) protocol.
4. Refere to this [webpage](http://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ) for how to use BioPython.
5. Refere to the references (Cock et.al., 2009 - [PMID: 19304878](https://www.ncbi.nlm.nih.gov/pubmed/19304878)) and (Hamelryck and Manderick, 2003 - [PMID: 14630660](https://www.ncbi.nlm.nih.gov/pubmed/14630660)) regarding the applications used here from biopython.
6. Refere to the references (Kabsch W. and Sander C., 1983 - [PMID: 6667333](https://www.ncbi.nlm.nih.gov/pubmed/6667333)) regading DSSP.
7. Refere to the reference (Tien et.al., 2013 - [PMID: 24278298](https://www.ncbi.nlm.nih.gov/pubmed/24278298)) regarding Wilke SASA parameters.
