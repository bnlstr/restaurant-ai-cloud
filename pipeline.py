import pandas as pd
from matching import normalize_address, similar_name

def run_pipeline():

    df = pd.read_csv("liquor_permits.csv")
    customers = pd.read_csv("data/usfoods_customers.csv")

    results = []

    for _, row in df.iterrows():

        name = str(row.get("CASE_NAME") or row.get("BUSINESS_NAME"))
        location = str(row["LOCATION"])

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
