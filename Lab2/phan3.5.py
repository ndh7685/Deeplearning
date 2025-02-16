import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")

# Phan5: Trực quan dữ liệu số lượng thí sinh đậu, rớt trên từng nhóm khu vực
df["KQ"] = df["KQXT"].apply(lambda x: "Đậu" if x > 0 else "Rớt")
cau35_plot = df.groupby(["KV", "KQ"]).size().reset_index(name="Số lượng")

plt.figure(figsize=(10, 6))
sns.barplot(data=cau35_plot, x="KV", y="Số lượng", hue="KQ", palette="Set2")
plt.xlabel("Khu vực")
plt.ylabel("Số lượng thí sinh")
plt.title("Số lượng thí sinh đậu, rớt theo từng khu vực")
plt.legend(title="Kết quả")
plt.show()
