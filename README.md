# thermalizer
--
### Automated translation from mesophilic AA sequence to thermally stabilized variant
--

Some notes:
* The environment for this tool can be reconstructed with conda.  It is saved in `environment.yml`
* Requires python 3.6

Overview of files:

| File | Description |
|------|-------------|
| P0_get_genomes.sh | draft sourcing data, ignore for now |
| P1_TableGenerator.py | Extracts all protein sequences from the refseq bacterial and archeael genomes. |
| P2_Table2Fasta | Creates a fasta file with the protein sequences from P1. |
| P3_16S_TableGenerator.py | Extracts 16sRNA sequences from the genome. |
| P4_split_data.py | Splits 16sRNA sequences into thermophilic and mesophilic. |
| P4_16S_blast.py | Aligns 16sRNA sequences. |
| P5_best_hit.py | For each thermophile find its best hit among mesophiles. |
| P6_append_protein.py | Appends corresponding proteins to P5. |
| P7_blastp_njobs.py | Aligns protein sequences from P6 |
| P8_blastp_best_hit.py | For each thermophilic protein find its best hit among mesophilic proteins. |
| P9_blastp_seq_pair.py | Appends sequences according to protein ids from P8. |
| P10_s2s_pytorch.py | Defines the modules for data preprocessing and training. |
| pytorchtools.py | Defines the classes for Encoder, Attention Mechanism, Decoder, EarlyStopping and InferenceDecoder. |
| [Seq2Seq_in_Pytorch.ipynb](Seq2Seq_in_Pytorch.ipynb) | The NLP Demo for a small sample. |
