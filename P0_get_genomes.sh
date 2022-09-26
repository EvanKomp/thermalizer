#!/bin/bash
HOST=ftp.ncbi.nlm.nih.gov
USER=anonymous
PASSWORD=$ENV_EMAIL

# move to bacteria folder and get GBFF files
cd data/refseq/archaea
lftp -c "open -u $USER,$PASSWORD $HOST; cd /genomes/refseq/archaea; mget -c -O './' /genomes/refseq/archaea/Acidianus_sp._HS-5/latest_assembly_versions/*/*.gbff.gz"

#<EOF
#user $USER $PASSWORD
#cd /genomes/refseq/archaea
#mget -c -O './' /genomes/refseq/archaea/Acidianus_sp._HS-5/latest_assembly_versions/*/*.gbff.gz
#EOF
