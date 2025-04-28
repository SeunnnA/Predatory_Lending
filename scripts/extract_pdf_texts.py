# 01: Setup
import os
import pdfplumber
import pandas as pd

# 02: Define Paths
pdf_folder = "../data/raw/web_scrapes/fair_loans/pdfs/"
output_texts = []

# 03: Loop through PDFs and extract text
for pdf_filename in os.listdir(pdf_folder):
    if pdf_filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_filename)
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                full_text = ""
                for page in pdf.pages:
                    full_text += page.extract_text() + "\n"
                output_texts.append(full_text)
                print(f"Extracted: {pdf_filename}")
        except Exception as e:
            print(f"Failed to extract {pdf_filename}: {e}")
            output_texts.append("")  # so we don't misalign rows

# 04: Create DataFrame
pdf_df = pd.DataFrame({
    "text": output_texts,
    "label": ["non_predatory"] * len(output_texts)
})

# Quick check
print(pdf_df.shape)
pdf_df.head()
# Save extracted pdf texts
pdf_df.to_csv("../data/processed/fair_loan_pdfs.csv", index=False)


