import pandas as pd

df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")
df = df.sort_values(by=["GT", "DH2"], ascending=[True, True])
print(df.sort_values(by=["GT", "DH2"], ascending=[True, True]))
