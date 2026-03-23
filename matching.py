from rapidfuzz import fuzz
import re

def normalize_address(address):
    address = address.lower()
    address = re.sub(r'[^a-z0-9 ]','',address)
    parts = address.split()
    return " ".join(parts[:3])

def similar_name(a,b,threshold=85):
    return fuzz.token_set_ratio(a.lower(),b.lower()) >= threshold
