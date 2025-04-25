# Identifying Predatory Lending Practices

**By:** Karrington Riley & Oluwaseun Ademiloye  

This project leverages Natural Language Processing (NLP) to detect predatory language in payday loan agreements and credit offers. We aim to build a classification model that distinguishes fair vs. predatory loan terms by analyzing loan documents, consumer complaints, and online discussions. The outcome will be a tool to assist consumers, regulators, and policymakers in identifying unfair lending practices.

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
- Optional: comparison with simple rule-based keyword flagging

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

