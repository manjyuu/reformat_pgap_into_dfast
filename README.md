# reformat_pgap_into_dfast.py

## Introduction
This repository contains a scrippt for reformatting the annotation file created by the NCBI Prokaryotic Genome Annotation Pipeline (PGAP) https://github.com/ncbi/pgap for DDBJ https://www.ddbj.nig.ac.jp/index-e.html submission.
The 'reformat_pgap_into_dfast.py script converts the 'annot.gbk' file, which is included in PGAP output, into the submission format for DDBJ. You can customize the features required for your submission by modifying the 'convert_feature()' function.

Please note that this script only handles the "Features" section. You will need to reformat the other parts (e.g., DBLINK, KEYWORD, etc.) separately.
<!-- This script was created for personal use with the aim of submitting an annotation file for a metagenome-assembled genome. I hope it proves useful. -->

## Environment
python 3.9.9
bio 1.6.2

## Usage
---

python reformat_pgap_into_dfast.py \<input file path\> \<output file path\>

---

## Author 
Riku Sakurai,
PhD student, Tohoku University

riku.sakurai.q5@dc.tohoku.ac.jp
