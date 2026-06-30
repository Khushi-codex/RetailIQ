import pandas as pd
from database.db import engine
from database.models import Base

# recreate table safely
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# load CSV
df = pd.read_csv("data/train.csv")

# FIX: use fresh connection each time
with engine.begin() as conn:
    df.to_sql(
        name="retail_sales",
        con=conn,
        if_exists="replace",
        index=False
    )

print("Data loaded successfully!")