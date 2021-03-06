####Author: Rhondene Wint 
### Converts fasta file to python dictionary


import fix_fasta

def fas2dict(fasta):
    
    headers=[]
    seqs=[]
    """Input: fasta formatted file
    Output: python dictionary of information"""
    
    with open(fasta, 'r') as file:
        for line in file:
            if line.startswith('>'):
                line=line.strip()
                #ID=line.split(sep)[0] #retain only name/ID
                headers.append(line[1:])
            else:
                seqs.append(line.strip())
    
    ## if number of sequences does not equal then call fix_fasta
    if len(seqs)!=len(headers):
        print('Removing internal newlines from fasta file.....')
        headers,seqs = fix_fasta.fix_fasta(fasta)
    assert len(seqs)==len(headers),'Unequal Number of sequences and headers!'
    return dict(zip(headers,seqs))

if __name__=='__main__':
    fas2dict(fasta)
              
                
        