import pandas as pd
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")
df = df.sort_values(by=["GT", "DH2"], ascending=[True, True])
pivot_table = df.pivot_table(values="DH1", index="KT", aggfunc=["count", "sum", "mean", "median", "min", "max", "std", lambda x: x.quantile(0.25), lambda x: x.quantile(0.5), lambda x: x.quantile(0.75)])
pivot_table.columns = ["count", "sum", "mean", "median", "min", "max", "std", "Q1", "Q2", "Q3"]

print(pivot_table)
