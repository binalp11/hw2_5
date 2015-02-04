#! /bin/bash
from __future__ import division

#defines a function to retrive the AT content
def get_at_content(dna, sig_fig=2):
    #sets a variable to hold the dna
    lower_dna = dna
    #makes the lowercase DNA into Uppercase DNA
    upper_dna = lower_dna.upper()
    #removes the nucleotide variable N 
    fixed_dna = upper_dna.replace('N', '')
    #gets the length of the DNA
    length = len(fixed_dna)
    #counts the amount of 'A''s 
    a_count = fixed_dna.count('A')
    #counts the amount of 'A''s 
    t_count = fixed_dna.count('T')
    #calculates the AT content
    at_content = (a_count + t_count) / length
    #returns the value, rounds it at defined significant figures, if not specificied, automatically set at 2 sig figs
    return round(at_content, sig_fig)



my_at_content = get_at_content('ATGCGCGCTAGATATGGGGG',5)
print str(my_at_content)

print get_at_content('ATGGGGGGGGGGCGCGCGCGAATATAT',5)

print get_at_content('accccccatataagggatata',5)


print get_at_content('ATGCGGGGNNNNCCCAATANNNN',5)