from Bio import SeqIO
import re, os

#contig_mapper.py: Assign contigs to different files based on their Kraken2 taxonomy

contig_taxonomy = {}
taxid_list = []
inh = open("kraken2_output.txt")
for line in inh:
    fields = re.split("\t", line)
    contig_taxonomy[fields[1]] = fields[2]
    if fields[2] in taxid_list:
        continue
    else:
        taxid_list.append(fields[2])
#print(contig_taxonomy)    


os.system("rm *_contigs.fasta")

myseqs = SeqIO.index("final.contigs.fa", "fasta")
for id in myseqs:
    taxid = contig_taxonomy[id]
    output_filename = taxid + "_contigs.fasta"
    print(id)
    #if contig_taxonomy[id] == "9606":
    #    print("It's a human contaminant")
    #elif contig_taxonomy[id] == "2697049":
    #    print("It's COVID!") 
    outh = open(output_filename, "a")
    outh.write(">" + id + "\n" + str(myseqs[id].seq) + "\n")
    outh.close()
