import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")

# Phan3.3: Trực quan dữ liệu số lượng thí sinh từng khu vực theo nhóm khối thi
cau33 = df[df["KT"].isin(["A", "A1", "B"])]
cau33_plot = cau33.groupby(["KV", "KT"]).size().reset_index(name="Số lượng")

plt.figure(figsize=(10, 6))
sns.barplot(data=cau33_plot, x="KV", y="Số lượng", hue="KT", palette="Set1")
plt.xlabel("Khu vực")
plt.ylabel("Số lượng thí sinh")
plt.title("Số lượng thí sinh theo khu vực và khối thi")
plt.legend(title="Khối thi")
plt.show()