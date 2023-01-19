# Our initial DNA sequence input.
print(" ")
dna_input = input("Please enter your DNA sequence: ")
dna_sequence = dna_input.upper()
print(" ")

# Validation of our DNA sequence input.
nucleotides = ["A", "T", "G", "C"]

for i in dna_sequence:
    if i not in nucleotides:
        print("Error! Ensure input is one of the four nucleotides: 'A', 'T', 'G', 'C'. Program is not case sensitive.")
        print(" ")
        quit()

print("DNA sequence accepted.")
print(" ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

# This function will take our regular DNA sequence and return the complimentary sequence as a string.
def complimentary_sequence(seq):
    comp = []
    for i in seq:
        if i == "T":
            comp.append("A")
        if i == "A":
            comp.append("T")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")
    return "".join(comp)

complimentary_dna_sequence = complimentary_sequence(dna_sequence)
reverse_complimentary_dna_sequence = complimentary_dna_sequence[::-1]

# Prints the regular and complimentary strands of our DNA sequence of interest.    
print("The forward DNA sequence is:")
print("5' - " + str(dna_sequence))
print(" ")
print("The complimentary DNA sequence is:")
print("3' - " + str(complimentary_dna_sequence))
print(" ")
print("The reverse complimentary DNA sequence is:")
print("5' - " + str(reverse_complimentary_dna_sequence))
print(" ")

# Prints the amount of A-T and G-C pairs there are and what the %G-C content is.
AT_score = 0
GC_score = 0

def percent_GC(seq):
    percent_GC = float((GC_score / (GC_score + AT_score)) * 100) 
    return round(percent_GC, 2)

for base_pair in dna_sequence:
    if base_pair == "A":
        AT_score += 1
    elif base_pair == "T":
        AT_score += 1
    elif base_pair == "G":
        GC_score += 1
    elif base_pair == "C":
        GC_score += 1

print("A-T base pairs: " + str(AT_score))
print("G-C base pairs: " + str(GC_score))
print("G-C percent is: " + str(percent_GC(dna_sequence)) + " %")
print(" ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

# Functions for counting start and stop codons in an RNA sequence.
def count_start_codon(seq):
    return seq.count("AUG")

def count_stop_codon(seq):
    return sum([seq.count("UGA"), seq.count("UAG"), seq.count("UAA")])

# Converts our DNA sequences into RNA transcripts.
forward_transcript = dna_sequence.replace("T", "U")
complimentary_transcript = complimentary_dna_sequence.replace("T", "U")
reverse_complimentary_transcript = reverse_complimentary_dna_sequence.replace("T", "U")
print("The forward RNA transcript is seen below. The program has identified " + str(count_start_codon(forward_transcript)) + " start codons and " + str(count_stop_codon(forward_transcript)) + " stop codons in this RNA sequence.")
print("5' - " + str(forward_transcript))
print(" ")
print("The complimentary RNA transcript is seen below The program has identified " + str(count_start_codon(complimentary_transcript)) + " start codons and " + str(count_stop_codon(complimentary_transcript)) + " stop codons in this RNA sequence.")
print("3' - " + str(complimentary_transcript))
print(" ")
print("The reverse complimentary RNA transcript is seen below. The program has identified " + str(count_start_codon(reverse_complimentary_transcript)) + " start codons and " + str(count_stop_codon(reverse_complimentary_transcript)) + " stop codons in this RNA sequence.")
print("5' - " + str(reverse_complimentary_transcript))
print(" ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

# These questions ask the user if they would like to save a transcript of choice to a text file.
save_q1 = input("Would you like to save one of these transcripts to a text file? Please choose 'Yes' or 'No' to continue: ")

if save_q1.lower() == "no":
    print("Okay. Program complete.")
    quit()
if save_q1.lower() == "yes":
    save_q2 = input("Okay. What sequence would you like to save? Please choose 'Forward', 'Complimentary' or 'Reverse Complimentary': ")
    if save_q2.lower() == "forward":
        with open("rna_seq.txt", "w") as f:
            f.write("The DNA sequence input was:")
            f.write("\n")
            f.write("\n")
            f.write(dna_sequence)
            f.write("\n")
            f.write("\n")
            f.write("The forward RNA transcript returned is:")
            f.write("\n")
            f.write("\n")
            f.write(forward_transcript)
    if save_q2.lower() == "complimentary":
        with open("rna_seq.txt", "w") as f:
            f.write("The DNA sequence input was:")
            f.write("\n")
            f.write("\n")
            f.write(dna_sequence)
            f.write("\n")
            f.write("\n")
            f.write("The complimentary RNA transcript returned is:")
            f.write("\n")
            f.write("\n")
            f.write(complimentary_transcript)
    if save_q2.lower() == "reverse complimentary":
        with open("rna_seq.txt", "w") as f:
            f.write("The DNA sequence input was:")
            f.write("\n")
            f.write("\n")
            f.write(dna_sequence)
            f.write("\n")
            f.write("\n")
            f.write("The reverse complimentary RNA transcript returned is:")
            f.write("\n")
            f.write("\n")
            f.write(reverse_complimentary_transcript)
else:
    print("Invalid choice. Program Closing.")
    quit()

print("Program complete.")
