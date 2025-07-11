import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import os
import time

# This script scrapes loan disclosures from various credit unions and banks.
# It saves the text content of each page to a separate file in the specified output folder.

# List of URLs (from credit unions, banks, etc.)
urls = [
    "https://www.psecu.com/disclosures",
    "https://www.psecu.com/loans/personal-loans",
    "https://www.navyfederal.org/loans-cards/personal-loans.html",
    "https://www.navyfederal.org/loans-cards/personal-loans/frequently-asked-questions.html",
    "https://www.navyfederal.org/content/dam/nfculibs/pdfs/membership/nfcu_606.pdf",
    "https://www.navyfederal.org/investment-services/disclosures.html",
    "https://www.penfed.org/personal-loans",
    "https://www.penfed.org/forms",
    "https://www.penfed.org/learn/how-to-read-a-personal-loan-agreement-and-its-fees",
    "https://www.navyfederal.org/content/dam/nfculibs/pdfs/other/1015e.pdf",
    "https://www.navyfederal.org/content/dam/nfculibs/pdfs/loans/nfcu_33.pdf",
    "https://www.alliantcreditunion.org/disclosures",
    "https://www.becu.org/-/media/Files/PDF/P-463.pdf",
    "https://www.becu.org/-/media/Files/PDF/550.pdf",
    "https://www.becu.org/loans-and-mortgages/personal",
    "https://www.schoolsfirstfcu.org/products/credit-cards-personal-loans/personal-loan/",
    "https://www.firsttechfed.com/borrow/personal-loans/fixed-rate-loan",
    "https://www.firsttechfed.com/-/media/firsttech-web/documents/other-pdfs/choicerewardsworldmastercardtruthinlendingdisclosure.pdf",
    "https://www.ncsecu.org/loans/personal-loans.html",
    "https://www.ncsecu.org/loans/personal-loans/signature-loans#disclosures",
    "https://www.ncsecu.org/loans/personal-loans/salary-advance",
    "https://www.suncoast.com/For-You/Loans-and-Credit-Cards/Personal-Loans",
    "https://cunamutual.widen.net/s/rd9jkld9zk/5547531_product-specific-disclosures-for-lending",
    "https://www.teachersfcu.org/personal-banking/lending/loans",
    "https://www.teachersfcu.org/personal-banking/lending",
    "https://www.golden1.com/credit-cards-loans/personal-loans",
    "https://www.golden1.com/-/media/golden1/site-documents/disclosures/l-137-credit_agreement_and-truth-in-lending_disclosure.pdf?rev=eb0399451ff84d9d9bcb440617075a21&hash=2B09D6D1F3F31EC8543B172A36B52440",
    "https://www.patelco.org/credit-cards-and-loans/personal-loans/personal-loan",

]

# Setup scrape log file to save urls that were not able to be scraped
# This will be used to track any failures during the scraping process
# and will be helpful for debugging and re-running the script in the future.
log_file = "../data/raw/web_scrapes/scrape_log.txt"
with open(log_file, "w") as f:
    f.write("SCRAPE FAILURES:\n")


# Output folders
base_folder = "../data/raw/web_scrapes/fair_loans/"
pdf_folder = os.path.join(base_folder, "pdfs")
text_folder = os.path.join(base_folder, "webpages")

os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

def download_pdf(url, filename):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(os.path.join(pdf_folder, filename), "wb") as f:
                f.write(response.content)
            print(f"Downloaded PDF: {filename}")
        else:
            raise Exception(f"Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Failed to download PDF: {url} ({e})")
        with open(log_file, "a") as f:
            f.write(f"PDF FAIL: {url} ({e})\n")


# Function to scrape webpage text
def scrape_webpage(url, filename):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            for script in soup(["script", "style"]):
                script.decompose()

            text = soup.get_text(separator="\n")
            text = "\n".join([line.strip() for line in text.split("\n") if line.strip()])

            with open(os.path.join(text_folder, filename), "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Scraped webpage: {filename}")
        else:
            raise Exception(f"Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Failed to scrape webpage: {url} ({e})")
        with open(log_file, "a") as f:
            f.write(f"WEB FAIL: {url} ({e})\n")


# Main loop
for idx, url in enumerate(urls):
    if url.lower().endswith(".pdf"):
        filename = f"fair_loan_{idx+1}.pdf"
        download_pdf(url, filename)
    else:
        filename = f"fair_loan_{idx+1}.txt"
        scrape_webpage(url, filename)
    time.sleep(2)