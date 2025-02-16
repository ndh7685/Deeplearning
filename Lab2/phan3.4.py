import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")

# Phan4: Trực quan dữ liệu số lượng thí sinh đậu, rớt trên từng nhóm khối thi
df["KQ"] = df["KQXT"].apply(lambda x: "Đậu" if x > 0 else "Rớt")
cau34_plot = df.groupby(["KT", "KQ"]).size().reset_index(name="Số lượng")

plt.figure(figsize=(10, 6))
sns.barplot(data=cau34_plot, x="KT", y="Số lượng", hue="KQ", palette="Set2")
plt.xlabel("Khối thi")
plt.ylabel("Số lượng thí sinh")
plt.title("Số lượng thí sinh đậu, rớt theo từng khối thi")
plt.legend(title="Kết quả")
plt.show()
