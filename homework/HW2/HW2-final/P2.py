def dna_complement(sequence):
    base_dict = {"A": "T", "T":"A", "G": "C", "C": "G"}
    if sequence is None:
        return
    complement_seq = ""
    for char in sequence:
        char = char.upper()
        if char not in base_dict:
            return
        complement_seq += base_dict[char]

    return complement_seq


valid_input = "AATGGC"
print(valid_input)
valid_output = dna_complement(valid_input)
print(valid_output)

invalid_input = "ABCD"
print(invalid_input)
invalid_output = dna_complement(invalid_input)
print(invalid_output)