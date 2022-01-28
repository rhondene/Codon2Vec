# User Guide 

## Background:
Codon2Vec runs on the command-line and is compatible with both Windows and Unix operating systems. 
## First time setup instructions
1. Download python3 (version 3.7 or higher) https://www.python.org/downloads/. Ensure that python is added to your operating system's path.
2. Download the Codon2Vec repository here: https://github.com/rhondene/Codon2Vec/tree/main/Codon2Vec
3. Unzip the Codon2Vec folder, and open a terminal window in the uncompressed Codon2Vec folder. 
4. Here you will do a one-time installation of the dependencies Codon2Vec needs to run. On the terminal window type the following command:

       python setup.py install
6. Exit the Codon2Vec folder 
Installation is now completed.


## Demonstratioj ofuse Codon2Vec

### 1. Example input files
Codon2Vec takes a fasta file of coding sequences and an expression table that is either comma-separated or tab-separated.  Below are guidelines for how the input files should be formatted:
a. fasta format
[screen shot of fasta]  

b.[screenshot of exprs]

<p><font color='maroon'**Important guidelines:** </font></p>
<li> Ensure that the sequence IDs in the fasta file match the sequence IDs in the expression table. But The fasta and expression table doesn't have to be in the same order or be the same length. </li>
<li> For the fasta file, the program expects that sequence ID immediately follows the fish fin '>' </li>
<li> For the expression table, ensure that the first two columns contain the ID and expression values</li>

### 2. Run Codon2Vec on the command-line

Open a terminal in the working folder containing the input files and Codon2Vec package folder like so:
[inser pic of folder]

To run Codon2Vec with default options, type this command on the terminal:
```console
python ./Codon2Vec -CDS some_input.fasta -exprs some_exprs.csv -outfolder results
```
**An example execution**:

To see all the available options that modifies the model training, type 
       ```console 
       python ./Codon2Vec/ --help
```
  [insert the help pic]
  
  

### 3. Output: 
Successfully running this program writes the model evaluation metrics to the standard output and a text file 





