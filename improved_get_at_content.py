#! /bin/bash
from __future__ import division

def get_at_content(dna):
    lower_dna = dna
    upper_dna = lower_dna.upper()
    length = len(upper_dna)
    a_count = upper_dna.count('A')
    t_count = upper_dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content



my_at_content = get_at_content('ATGCGCGCTAGATATGGGGG')
print str(my_at_content)

print get_at_content('ATGGGGGGGGGGCGCGCGCGAATATAT')

print get_at_content('accccccatataagggatata')