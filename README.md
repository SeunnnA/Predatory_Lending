# Identifying Predatory Lending Practices

**By:** Karrington Riley & Oluwaseun Ademiloye  

This project leverages Natural Language Processing (NLP) to detect predatory language in payday loan agreements and credit offers. We aim to build a classification model that distinguishes fair vs. predatory loan terms by analyzing loan documents, consumer complaints, and online discussions. The outcome will be a tool to assist consumers, regulators, and policymakers in identifying unfair lending practices.

---

## Run Instructions

To reproduce this project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Predatory_Lending.git
   cd Predatory_Lending
   python -m venv env     # create and activate virtual env
   source env/bin/activate  # On Windows use: .\env\Scripts\activate
   pip install -r scripts/requirements.txt   # install dependencies
   jupyter lab   # run the notebooks
   ```
2. Note: The full dataset CSV (~47MB) is not pushed to GitHub due to size. Larger files like the full dataset and trained models can be accessed here: https://drive.google.com/drive/folders/1te6Bwvvu3_KCZZfY4cHUto2I7NCCNiJ4?usp=sharing
   
   To run evaluation directly:
   
   Upload the file full_dataset_with_cleaned.csv to data/processed/
   
   Then run the notebook DS340_Predatory_Lending_notebook.ipynb

3. Colab Alternative

   Upload the notebook to Google Colab

   Manually upload required files (CSV + models) using the file browser
   
   Run cells as usual (no GPU required unless using BERT)

4. Report is in Github listed as DS340 Final Project Report.docx

---

## Context

Predatory lending disproportionately affects low-income and marginalized communities, trapping borrowers in cycles of debt through excessive interest rates, hidden fees, and aggressive repayment structures. Payday loans are a key area of concern.

By developing a reliable NLP-based classifier, our system will help:
- Flag questionable or non-transparent loan terms
- Empower consumer decision-making
- Assist researchers and regulators in auditing loan policies

---

## Core Approach

The **main objective** is to accurately classify full-length loan documents as either _fair_ or _predatory_.

To achieve this, we will:
- **Preprocess & segment** long-form loan agreements
- **Train supervised classification models** using both traditional ML (e.g., SVM, Logistic Regression) and transformer-based models (e.g., BERT)
- **Compare approaches** to identify the best method for handling legal/financial text

Optional extensions (time-permitting):
- **Topic Modeling with LDA** to surface recurring predatory themes
- **Named Entity Recognition (NER)** to extract and evaluate financial terms

---

## Data Sources

We will collect data from both real-world and synthetic sources:

- **CFPB Complaints Database**: Public consumer complaints about payday loans and credit practices.
- **Loan Agreements**: Publicly available contracts from state regulators and watchdog organizations.
- **Fair Lending Documents**: Loan terms from credit unions and non-profit lenders for contrast.
- **Online Discussions**: Web-scraped Reddit and Twitter posts where users share experiences with payday loans.

---

## Methodology

### Classification Strategy

We will experiment with multiple ways of handling document length:

- **Extract key segments** (e.g., interest rates, fees) and classify them
- **Split documents into sentences**, classify individually, then aggregate
- **Use summarization**, then classify the summary
- **Sliding windows** for long inputs with transformers

We will compare performance using:
- Traditional ML models (TF-IDF + SVM, Logistic Regression)
- Transformer models (BERT, RoBERTa via HuggingFace Transformers)

### Evaluation Metrics

- **Precision**, **Recall**, and **F1-score** on a labeled test set
- Real-world case study comparisons

---

## Libraries & Tools

- [`transformers`](https://huggingface.co/transformers) (BERT/DistilBERT)
- [`scikit-learn`](https://scikit-learn.org/)
- [`spaCy`](https://spacy.io/) (for optional NER)
- [`pandas`](https://pandas.pydata.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`nltk`](https://www.nltk.org/) (for basic preprocessing)

---

## Project Timeline

| Date       | Milestone                                      |
|------------|------------------------------------------------|
| March 25   | Data collection & preprocessing complete     |
| April 5    | Initial classification models trained        |
| April 15   | Model evaluation & refinement in progress    |
| April 25   | Prototype tool + final report draft          |
| May 1      | Final in-class presentation                  |

---

## Final Output

- A labeled dataset of fair vs. predatory loan agreements
- Trained and evaluated ML and transformer-based classifiers
- Jupyter notebooks with exploratory and experimental results
- Final report + presentation



