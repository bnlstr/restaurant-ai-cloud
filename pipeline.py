import pandas as pd
import requests
from matching import normalize_address, similar_name

def download_permit_data():

    # Missouri open data CSV endpoint
    url = "https://data.mo.gov/resource/6k9t-2f4v.csv?$limit=50000"

    response = requests.get(url)

    with open("liquor_permits.csv","wb") as f:
        f.write(response.content)

def run_pipeline():

    # 🔥 AUTO DOWNLOAD DATA
    download_permit_data()

    df = pd.read_csv("liquor_permits.csv")

    customers = pd.read_csv("data/usfoods_customers.csv")

    results = []

    for _, row in df.iterrows():

        name = str(row.get("case_name") or row.get("business_name"))
        location = str(row.get("location"))

        if not name or not location:
            continue

        skip = False

        for _, cust in customers.iterrows():

            cust_name = str(cust["DBA"])
            cust_addr = str(cust["LOCATION"])

            if normalize_address(cust_addr) == normalize_address(location):
                if similar_name(cust_name, name):
                    skip = True
                    break

        if not skip:
            results.append({
                "name": name,
                "address": location
            })

    return pd.DataFrame(results)
