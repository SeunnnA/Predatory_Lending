#!/usr/bin/env python3
# scrape_new_fair_loans.py

# -*- coding: utf-8 -*-
import requests
import os
import re
import time
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

### retrieved list of over 200 fair loan domains from
### https://www.mx.com/blog/biggest-us-credit-unions-by-asset-size/

# 1) Now look for domains list next to this script:
SCRIPT_DIR = os.path.dirname(__file__)
DOMAINS_FILE = os.path.join(SCRIPT_DIR, "fair_loan_domains.txt")

# 2) output to project nonpredatory folders:
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
TXT_OUT = os.path.join(PROJECT_ROOT, "data", "raw", "web_scrapes", "fair_loans", "webpages")
PDF_OUT = os.path.join(PROJECT_ROOT, "data", "raw", "web_scrapes", "fair_loans", "pdfs")

os.makedirs(TXT_OUT, exist_ok=True)
os.makedirs(PDF_OUT, exist_ok=True)

KEYWORDS = ["loan", "disclosure", "terms", "agreement", "truth-in-lending", ".pdf"]

def find_sitemaps(domain):
    try:
        r = requests.get(f"https://{domain}/robots.txt", timeout=10)
        return re.findall(r"(?i)^sitemap:\s*(.+)$", r.text, flags=re.MULTILINE)
    except:
        return []

def parse_sitemap(sitemap_url):
    try:
        r = requests.get(sitemap_url, timeout=10)
        tree = ET.fromstring(r.content)
        for loc in tree.findall(".//{*}loc"):
            yield loc.text
    except Exception as e:
        print(f"  [!] sitemap parse failed {sitemap_url}: {e}")

def sanitize_filename(url):
    name = url.split("://",1)[-1]
    return re.sub(r"[^\w\-\.]", "_", name)[:200]

def scrape_page(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script","style"]):
        tag.decompose()
    return "\n".join(l.strip() for l in soup.get_text().splitlines() if l.strip())

if __name__ == "__main__":
    with open(DOMAINS_FILE) as f:
        domains = [d.strip() for d in f if d.strip()]

    for dom in domains:
        print(f"\n→\ crawling {dom}")
        for sitemap in find_sitemaps(dom):
            print("  sitemap:", sitemap)
            for url in parse_sitemap(sitemap):
                low = url.lower()
                if any(kw in low for kw in KEYWORDS):
                    fn = sanitize_filename(url)
                    try:
                        if low.endswith(".pdf"):
                            out = os.path.join(PDF_OUT, fn + ".pdf")
                            resp = requests.get(url, timeout=20); resp.raise_for_status()
                            with open(out, "wb") as w: w.write(resp.content)
                            print("    [PDF] ", fn)
                        else:
                            txt = scrape_page(url)
                            out = os.path.join(TXT_OUT, fn + ".txt")
                            with open(out, "w", encoding="utf-8") as w: w.write(txt)
                            print("    [TXT] ", fn)
                    except Exception as e:
                        print(f"    [!] failed {url}: {e}")
        time.sleep(1) # pause before next domain
