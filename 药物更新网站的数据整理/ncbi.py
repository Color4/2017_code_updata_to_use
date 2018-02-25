from Bio import Entrez
Entrez.email = "A.N.Other@example.com"     # Always tell NCBI who you are
#handle = Entrez.efetch(db="nucleotide", id="186972394", rettype="gb", retmode="text")
for i in range(100):
    number = 19304878 + i
    handle = Entrez.efetch(db="pubmed", id=number, rettype="gb", retmode="text")
    #print(handle.read())
    #print(handle["DOI"])
    paper_message = handle.read().rstrip().split('\n\n')
    print(len(paper_message))
