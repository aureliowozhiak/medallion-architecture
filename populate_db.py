from db import DB
import pandas as pd
import os

db = DB(host="localhost", port=5432, database="postgres", user="postgres", password="postgres")
    
for file in os.listdir("02-silver-validated"):
    df = pd.read_parquet(f"02-silver-validated/{file}")

    db.create_table(
        file.replace(".parquet", ""), 
        df.columns.tolist()
    )

    db.insert_data(
        file.replace(".parquet", ""), 
        df
    )