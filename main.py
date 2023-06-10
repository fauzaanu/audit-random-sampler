import random as rand
import fpdf as fpdf2
import math
from pprint import pprint




# clientname = input("Enter Client Name: \n")
# amt_range = input("Enter amount of ranges: \n")
# process = input("Enter the current process: \n")
# amt_range = int(amt_range)
# samplesize = int(input("Enter the amount of samples: \n"))

clientname = "Client 1"
amt_range = 4
process =   "Process 1"
amt_range = int(amt_range)
samplesize = 25

ranges = dict()
for i in range(amt_range):
    print(f"Range {i+1}:")
    range_start =1
    range_end = input("Enter Range End: \n")
    print("\n")
   # store the ranges in a dictionary
    ranges[i+1] = [range_start, range_end,0]
#print(ranges)

#we are going to add every single range end to a list
range_ends = []
for rangeitem in ranges:
    range_ends.append(int(ranges[rangeitem][1]))
    
totalrangeend = sum(range_ends)
#trying to divide the range end by the total range end
for rangeitem in ranges:
    ranges[rangeitem][2] = int(ranges[rangeitem][1]) / totalrangeend
    
# apportion the samplesize to the ranges
for rangeitem in ranges:
    ranges[rangeitem][2] = int(ranges[rangeitem][2] * samplesize)
    
#rounding the apportioned samplesize
for rangeitem in ranges:
    ranges[rangeitem][2] = round(ranges[rangeitem][2])
    
#checking if the apportioned samplesize is equal to the samplesize
# if not, we add the difference to the first range
if sum([ranges[rangeitem][2] for rangeitem in ranges]) != samplesize:
    ranges[1][2] += samplesize - sum([ranges[rangeitem][2] for rangeitem in ranges])
    
#rint(ranges)

# the third value in the dictionary is the apportioned samplesize
# we are going to generate the samples for each range
# the amount of samples for each range is the third value in the dictionary
# a new dictionary will be created with a fourth value which is a list of the samples
for rangeitem in ranges:
    ranges[rangeitem].append([])
    for i in range(ranges[rangeitem][2]):
        sample = rand.randint(1, int(ranges[rangeitem][1]))
        while sample in ranges[rangeitem]:
            sample = rand.randint(1, int(ranges[rangeitem][1]))
        ranges[rangeitem][3].append(sample)
pprint(ranges)


# {1: [1, '100', 3, [58, 6, 75]],
# 1 represents the range number
# 1 represents the range start and this does not need to be included in the pdf
# 100 represents the range end and this does not need to be included in the pdf
# 3 represents the apportioned samplesize
# [58, 6, 75] represents the samples for the range
# 
# add these information to the pdf using the fpdf library
for rangeitem in ranges:
    print(f"Range {rangeitem}:")
    print(f"Range Start: {ranges[rangeitem][0]}")
    print(f"Range End: {ranges[rangeitem][1]}")
    print(f"Apportioned Sample size: {ranges[rangeitem][2]}")
    print(f"Samples: {ranges[rangeitem][3]}")
    print("\n")
    
    
    
pdf = fpdf2.FPDF()
pdf.add_page()
pdf.set_font("Arial", size=8)
# pdf.image("pdfhead.png", x=0, y=0,)


pdf.cell(200, 10, txt=" ", ln=1, align="L")
pdf.cell(200, 10, txt=f"Client: {clientname}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Process: {process}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Range: 1 - {totalrangeend}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Amount of samples: {samplesize}", ln=1, align="L")
pdf.cell(200, 10, txt=" ", ln=1, align="L")


    
    
for rangeitem in ranges:
    pdf.cell(200, 10, txt=f"Range {rangeitem}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Range Start: {ranges[rangeitem][0]}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Range End: {ranges[rangeitem][1]}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Apportioned Samplesize: {ranges[rangeitem][2]}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Samples: {ranges[rangeitem][3]}", ln=1, align="L")
    pdf.cell(200, 10, txt=" ", ln=1, align="L")
    
pdf.output("sample.pdf")




    





# def clean_sequence_files():
#     with open("sequence1.txt", "w") as f:
#         f.write("")
#     with open("sequence2.txt", "w") as f:
#         f.write("")
        
# def generate_sequence(filename: str):
#     for i in range(int(amount_of_random_samples)):
#         sample = rand.randint(1, int(range_end))
#         while sample in taken_samples:
#             sample = rand.randint(1, int(range_end))
          
#         with open(f"{filename}.txt", "a") as f:
#             f.write(f"{sample} \n")
#         taken_samples.append(rand.randint(1, int(range_end)))
    

# taken_samples = []

        
# clean_sequence_files()
# generate_sequence(filename="sequence1")
# generate_sequence(filename="sequence2")


# pdf = fpdf2.FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.image("pdfhead.png", x=0, y=0,)

# # leaving some white space at the top of the pdf
# for i in range(5):
#     pdf.cell(200, 10, txt=" ", ln=1, align="L")


# pdf.cell(200, 10, txt=f"Client: {clientname}", ln=1, align="L")
# pdf.cell(200, 10, txt=f"Process: {process}", ln=1, align="L")
# pdf.cell(200, 10, txt=f"Range: 1 - {range_end}", ln=1, align="L")
# pdf.cell(200, 10, txt=f"Amount of samples: {amount_of_random_samples}", ln=1, align="L")

# # get the sequence numbers from the text files
# seq1  = []
# seq2 = []

# with open("sequence1.txt", "r") as f:
#     for line in f:
#         seq1.append(line)   
# with open("sequence2.txt", "r") as f:
#     for line in f:
#         seq2.append(line)
   
# # dynamic rows
# row_amount = math.ceil(len(seq1) / 5.0)

# pdf.cell(200, 10, txt="SEQUENCE 1", ln=1, align="C")
# col_width = pdf.w / 5.0
# row_height = pdf.font_size * 2
    
# # Create grid
# seq1_iter = iter(seq1)
# for row in range(row_amount):
#     for col in range(5):
#         x = col * col_width
#         y = row * row_height
#         try:
#             value = next(seq1_iter)
#             pdf.cell(col_width, row_height, txt=f"{value}", ln=0, align="C")
#         except StopIteration:
#             break
#     pdf.cell(200, 10, txt=" ", ln=1, align="L")
    


# pdf.cell(200, 10, txt=" ", ln=1, align="L")
# pdf.cell(200, 10, txt="SEQUENCE 2", ln=1, align="C")


# seq2_iter = iter(seq2)
# for row in range(row_amount):
#     for col in range(5):
#         x = col * col_width
#         y = row * row_height
#         try:
#             value = next(seq2_iter)
#             pdf.cell(col_width, row_height, txt=f"{value}", ln=0, align="C")
#         except StopIteration:
#             break
#     pdf.cell(200, 10, txt=" ", ln=1, align="L")
        
# with open(f"{clientname}.pdf", "wb") as f:
#     pdf.output(f)
    
# input("Done! Press any key to exit...")


    
    