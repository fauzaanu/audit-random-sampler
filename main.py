import random as rand
import fpdf as fpdf2
import math
import warnings


warnings.filterwarnings("ignore")

clientname = input("Enter Client Name: \n")
range_end = input("Enter Range End: \n")
amount_of_random_samples = input("Enter amount of random samples: \n")
process = input("Enter the current process: \n")

fit


def clean_sequence_files():
    with open("sequence1.txt", "w") as f:
        f.write("")
    with open("sequence2.txt", "w") as f:
        f.write("")
        
def generate_sequence(filename: str):
    for i in range(int(amount_of_random_samples)):
        sample = rand.randint(1, int(range_end))
        while sample in taken_samples:
            sample = rand.randint(1, int(range_end))
          
        with open(f"{filename}.txt", "a") as f:
            f.write(f"{sample} \n")
        taken_samples.append(rand.randint(1, int(range_end)))
    

taken_samples = []

        
clean_sequence_files()
generate_sequence(filename="sequence1")
generate_sequence(filename="sequence2")


pdf = fpdf2.FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.image("pdfhead.png", x=0, y=0,)

# leaving some white space at the top of the pdf
for i in range(5):
    pdf.cell(200, 10, txt=" ", ln=1, align="L")


pdf.cell(200, 10, txt=f"Client: {clientname}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Process: {process}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Range: 1 - {range_end}", ln=1, align="L")
pdf.cell(200, 10, txt=f"Amount of samples: {amount_of_random_samples}", ln=1, align="L")

# get the sequence numbers from the text files
seq1  = []
seq2 = []

with open("sequence1.txt", "r") as f:
    for line in f:
        seq1.append(line)   
with open("sequence2.txt", "r") as f:
    for line in f:
        seq2.append(line)
   
# dynamic rows
row_amount = math.ceil(len(seq1) / 5.0)

pdf.cell(200, 10, txt="SEQUENCE 1", ln=1, align="C")
col_width = pdf.w / 5.0
row_height = pdf.font_size * 2
    
# Create grid
seq1_iter = iter(seq1)
for row in range(row_amount):
    for col in range(5):
        x = col * col_width
        y = row * row_height
        try:
            value = next(seq1_iter)
            pdf.cell(col_width, row_height, txt=f"{value}", ln=0, align="C")
        except StopIteration:
            break
    pdf.cell(200, 10, txt=" ", ln=1, align="L")
    


pdf.cell(200, 10, txt=" ", ln=1, align="L")
pdf.cell(200, 10, txt="SEQUENCE 2", ln=1, align="C")


seq2_iter = iter(seq2)
for row in range(row_amount):
    for col in range(5):
        x = col * col_width
        y = row * row_height
        try:
            value = next(seq2_iter)
            pdf.cell(col_width, row_height, txt=f"{value}", ln=0, align="C")
        except StopIteration:
            break
    pdf.cell(200, 10, txt=" ", ln=1, align="L")
        
with open(f"{clientname}.pdf", "wb") as f:
    pdf.output(f)
    
input("Done! Press any key to exit...")


    
    