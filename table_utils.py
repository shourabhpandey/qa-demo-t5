import pandas as pd

def table_to_text(path):
    df = pd.read_csv(path)
    return df.to_string(index=False)
