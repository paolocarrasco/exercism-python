def to_rna(dna_strand):
    
    transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    complement = map(lambda n: transcription[n], dna_strand)

    return ''.join(complement)

