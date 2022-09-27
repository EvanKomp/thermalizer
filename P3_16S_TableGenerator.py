import os
from datetime import datetime

from Bio import SeqIO
import numpy as np
import pandas as pd

# Specify data location
homedir = "./data/refseq/"

start_time = datetime.now()

file_count = 0
for root, dirs, files in os.walk(homedir):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith(".gbff"):
            file_count = file_count + 1

current_file = 0
f = open("data/16S_seq_dic.tsv", "w")
f.write("organism\tlocus\tproduct\tsequence\n")
print("Mission start:")
for root, dirs, files in os.walk(homedir):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith(".gbff"):
            current_file += 1
            if current_file % 100 == 0:
                print("{:.2%} complete ({} of {} files)".format(current_file/file_count, current_file, file_count))
            try:
                done = False
                for seq_record in SeqIO.parse(filepath, "genbank"):
                    organism = seq_record.annotations["organism"]
                    for feature in seq_record.features:
                        if feature.type == 'rRNA' and feature.qualifiers['product'][0] == '16S ribosomal RNA':
                            f.write(f"{organism}\t{seq_record.id}\t{feature.qualifiers['product'][0] if 'product' in feature.qualifiers else np.nan}\t{feature.extract(seq_record.seq)}\n")
                            done = True
                            break
                    if done is True:
                        break
                            # commented out the line below to speed up code
                            # f.flush() 
            except AttributeError:
                print(f"parsing of file {filepath} failed")

f.close()

stop_time = datetime.now()
total_time = stop_time - start_time
print("run time was:", total_time)
