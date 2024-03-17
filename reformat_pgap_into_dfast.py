#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio import SeqIO
import sys

# function for changing the format of locaton 
def convert_location(location):
    # reforat location
    start, end, strand = location.start + 1, location.end, location.strand
    if strand == 1:
        location_str = f"{start}..{end}"
    else:
        location_str = f"complement({start}..{end})"
    return location_str

# define the features needed for submission
def convert_feature(feature):
    converted_qualifiers = {
        'product': '',
        'transl_table': '',
        'codon_start': '',
        'locus_tag': '',
        'gene': '',
        'inference': '',
        'note': '',
        'ncRNA_class': ''
    }
    
    # Obtain information from feature.qualifiers
    if 'product' in feature.qualifiers:
        converted_qualifiers['product'] = feature.qualifiers['product'][0]
    if 'transl_table' in feature.qualifiers:
        converted_qualifiers['transl_table'] = feature.qualifiers['transl_table'][0]
    if 'codon_start' in feature.qualifiers:
        converted_qualifiers['codon_start'] = feature.qualifiers['codon_start'][0]
    if 'locus_tag' in feature.qualifiers:
        converted_qualifiers['locus_tag'] = feature.qualifiers['locus_tag'][0]
    if 'gene' in feature.qualifiers:
        converted_qualifiers['gene'] = feature.qualifiers['gene'][0]
    if 'inference' in feature.qualifiers and feature.qualifiers['inference']:
        inference_value = feature.qualifiers['inference'][0]
        # `:`の直後のスペースを除去する
        inference_value = inference_value.replace(': ', ':')
        converted_qualifiers['inference'] = inference_value
    if 'note' in feature.qualifiers:
        converted_qualifiers['note'] = feature.qualifiers['note'][0]
    if 'ncRNA_class' in feature.qualifiers and feature.qualifiers['ncRNA_class']:
        converted_qualifiers['ncRNA_class'] = feature.qualifiers['ncRNA_class'][0]
    
    # change the format of location
    location_str = convert_location(feature.location)
    
    # bind as a tab-separated text
    converted_str = f"{feature.type}\t{location_str}\t"
    
    # recognize whether each qualifier is empty or not
    if converted_qualifiers['product']:
        converted_str += f"product\t{converted_qualifiers['product']}\n"
    if converted_qualifiers['transl_table']:
        converted_str += f"\t\ttransl_table\t{converted_qualifiers['transl_table']}\n"
    if converted_qualifiers['codon_start']:
        converted_str += f"\t\tcodon_start\t{converted_qualifiers['codon_start']}\n"
    if converted_qualifiers['locus_tag']:
        converted_str += f"\t\tlocus_tag\t{converted_qualifiers['locus_tag']}\n"
    if converted_qualifiers['gene']:
        converted_str += f"\t\tgene\t{converted_qualifiers['gene']}\n"
    if converted_qualifiers['inference']:
        converted_str += f"\t\tinference\t{converted_qualifiers['inference']}\n"
    if converted_qualifiers['note']:
        converted_str += f"\t\tnote\t{converted_qualifiers['note']}\n"
    if converted_qualifiers['ncRNA_class']:
        converted_str += f"\t\tncRNA_class\t{converted_qualifiers['ncRNA_class']}\n"
    
    
    return converted_str
    
def remove_gene_features(input_file, output_file):
    # main function
    with open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(input_file, 'genbank'):
            # obtain features other than gene
            for feature in record.features:
                if feature.type == 'source':
                    # write source feature
                    source_location = convert_location(feature.location)
                    out_handle.write(f"{feature.type}\t{source_location}\n")
                elif feature.type != 'gene':
                    # change the format
                    converted_str = convert_feature(feature)
                    out_handle.write(converted_str)

# path for input/output file
input_file = sys.argv[1]
output_file = sys.argv[2]

# run 
remove_gene_features(input_file, output_file)
