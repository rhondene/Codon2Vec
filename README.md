# Codon2Vec: Learning the Regulatory Grammar of Codon Optimality to Predict Gene Expression
Codon2Vec is an embedding neural network that predicts 'high' or 'low' gene expression directly from the protein-coding sequences. Embedding neural networks are commonly used for natural language processing (NLP) applications. Analogous to how an English sentence is a string of words,  a gene can be thought of as a string of codons. Similar to how NLP neural networks model English sentences as a non-random sequence of words, we considered a coding sequence as a non-random non-overlapping array of codons (k-mers of length = 3).
![C2V Schema](/C2V_schema.png)

## Biological Principle: 
**Background:** Gene expression is the universal algorithm that transduces biological instructions from DNA to direct the synthesis of proteins, the molecules that ultimately establishes a cell’s identity and function. During gene expression, a segment of DNA – a gene – is first copied into a messenger RNA (mRNA) molecule. This “message” within the mRNA is organized as a sequence of discrete units called <b>codons</b>. Each mRNA codon is then translated by its complementary tRNA molecule into a specific amino acid, the building block of proteins. 
 
**Codon Optimization**: Natural selection has shaped codon usage to function as regulatory grammar for controlling gene expression. Most organisms have evolved an unequal representation of codons for encoding their proteins, a property known as <i>codon usage bias</i>. Additionally, the supply of cognate tRNAs varies among codons, leading to some codons being better translated than others. Indeed, it has been demonstrated in many organisms, that highly expressed mRNAs are biased toward translationally optimal codons that are decoded by abundant tRNAs. As an application, a common strategy in synthetic biology for to improving the expression proteins outside of their native context involves modifying the codon usage of the exogenous mRNAs.

![C2V Schema](/Codon_optimality.png)


## Value Proposition:
1. **Reference-free**Unlike conventional codon usage methods, Codon2Vec does not rely on a priori knowledge of optimal codons from a pre-defined reference genes. The trained model can then be used to predict expression from new sequences.
2. **Potentially captures codon order**: Popular codon usage bias methods are summative and therefore would fail to capture the influence of codon order on gene expression (Cannarozzi et al., 2010). In contrast, because Codon2Vect represents codons as vectors (‘embeddings’) in Euclidean space, in principle, contextually related codons are projected close together embedding space (Mikolov et al, 2013). 
3. **Automates feature selection**:  Moreover, Codon2Vec bypasses the need for artisanal feature selection since it extracts information directly from sequences and expression data, and the function that maps codons to real-valued vectors is also learned during training.

. 




## Copyright Notice 

Codon2Vec Copyright (c) 2021, The Regents of the University of California,
through Lawrence Berkeley National Laboratory (subject to receipt of any
required approvals from the U.S. Dept. of Energy) and University of
California, Merced. All rights reserved.

If you have questions about your rights to use or distribute this software,
please contact Berkeley Lab's Intellectual Property Office at
IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department
of Energy and the U.S. Government consequently retains certain rights.  As
such, the U.S. Government has been granted for itself and others acting on
its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
Software to reproduce, distribute copies to the public, prepare derivative 
works, and perform publicly and display publicly, and to permit others to do so.


****************************
# License Agreement 

### MIT License

Codon2Vec Copyright (c) 2021, The Regents of the University of California,
through Lawrence Berkeley National Laboratory (subject to receipt of any
required approvals from the U.S. Dept. of Energy) and University of
California, Merced. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 

SOFTWARE.
