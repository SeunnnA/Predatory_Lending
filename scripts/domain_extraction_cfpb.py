#!/usr/bin/env python3
# domain_extraction_cfpb.py

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse, parse_qs, unquote

# Paths
CSV_PATH = "data/raw/cfpb_complaints.csv"
DOMAINS_TXT = os.path.join("scripts", "predatory_loan_domains.txt")

# 1. Load unique company names from CFPB data
df = pd.read_csv(CSV_PATH)
if "Company" not in df.columns:
    raise ValueError("CSV missing 'Company' column")
companies = sorted(set(df["Company"].dropna().unique()))

# 2. Function to get real website URL from DuckDuckGo
def find_domain_duckduckgo(company_name):
    query = f"{company_name} site"
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        link = soup.find("a", {"class": "result__a"})
        if link and 'href' in link.attrs:
            wrapped_url = link['href']
            parsed = urlparse(wrapped_url)
            qs = parse_qs(parsed.query)
            if 'uddg' in qs:
                real_url = unquote(qs['uddg'][0])
                return real_url
    except Exception as e:
        print(f"[!] Failed to find domain for {company_name}: {e}")
    return None

# 3. Function to clean URL into just the domain
def extract_domain_only(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return None

# 4. Find and store domains
seen = set()
with open(DOMAINS_TXT, "a", encoding="utf-8") as f:
    for company in companies:
        url = find_domain_duckduckgo(company)
        domain = extract_domain_only(url)
        if domain and domain not in seen:
            f.write(domain + "\n")
            seen.add(domain)
            print(f"[✓] Added: {domain}")
        else:
            print(f"[x] Skipped or failed for {company}")
        time.sleep(1) #delay between requests