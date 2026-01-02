import re

BANKING_KEYWORDS = [
    "bank", "account", "loan", "emi", "interest",
    "credit", "debit", "card", "atm", "balance",
    "deposit", "withdraw", "cheque", "upi",
    "net banking", "mobile banking", "statement",
    "mortgage", "finance"
]

def validate_banking_query(text: str):
    if not text:
        return False, None

    text = text.lower()

    for keyword in BANKING_KEYWORDS:
        if re.search(rf"\b{keyword}\b", text):
            return True, keyword

    return False, None
